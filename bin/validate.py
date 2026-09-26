#!/usr/bin/env python3
"""Validate every data file under data/ and print a summary.

The shape of each file comes from awesome_data.SECTIONS. What each kind of entry may and must contain comes
from SCHEMAS below, and every rule that applies to a given field is registered in FIELD_CHECKS.
Tunable limits: DESCRIPTION_MAX, TAGS_MAX, TAG_LENGTH_MAX, see below.

Validation protocol and severity :

Fatal and stopping the run at the first bad file:
  - file unreadable, empty, or invalid YAML (reported with line and column)
  - duplicate key in a mapping (most likely a missing "-")
  - top level is not a mapping, or the root key is missing or empty
  - an entry that is not a mapping (most likely a missing "-")

Errors, exit code 1:
  Per kind of entry, see SCHEMAS
    - every required field must be present and non-empty
    - no unknown field: a typo is reported with the closest known field (descripton -> description)
    - "category" takes a single slug from the file's own `categories:` block
    - a field declared unique is not used twice: plugin names, locales
  Per field, see FIELD_CHECKS
    - description: text, starts with a capital, ends with . ! or ?, contains no em dash, at most DESCRIPTION_MAX chars
    - tags: list of lowercase trimmed strings, at most TAGS_MAX, at most TAG_LENGTH_MAX chars each, no duplicate, and
      none equal to the entry category slug
    - screenshot: raw https file URL. Special case for GitHub: no "blob" URL because it serves the file viewer page
    - native: not made of spaces
    - by_url: requires "by"
  Everywhere
    - urls are https, not plain http

Warnings, printed but not fatal:
    - locale not in xx_XX form, which lets "uk" through
    - the same URL used by two entries, unless one is marked cross_listed

Not checked here: whether a link is alive
"""

import argparse
import re
import sys
from collections import Counter
from collections.abc import Set as AbstractSet
from dataclasses import dataclass, field

import awesome_data as data

LOCALE = re.compile(r'^[a-z]{2}(_[A-Z]{2})?$')

DESCRIPTION_MAX = 200
TAGS_MAX = 5
TAG_LENGTH_MAX = 30


@dataclass(frozen=True)
class Schema:
    """What one kind of entry may and must contain.

    :param allowed: Every field the entry may carry
    :param required: Fields that must be present and non-empty
    :param unique: Fields whose value must not repeat across the list
    """

    allowed: AbstractSet[str]
    required: tuple = ()
    unique: dict = field(default_factory=dict)

    def __post_init__(self):
        """Freeze `allowed` so a set literal can be passed in."""
        object.__setattr__(self, 'allowed', frozenset(self.allowed))


BADGES = {'official', 'tested'}
LISTED = {'name', 'url', 'description', 'category'} | BADGES

# Every kind of entry. See awesome_data.SECTIONS for top level entries.
#
# A schema gives three rules, see validate_entries():
#   - `allowed` : `{'slug', 'description', 'this', 'that'}`
#     Anything else is an error, with a "did you mean" hint.
#   - `required` : `('slug', 'description')`
#     Lists the fields that must be present and non-empty.
#   - `unique` : `{'slug': 'what to do'}`
#     Lists the fields with unique value across the list, with a hint on how to resolve the clash.
SCHEMAS = {
    'category': Schema({'slug', 'label', 'description'}, ('slug', 'label', 'description')),
    'plugin': Schema(
        LISTED | {'tags'}, ('name', 'url', 'description'),
        unique={'name': ', qualify it with the repository name, @author or the site'},
    ),
    'theme': Schema({'name', 'url', 'description', 'tags', 'screenshot'} | BADGES, ('name', 'url', 'description')),
    'translation': Schema(
        {'language', 'locale', 'native', 'urls'} | BADGES, ('language', 'locale', 'native', 'urls'),
        unique={'locale': ''},
    ),
    'translation url': Schema({'url', 'note', 'label'}, ('url',)),
    'integration platform': Schema({'platform', 'category', 'note', 'entries'}, ('platform', 'entries')),
    'integration entry': Schema({'name', 'url', 'description', 'cross_listed'} | BADGES, ('name', 'url', 'description')),
    'deployment': Schema(LISTED, ('name', 'url', 'description')),
    'official link': Schema(LISTED, ('name', 'url', 'description')),
    'guide': Schema({'title', 'url', 'category', 'platform', 'lang', 'note'} | BADGES, ('title', 'url')),
    'showcase': Schema({'url', 'category', 'description', 'by', 'by_url'} | BADGES, ('url',)),
}


