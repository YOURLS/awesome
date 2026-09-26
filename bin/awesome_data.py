"""Shared helpers to load the data files under data/.

Both bin/validate.py and bin/generate_readme.py import this module, so the notion of "where the data lives",
"how each file is shaped" and "who owns which URL" is defined once, in SECTIONS.
"""

import os
from dataclasses import dataclass

import yaml


ROOT: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, 'data')


class DataFileError(Exception):
    """A data file could not be read. Carries a message meant for a human."""


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that rejects duplicate mapping keys.

    PyYAML accepts them and keeps the last one, which turns a missing `-` in a
    list of entries into the silent deletion of the entry above it.
    """


def _no_duplicate_keys(loader, node, deep=False):
    """Build a mapping, refusing any key that appears twice

    :param loader: The active YAML loader
    :param node: The mapping node being constructed
    :param deep: Whether to construct child nodes deeply
    :return: The mapping as a dict
    """
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                'while building a mapping',
                node.start_mark,
                f'duplicate key "{key}" - a missing "-" would do this',
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicate_keys
)


def format_yaml_error(filename, text, error):
    """Turn a YAML exception into a message pointing at the offending line

    :param filename: Name of the file being parsed
    :param text: Full text of the file
    :param error: The MarkedYAMLError raised by PyYAML
    :return: A multi-line, human readable message
    """
    mark = getattr(error, 'problem_mark', None) or getattr(error, 'context_mark', None)
    problem = getattr(error, 'problem', None) or str(error)
    location = f'{filename}:{mark.line + 1}:{mark.column + 1}' if mark else filename

    lines = [f'{location}: {problem}']
    if getattr(error, 'context', None):
        lines.append(f'  {error.context}')
    if mark is None:
        return '\n'.join(lines)

    source = text.splitlines()
    start = max(mark.line - 2, 0)
    for number in range(start, min(mark.line + 2, len(source))):
        prefix = '>' if number == mark.line else ' '
        lines.append(f'  {prefix} {number + 1:>4} | {source[number]}')
        if number == mark.line:
            lines.append(f'      {" " * 4} | {" " * mark.column}^')
    return '\n'.join(lines)



@dataclass(frozen=True)
class Section:
    """How one data file is shaped.

    :param key: Root key holding the list of entries
    :param noun: How an entry is named in messages, eg "plugin"
    :param label: Field naming an entry in messages
    :param categories: Whether the file carries a `categories:` block
    :param nested: Field holding child mappings, when the URLs live there
    :param child_kind: Schema name of a child, for the validator
    :param child_label: Field naming a child in messages. None means a child is only named after its parent
    :param count_children: Whether the summary counts children, not entries
    """

    key: str
    noun: str
    label: str = 'name'
    categories: bool = True
    nested: str = None
    child_kind: str = None
    child_label: str = None
    count_children: bool = False


# Every data file, in README order.
SECTIONS = {
    'official.yml': Section('official', 'official link'),
    'plugins.yml': Section('plugins', 'plugin'),
    'themes.yml': Section('themes', 'theme', categories=False),
    'translations.yml': Section(
        'translations', 'translation', label='language', categories=False,
        nested='urls', child_kind='translation url',
    ),
    'integrations.yml': Section(
        'integrations', 'integration platform', label='platform',
        nested='entries', child_kind='integration entry', child_label='name',
        count_children=True,
    ),
    'deployments.yml': Section('deployments', 'deployment'),
    'guides.yml': Section('guides', 'guide', label='title'),
    'showcases.yml': Section('showcases', 'showcase', label='url'),
}


def load_file(filename):
    """Load a single data file

    :param filename: File name relative to data/, eg 'plugins.yml'
    :return: The parsed document as a dict
    """
    path = os.path.join(DATA_DIR, filename)
    try:
        with open(path, encoding='utf-8') as handle:
            text = handle.read()
    except OSError as error:
        raise DataFileError(f'{filename}: cannot be read ({error.strerror})') from None

    try:
        document = yaml.load(text, Loader=StrictLoader)
    except yaml.MarkedYAMLError as error:
        raise DataFileError(format_yaml_error(filename, text, error)) from None

    if document is None:
        raise DataFileError(f'{filename}: file is empty')
    if not isinstance(document, dict):
        raise DataFileError(f'{filename}: top level must be a mapping, got {type(document).__name__}')

    key = SECTIONS[filename].key
    if key not in document:
        raise DataFileError(f'{filename}: missing top level key "{key}"')
    if not isinstance(document[key], list) or not document[key]:
        raise DataFileError(f'{filename}: "{key}" must be a non-empty list')
    for index, entry in enumerate(document[key], start=1):
        if not isinstance(entry, dict):
            raise DataFileError(
                f'{filename}: entry {index} under "{key}" is a {type(entry).__name__}, '
                f'expected a mapping - check for a stray or missing "-"'
            )

    return document


def load_all():
    """Load every data file.

    :return: Dict mapping file name to parsed document
    """
    return {filename: load_file(filename) for filename in SECTIONS}


def owner(url):
    """Extract the account, or domain, of a URL/repo

    https://github.com/ozh/awesome-plugin -> @ozh
    http://ozh.com/awesome-plugin -> ozh.com

    :param url: Any http(s) URL
    :return: The account name prefixed with @, or the host when the URL isn't a known git host
    """
    forges = ('github.com', 'gist.github.com', 'gitlab.com', 'bitbucket.org', 'codeberg.org')
    parts = url.split('//', 1)[-1].split('/')
    host = parts[0]
    if host in forges and len(parts) > 1 and parts[1]:
        return f'@{parts[1]}'
    return host


def sort_key(text):
    """Build a case- and punctuation-insensitive sort key

    :param text: The string to sort on
    :return: A normalized string
    """
    return ''.join(char for char in text.lower() if char.isalnum() or char.isspace()).strip()


def children(entry, key):
    """Return the list of mappings held under a key, ignoring anything else

    :param entry: The parent dict
    :param key: Field expected to hold a list of dicts, eg 'urls'
    :return: The dict items of that list, or an empty list
    """
    value = entry.get(key)
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def describe(noun, entry, field):
    """Name an entry in a message, eg `plugin "QRCode"`

    :param noun: What the entry is
    :param entry: The entry dict
    :param field: Field holding its name
    :return: The noun and the quoted name, or a placeholder when it has none
    """
    return f'{noun} "{entry.get(field) or f"<no {field}>"}"'


def describe_child(section, parent_label, child):
    """Name a nested entry in a message.

    :param section: The Section the child belongs to
    :param parent_label: The label of the parent, from describe()
    :param child: The child dict
    :return: The parent label, extended with the child name when it has one
    """
    if not section.child_label:
        return parent_label
    return f'{parent_label} / "{child.get(section.child_label) or f"<no {section.child_label}>"}"'


def all_urls(documents):
    """Walk every document and yield each URL with the entry that owns it

    :param documents: Dict returned by load_all()
    :return: List of (url, label) tuples
    """
    found = []

    def add(entry, label):
        """Record one url when the entry actually has one

        :param entry: The entry dict
        :param label: How to name it in messages
        :return: None
        """
        if isinstance(entry.get('url'), str) and entry['url']:
            found.append((entry['url'], label))

    for filename, section in SECTIONS.items():
        for entry in documents[filename][section.key]:
            label = describe(section.noun, entry, section.label)
            if not section.nested:
                add(entry, label)
                continue
            for child in children(entry, section.nested):
                # A cross-platform app listed under Windows and Linux is not
                # a duplicate, it is the same download for two audiences.
                if child.get('cross_listed'):
                    continue
                add(child, describe_child(section, label, child))

    return found
