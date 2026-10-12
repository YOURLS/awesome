#!/usr/bin/env python3
"""Render README.md from README.template.md and the data files under data/.

The template defines the editorial content, this script fills the `{{ placeholder }}` with generated lists.

Usage:
  bin/generate_readme.py           write README.md
  bin/generate_readme.py --check   exit 1 if README.md does not match data (like, has been edited manually)
"""

import argparse
import os
import re
import sys
from collections import Counter, defaultdict

import awesome_data as data

ROOT: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # ROOT annotated as str to prevent PyCharm false warning on 'join'
TEMPLATE = os.path.join(ROOT, 'README.template.md')
OUTPUT = os.path.join(ROOT, 'README.md')

BANNER = (
    '\n\n<!-- GENERATED FILE - DO NOT EDIT. EDIT FILES IN DATA/. SEE CONTRIBUTING.md -->\n\n\n'
)
# Navigation markers appended to headings. Change the glyphs here and
#  - NAV_TO_TOP goes on every "## Section"
#  - NAV_TO_SECTION on every sub-heading below it, pointing back at its parent section.
NAV_TO_TOP = '▴'
NAV_TO_TOP_TARGET = '#custom-top'
NAV_TO_TOP_TITLE = 'Back to top'
NAV_TO_SECTION = '▵'
# {section} is replaced by the parent section title, lowercased.
NAV_TO_SECTION_TITLE = 'Back to {section}'
# Heading levels
NAV_SECTION_LEVEL = 2
NAV_SUB_LEVELS = (3, 4)

# Appended to a guide category label for entries written in another language.
OTHER_LANGUAGES = 'in other languages'

# Badges appended next to items
BADGE_OFFICIAL = '☑️'
BADGE_TESTED = '🧪'

HEADING = re.compile(r'^(#{1,6}) (.*)$')
INTERNAL_LINK = re.compile(r'\]\(#([a-z0-9_-]+)([ )])')


# --- Small building blocks -------------------------------------------------

def anchor(label):
    """Build the GitHub anchor for a heading

    :param label: The heading text
    :return: The anchor, without its leading hash
    """
    # GitHub keeps letters, digits, hyphens, underscores and spaces.
    kept = ''.join(char for char in label.lower() if char.isalnum() or char in ' -_')
    return kept.replace(' ', '-')


def parse_heading(line):
    """Split a Markdown heading line

    :param line: One line of markdown
    :return: Tuple (level, text), or None when the line is not a heading
    """
    match = HEADING.match(line)
    if not match:
        return None
    return len(match.group(1)), match.group(2).strip()


def badges(entry):
    """Render the official and tested badges of an entry.

    :param entry: Any entry dict
    :return: A string starting with a space, or an empty string
    """
    marks = ''
    if entry.get('official'):
        marks += BADGE_OFFICIAL
    if entry.get('tested'):
        marks += BADGE_TESTED
    return f' {marks}' if marks else ''


def tail(text):
    """Render the optional text that follows a link.

    :param text: A description or note, possibly empty
    :return: The text prefixed with a dash, or an empty string
    """
    return f' - {text}' if text else ''


def link(entry, text_key='name'):
    """Render an entry as a markdown link followed by its badges

    :param entry: An entry dict with a url
    :param text_key: Field holding the link text
    :return: The markdown link
    """
    return f'[{entry[text_key]}]({entry["url"]}){badges(entry)}'


def bullet(entry, text_key='name', tail_key='description', indent='', prefix=''):
    """Render an entry as one list item

    :param entry: An entry dict with a url
    :param text_key: Field holding the link text
    :param tail_key: Field holding the text after the link, if any
    :param indent: Leading spaces for nesting
    :param prefix: Text placed before the link, eg "Azure: "
    :return: One markdown line
    """
    return f'{indent}- {prefix}{link(entry, text_key)}{tail(entry.get(tail_key))}'


def by_name(entries, key='name'):
    """Sort entries alphabetically on a field

    :param entries: List of entry dicts
    :param key: Field to sort on
    :return: A new sorted list
    """
    return sorted(entries, key=lambda item: data.sort_key(item[key]))


def bullets(entries):
    """Render entries as a sorted list of bullets

    :param entries: List of entry dicts with name, url and description
    :return: List of Markdown lines
    """
    return [bullet(entry) for entry in by_name(entries)]