class Report:
    """Collects errors and warnings raised while validating."""

    def __init__(self):
        """Initialize empty lists"""
        self.errors = []
        self.warnings = []

    def error(self, message):
        """Record a blocking problem

        :param message: Human readable description
        :return: None
        """
        self.errors.append(message)

    def warn(self, message):
        """Record a non-blocking problem

        :param message: Human readable description
        :return: None
        """
        self.warnings.append(message)


def distance(left, right):
    """Levenshtein distance between two short strings - very simple implementation

    :param left: First string
    :param right: Second string
    :return: The number of single-character edits between them
    """
    previous = list(range(len(right) + 1))
    for i, a in enumerate(left, start=1):
        current = [i]
        for j, b in enumerate(right, start=1):
            current.append(min(
                previous[j] + 1,          # deletion
                current[j - 1] + 1,       # insertion
                previous[j - 1] + (a != b)  # substitution
            ))
        previous = current
    return previous[-1]


def check_fields(entry, allowed, label, report):
    """Reject any field the schema does not know about

    :param entry: The entry dict to check
    :param allowed: Set of allowed field names
    :param label: How to name this entry in messages.
    :param report: The Report instance to fill.
    :return: None
    """
    for name in entry:
        if name in allowed:
            continue
        # Suggest the closest known field, but only when it is "close" (a third of the length or less) to reject nonsense
        # Case-insensitive, so "URL" is offered "url" rather than nothing.
        typed = str(name).lower()
        near = min(allowed, key=lambda known: distance(typed, known), default=None)
        hint = ''
        if near and distance(typed, near) <= max(1, len(near) // 3):
            hint = f', did you mean "{near}"?'
        report.error(f'{label}: unknown field "{name}"{hint}')


def check_required(entry, fields, label, report):
    """Ensure every required field is present and non-empty

    :param entry: The entry dict to check
    :param fields: Iterable of required field names
    :param label: How to name this entry in messages
    :param report: The Report instance to fill
    :return: None
    """
    for name in fields:
        if not entry.get(name):
            report.error(f'{label}: missing field "{name}"')


def check_category(entry, known, label, report):
    """Ensure the entry points at one existing category slug

    :param entry: The entry dict
    :param known: Set of valid slugs for the file.
    :param label: How to name this entry in messages
    :param report: The Report instance to fill
    :return: None
    """
    category = entry.get('category')
    if not category:
        report.error(f'{label}: missing field "category"')
    elif isinstance(category, list):
        report.error(f'{label}: "category" takes a single slug, use "tags" for the rest')
    elif category not in known:
        report.error(f'{label}: unknown category "{category}"')


def check_description(entry, label, report):
    """Apply the shared style rules to a description

    :param entry: The entry dict, may have no description
    :param label: How to name this entry in messages
    :param report: The Report instance to fill
    :return: None
    """
    description = entry.get('description')
    if not description:
        return
    if not isinstance(description, str):
        # An unquoted 2024 or yes parses as a number or a boolean
        report.error(f'{label}: description must be text, quote it')
        return
    if not description.endswith(('.', '!', '?')):
        report.error(f'{label}: description does not end with punctuation')
    if '—' in description:
        report.error(f'{label}: description uses an em dash, use a regular dash')
    if description[:1].islower():
        report.error(f'{label}: description must start with a capital letter')
    if len(description) > DESCRIPTION_MAX:
        report.error(
            f'{label}: description is {len(description)} characters, max is {DESCRIPTION_MAX} - make it shorter'
        )


def check_tags(entry, label, report):
    """Check the free-text tags of an entry

    :param entry: The entry dict
    :param label: How to name this entry in messages
    :param report: The Report instance to fill
    :return: None
    """
    tags = entry.get('tags')
    if tags is None:
        return
    if not isinstance(tags, list):
        report.error(f'{label}: "tags" must be a list, eg `[database, driver, pgsql]`')
        return

    for tag in tags:
        if not isinstance(tag, str) or not tag.strip():
            report.error(f'{label}: empty or non-text tag')
            continue
        if tag != tag.lower().strip():
            report.error(f'{label}: tag "{tag}" must be lowercase and trimmed')
        if len(tag) > TAG_LENGTH_MAX:
            report.error(
                f'{label}: tag "{tag[:40]}" is {len(tag)} characters, max is {TAG_LENGTH_MAX}'
            )

    if len(tags) > TAGS_MAX:
        report.error(
            f'{label}: {len(tags)} tags, max is {TAGS_MAX} - keep the most useful ones'
        )
    if len(tags) != len(set(map(str, tags))):
        report.error(f'{label}: duplicate tag')
    if entry.get('category') in tags:
        report.error(f'{label}: tag "{entry["category"]}" cannot be the same as the entry category')


def check_screenshot(entry, label, report):
    """Ensure a screenshot is a raw https file, not a GitHub page

    :param entry: The entry dict
    :param label: How to name this entry in messages
    :param report: The Report instance to fill
    :return: None
    """
    shot = entry.get('screenshot')
    if not shot:
        return
    if not str(shot).startswith('https://'):
        report.error(f'{label}: screenshot must be an https URL')
    if '/blob/' in str(shot):
        report.error(f'{label}: screenshot points at a GitHub page, use the raw file URL')


def check_locale(entry, label, report):
    """Warn about a locale that is not in xx_XX form

    :param entry: The entry dict
    :param label: How to name this entry in messages
    :param report: The Report instance to fill
    :return: None
    """
    locale = entry.get('locale')
    if locale and not LOCALE.match(str(locale)):
        report.warn(f'{label}: locale "{locale}" is not in xx_XX form')


def check_native(entry, label, report):
    """Reject a native name made of spaces

    Presence is enforced by the schema, which requires fields to be non-empty.
    A blank string is not empty, so it gets through and is caught here.

    :param entry: The entry dict
    :param label: How to name this entry in messages
    :param report: The Report instance to fill
    :return: None
    """
    if entry.get('native') and not str(entry['native']).strip():
        report.error(f'{label}: "native" is blank')


def check_by(entry, label, report):
    """Ensure a `by_url` comes with a `by`

    :param entry: The entry dict
    :param label: How to name this entry in messages
    :param report: The Report instance to fill
    :return: None
    """
    if entry.get('by_url') and not entry.get('by'):
        report.error(f'{label}: has "by_url" but no "by"')


# Field name -> rule applied to every kind of entry allowed to carry it.
FIELD_CHECKS = {
    'description': check_description,
    'tags': check_tags,
    'screenshot': check_screenshot,
    'locale': check_locale,
    'native': check_native,
    'by_url': check_by,
}


def check_children(entry, key, label, report):
    """Report anything under a key that is not a list of mappings

    :param entry: The parent dict
    :param key: Field expected to hold a list of dicts
    :param label: How to name the parent in messages
    :param report: The Report instance to fill
    :return: The usable mappings, see awesome_data.children()
    """
    value = entry.get(key)
    if value is not None and not isinstance(value, list):
        report.error(f'{label}: "{key}" must be a list')
    elif isinstance(value, list):
        for item in value:
            if not isinstance(item, dict):
                report.error(f'{label}: an entry in "{key}" is not a mapping, check for a stray or missing "-"')
    return data.children(entry, key)


def check_unique(labelled, name, kind, hint, report):
    """Reject a field value used by more than one entry

    :param labelled: List of (label, entry) pairs
    :param name: The field that must be unique
    :param kind: Schema name, used to word the message
    :param hint: Appended to the message, eg how to rename
    :param report: The Report instance to fill
    :return: None
    """
    counts = Counter(entry.get(name) for _, entry in labelled if entry.get(name))
    for value, count in sorted(counts.items(), key=lambda item: str(item[0])):
        if count > 1:
            report.error(f'{kind} {name} "{value}" is used {count} times, it must be unique{hint}')


def validate_entries(labelled, kind, known, report):
    """Run every schema rule on a list of entries of one kind

    :param labelled: List of (label, entry) pairs
    :param kind: Key into SCHEMAS
    :param known: Set of valid category slugs, when the kind has a category
    :param report: The Report instance to fill
    :return: None
    """
    schema = SCHEMAS[kind]
    for label, entry in labelled:
        check_fields(entry, schema.allowed, label, report)
        check_required(entry, schema.required, label, report)
        if 'category' in schema.allowed:
            check_category(entry, known, label, report)
        for name, check in FIELD_CHECKS.items():
            if name in schema.allowed:
                check(entry, label, report)

    for name, hint in schema.unique.items():
        check_unique(labelled, name, kind, hint, report)


def validate_section(filename, document, report):
    """Validate one data file against its Section and the SCHEMAS.

    :param filename: The file name, key into awesome_data.SECTIONS
    :param document: The parsed document
    :param report: The Report instance to fill
    :return: None
    """
    section = data.SECTIONS[filename]
    allowed = {section.key, 'categories'} if section.categories else {section.key}
    check_fields(document, allowed, filename, report)

    known = set()
    if section.categories:
        if 'categories' not in document:
            report.error(f'{filename}: missing top level key "categories"')
        categories = check_children(document, 'categories', filename, report)
        validate_entries(
            [(data.describe(f'{filename} category', item, 'slug'), item) for item in categories],
            'category', None, report,
        )
        known = {item['slug'] for item in categories if item.get('slug')}

    entries = [
        (data.describe(section.noun, entry, section.label), entry)
        for entry in document[section.key]
    ]
    validate_entries(entries, section.noun, known, report)

    if not section.nested:
        return
    for label, entry in entries:
        validate_entries(
            [
                (data.describe_child(section, label, child), child)
                for child in check_children(entry, section.nested, label, report)
            ],
            section.child_kind, None, report,
        )


def validate_urls(documents, report):
    """Check URL scheme and uniqueness across every file at once

    :param documents: Dict returned by data.load_all()
    :param report: The Report instance to fill
    :return: None
    """
    seen = {}
    for url, label in data.all_urls(documents):
        if not url.startswith('https://'):
            report.error(f'{label}: url is not https')
        if url in seen:
            report.warn(f'{label}: shares its URL with {seen[url]}')
        seen[url] = label


def validate_all(documents):
    """Run every check on every file

    :param documents: Dict returned by data.load_all()
    :return: The filled Report
    """
    report = Report()
    for filename, document in documents.items():
        validate_section(filename, document, report)
    validate_urls(documents, report)
    return report


def summarize(documents):
    """Print counts per file and per plugin category.

    :param documents: Dict returned by data.load_all()
    :return: None
    """
    plugins = documents['plugins.yml']['plugins']
    categories = documents['plugins.yml']['categories']
    counts = Counter(plugin.get('category') for plugin in plugins)
    tags = Counter(tag for plugin in plugins for tag in plugin.get('tags') or [])

    width = max(len(category['label']) for category in categories)
    print(f'{"PLUGIN CATEGORY".ljust(width)}  PLUGINS')
    for category in categories:
        print(f'{category["label"].ljust(width)}  {counts[category["slug"]]:>7}')

    print(f'\n{len(tags)} distinct tags on {sum(1 for p in plugins if p.get("tags"))} plugins')
    print('Most used: ' + ', '.join(f'{tag} ({count})' for tag, count in tags.most_common(8)))
    orphans = sorted(tag for tag, count in tags.items() if count == 1)
    if orphans:
        print(f'Used once ({len(orphans)}): ' + ', '.join(orphans))

    print()
    for filename, section in data.SECTIONS.items():
        entries = documents[filename][section.key]
        count = len(entries)
        if section.count_children:
            count = sum(len(data.children(entry, section.nested)) for entry in entries)
        print(f'{filename.ljust(20)} {count:>4} entries')


def parse_args(argv):
    """Parse the command line

    :param argv: Arguments, without the program name
    :return: The parsed namespace
    """
    parser = argparse.ArgumentParser(
        description='Validate the data files under data/.', allow_abbrev=False,
    )
    parser.add_argument(
        '--quiet', action='store_true',
        help='skip the summary printed when everything is valid',
    )
    return parser.parse_args(argv)


def main(argv=None):
    """Entry point

    :param argv: Command line arguments, defaults to sys.argv[1:]
    :return: Exit status, 0 when every file is valid
    """
    args = parse_args(sys.argv[1:] if argv is None else argv)

    try:
        documents = data.load_all()
    except data.DataFileError as error:
        print(f'\n{error}', file=sys.stderr)
        return 1

    report = validate_all(documents)

    for warning in report.warnings:
        print(f'warning: {warning}')

    if report.errors:
        print(f'\n{len(report.errors)} error(s):', file=sys.stderr)
        for error in report.errors:
            print(f'  - {error}', file=sys.stderr)
        return 1

    if not args.quiet:
        print()
        summarize(documents)
    return 0


if __name__ == '__main__':
    sys.exit(main())