def group_by(items, key):
    """Group items, keeping their order within each group.

    :param items: Any iterable
    :param key: Function computing the group of an item
    :return: Dict mapping group to list of items, missing groups are empty
    """
    groups = defaultdict(list)
    for item in items:
        groups[key(item)].append(item)
    return groups


def section(category, suffix='', blurb=True):
    """Render the heading of a category.

    :param category: A category dict with label and description
    :param suffix: Appended to the label
    :param blurb: Whether to quote the category description below it
    :return: List of markdown lines, ending with a blank one
    """
    lines = [f'### {category["label"]}{suffix}', '']
    if blurb:
        lines += [f'{category["description"].strip()}', '']
    return lines


def render_by_category(document, key, render):
    """Render a file as one sub-section per category, in category order

    :param document: A parsed document with a categories block
    :param key: Root key holding the entries
    :param render: Function turning a list of entries into markdown lines
    :return: The markdown block. Empty categories render nothing: no link can point at a dead anchor.
    """
    groups = group_by(document[key], lambda item: item['category'])
    blocks = []
    for category in document['categories']:
        entries = groups[category['slug']]
        if entries:
            blocks.append('\n'.join(section(category) + render(entries)))
    return '\n\n'.join(blocks)


# --- One renderer per placeholder --------------------------------------------

def render_plugin_index(document):
    """Render the category table shown above the plugin list.

    :param document: The parsed plugins.yml document
    :return: A markdown table
    """
    counts = Counter(plugin['category'] for plugin in document['plugins'])

    lines = ['| Category | Plugins |', '| --- | ---: |']
    for category in document['categories']:
        if not counts[category['slug']]:
            continue
        target = f'[{category["label"]}](#{anchor(category["label"])})'
        lines.append(f'| {target} | {counts[category["slug"]]} |')
    return '\n'.join(lines)


def render_plugins(document):
    """Render every plugin section, one per category

    Tags are intentionally not rendered: they are search keywords for awesome.yourls.org only

    :param document: The parsed plugins.yml document
    :return: The markdown block
    """
    return render_by_category(document, 'plugins', bullets)


def render_themes(document):
    """Render the themes list

    :param document: The parsed themes.yml document
    :return: The markdown block
    """
    return '\n'.join(bullets(document['themes']))


def render_translations(document):
    """Render the translations list.

    One repository stays on a single line; several become a nested list.

    :param document: The parsed translations.yml document
    :return: The markdown block
    """
    lines = []
    for entry in by_name(document['translations'], 'language'):
        links = entry['urls']
        if len(links) == 1:
            lines.append(
                f'- [{entry["language"]}]({links[0]["url"]})'
                f'{badges(entry)} (`{entry["locale"]}`){tail(links[0].get("note"))}'
            )
            continue

        lines.append(f'- {entry["language"]} (`{entry["locale"]}`){badges(entry)}')
        for item in links:
            label = item.get('label') or data.owner(item['url'])
            lines.append(f'  - [{label}]({item["url"]}){tail(item.get("note"))}')
    return '\n'.join(lines)


def render_platforms(platforms):
    """Render integration platforms, sorted by name

    A platform holding a single entry renders as one bullet, a platform holding several renders as a nested list.

    :param platforms: List of platform dicts, each with entries
    :return: List of markdown lines
    """
    lines = []
    for platform in by_name(platforms, 'platform'):
        entries = platform['entries']
        if len(entries) == 1 and not platform.get('note'):
            entry = entries[0]
            # Keep platform name when it has information the entry name does not, eg "Chrome" for an add-on named "YOURLS".
            prefix = ''
            if data.sort_key(entry['name']) != data.sort_key(platform['platform']):
                prefix = f'{platform["platform"]}: '
            lines.append(bullet(entry, prefix=prefix))
            continue

        lines.append(f'- {platform["platform"]}')
        lines.extend(bullet(entry, indent='  ') for entry in entries)
        if platform.get('note'):
            lines.append(f'  - {platform["note"]}')
    return lines


def render_integrations(document):
    """Render the integrations, grouped by category then by platform

    :param document: The parsed integrations.yml document
    :return: The markdown block
    """
    return render_by_category(document, 'integrations', render_platforms)


def render_listed(document, key):
    """Render a flat, categorized list of name/url/description entries

    Shared by deployments.yml and official.yml, which have the same structure.

    :param document: The parsed document
    :param key: Root key holding the entries
    :return: The markdown block
    """
    return render_by_category(document, key, bullets)


def render_guide_entries(entries):
    """Render a set of guides, nesting those that share a platform

    :param entries: List of guide dicts
    :return: A list of markdown lines
    """
    groups = group_by(entries, lambda item: item.get('platform', ''))

    lines = []
    for platform in sorted(groups, key=data.sort_key):
        group = by_name(groups[platform], 'title')
        if not platform:
            lines.extend(bullet(entry, 'title', 'note') for entry in group)
            continue
        if len(group) == 1:
            # A lone guide is not nested : keep the platform visible when the title doesn't say it, eg "Windows" for a WAMP guide.
            entry = group[0]
            prefix = '' if platform.lower() in entry['title'].lower() else f'{platform}: '
            lines.append(bullet(entry, 'title', 'note', prefix=prefix))
            continue
        lines.append(f'- {platform}')
        lines.extend(bullet(entry, 'title', 'note', indent='  ') for entry in group)
    return lines


def render_guides(document):
    """Render the guides, split by category then by language.

    Guides written in another language get their own sub-section

    :param document: The parsed guides.yml document
    :return: The markdown block
    """
    blocks = []
    for category in document['categories']:
        in_category = [item for item in document['guides'] if item['category'] == category['slug']]
        english = [item for item in in_category if item.get('lang', 'en') == 'en']
        others = [item for item in in_category if item.get('lang', 'en') != 'en']
        for suffix, entries in (('', english), (f' {OTHER_LANGUAGES}', others)):
            if entries:
                lines = section(category, suffix, blurb=not suffix)
                blocks.append('\n'.join(lines + render_guide_entries(entries)))
    return '\n\n'.join(blocks)


def render_showcase_entries(entries):
    """Render showcases in file order, the site URL being the link text

    :param entries: List of showcase dicts
    :return: List of markdown lines
    """
    lines = []
    for entry in entries:
        line = f'- {entry["url"]}{badges(entry)}'
        if entry.get('by'):
            by = f'[{entry["by"]}]({entry["by_url"]})' if entry.get('by_url') else entry['by']
            line += f' by {by}.'
        lines.append(line + tail(entry.get('description')))
    return lines


def render_showcases(document):
    """Render the showcase section

    :param document: The parsed showcases.yml document
    :return: The markdown block
    """
    return render_by_category(document, 'showcases', render_showcase_entries)


# --- Assembly ----------------------------------------------------------------

def add_navigation(content):
    """Append the navigation markers to every heading

    Done as a final pass so template-written and generated headings are treated the same way

    :param content: The assembled markdown
    :return: The markdown with markers added
    """

    # The marker becomes part of the heading text so we must put it in the anchor :
    # "## Plugins ▴" gives `#plugins-` and not `#plugins`

    # Pass 1 records that shift for every heading.
    moved = {}
    for line in content.split('\n'):
        heading = parse_heading(line)
        if not heading:
            continue
        level, text = heading
        if level == NAV_SECTION_LEVEL:
            moved[anchor(text)] = anchor(f'{text} {NAV_TO_TOP}')
        elif level in NAV_SUB_LEVELS:
            moved[anchor(text)] = anchor(f'{text} {NAV_TO_SECTION}')

    # Pass 2 appends the markers, pointing sub-headings at the shifted anchor of their parent section.
    section_anchor = None
    section_title = None
    lines = []
    for line in content.split('\n'):
        heading = parse_heading(line)
        level, text = heading if heading else (None, None)
        if level == NAV_SECTION_LEVEL:
            section_anchor = moved[anchor(text)]
            section_title = text.lower()
            line = f'{line} [{NAV_TO_TOP}]({NAV_TO_TOP_TARGET} "{NAV_TO_TOP_TITLE}")'
        elif section_anchor and level in NAV_SUB_LEVELS:
            title = NAV_TO_SECTION_TITLE.format(section=section_title)
            line = f'{line} [{NAV_TO_SECTION}](#{section_anchor} "{title}")'
        lines.append(line)

    # Pass 3 repoints every internal link written against the plain anchor, in the template's TOC and in generated tables
    def repoint(match):
        """Rewrite one internal link target

        :param match: Match with the anchor in group 1 and the tail in group 2
        :return: The rewritten link opening
        """
        target = match.group(1)
        return f'](#{moved.get(target, target)}{match.group(2)}'

    return INTERNAL_LINK.sub(repoint, '\n'.join(lines))


def check_anchors(content):
    """Verify that internal links point at existing anchors

    :param content: The final markdown
    :return: Tuple of (dangling anchors, duplicated anchors), both sorted
    """
    targets = Counter()
    for line in content.split('\n'):
        heading = parse_heading(line)
        if heading:
            # [label](url) in a heading contributes its label only
            rendered = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', heading[1])
            targets[anchor(rendered)] += 1
        # The top anchor is declared in the template as <a name="custom-top">.
        for name in re.findall(r'<a name="([^"]+)"', line):
            targets[name] += 1

    used = {match.group(1) for match in INTERNAL_LINK.finditer(content)}
    # GitHub suffixes the second identical heading with "-1"
    duplicated = [name for name, count in targets.items() if count > 1]
    return sorted(used - set(targets)), sorted(duplicated)


def fill(template, values):
    """Replace every {{ placeholder }} of the template

    :param template: The template text
    :param values: Dict mapping placeholder name to rendered block
    :return: The filled text
    """
    missing = set(re.findall(r'\{\{\s*([a-z._]+)\s*\}\}', template)) - set(values)
    if missing:
        raise SystemExit(f'unknown placeholder(s) in template: {", ".join(sorted(missing))}')

    def replace(match):
        """Look up one placeholder

        :param match: Match with the placeholder name in group 1
        :return: The rendered block
        """
        return values[match.group(1)]

    return re.sub(r'\{\{\s*([a-z._]+)\s*\}\}', replace, template)


def render_all(documents):
    """Render every placeholder from the loaded data

    :param documents: Dict returned by data.load_all()
    :return: Dict mapping placeholder name to markdown block
    """
    plugins = documents['plugins.yml']
    return {
        'official.list': render_listed(documents['official.yml'], 'official'),
        'plugins.count': str(len(plugins['plugins'])),
        'plugins.index': render_plugin_index(plugins),
        'plugins.list': render_plugins(plugins),
        'themes.list': render_themes(documents['themes.yml']),
        'translations.list': render_translations(documents['translations.yml']),
        'integrations.list': render_integrations(documents['integrations.yml']),
        'deployments.list': render_listed(documents['deployments.yml'], 'deployments'),
        'guides.list': render_guides(documents['guides.yml']),
        'showcases.list': render_showcases(documents['showcases.yml']),
    }


def build(documents=None):
    """Render the whole README

    :param documents: Dict returned by data.load_all(), loaded when omitted
    :return: The README content as a string
    """
    if documents is None:
        documents = data.load_all()

    with open(TEMPLATE, encoding='utf-8') as handle:
        template = handle.read()

    content = BANNER + add_navigation(fill(template, render_all(documents)))

    dangling, duplicated = check_anchors(content)
    if dangling:
        raise SystemExit('dangling internal link(s): ' + ', '.join(f'#{a}' for a in dangling))
    if duplicated:
        raise SystemExit(
            'duplicated heading anchor(s), links are ambiguous: '
            + ', '.join(f'#{a}' for a in duplicated)
        )

    return content


def parse_args(argv):
    """Parse the command line

    :param argv: Arguments, without the program name
    :return: The parsed namespace
    """
    parser = argparse.ArgumentParser(
        description='Render README.md from README.template.md and data/*.yml.',
        allow_abbrev=False,
    )
    parser.add_argument(
        '--check', action='store_true',
        help='do not write anything, exit 1 if README.md is out of date',
    )
    return parser.parse_args(argv)


def main(argv=None):
    """Entry point

    :param argv: Command line arguments, defaults to sys.argv[1:]
    :return: Exit status, 0 on success or when the README is up to date
    """
    args = parse_args(sys.argv[1:] if argv is None else argv)

    try:
        content = build()
    except data.DataFileError as error:
        print(f'\n{error}', file=sys.stderr)
        return 1

    if args.check:
        try:
            with open(OUTPUT, encoding='utf-8') as handle:
                current = handle.read()
        except OSError as error:
            print(f'README.md cannot be read ({error.strerror}), run without --check to create it.', file=sys.stderr)
            return 1
        if current != content:
            print(
                'README.md is out of date. It is generated from data/*.yml: '
                'edit the data files, not the README.',
                file=sys.stderr,
            )
            return 1
        print('README.md is up to date.')
        return 0

    with open(OUTPUT, 'w', encoding='utf-8') as handle:
        handle.write(content)
    print(f'Wrote {OUTPUT} ({len(content.splitlines())} lines).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
