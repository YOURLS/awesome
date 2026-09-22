"""Tests for awesome_data: loading, the section registry and URL walking."""

import pytest
import yaml

import awesome_data as data


def write(tmp_path, monkeypatch, filename, text):
    """Point DATA_DIR at a temporary directory holding one file.

    :param tmp_path: pytest's temporary directory.
    :param monkeypatch: pytest's monkeypatch fixture.
    :param filename: Name of the data file to create.
    :param text: Its content.
    :return: None
    """
    (tmp_path / filename).write_text(text, encoding='utf-8')
    monkeypatch.setattr(data, 'DATA_DIR', str(tmp_path))


def test_strict_loader_rejects_duplicate_keys():
    with pytest.raises(yaml.constructor.ConstructorError, match='duplicate key "name"'):
        yaml.load('name: a\nname: b\n', Loader=data.StrictLoader)


@pytest.mark.parametrize('text, message', [
    ('', 'file is empty'),
    ('- a\n- b\n', 'top level must be a mapping'),
    ('other: [1]\n', 'missing top level key "plugins"'),
    ('plugins: []\n', '"plugins" must be a non-empty list'),
    ('plugins: hello\n', '"plugins" must be a non-empty list'),
    ('plugins:\n  - name: a\n  - just a string\n', 'entry 2 under "plugins" is a str'),
])
def test_load_file_rejects_malformed_documents(tmp_path, monkeypatch, text, message):
    write(tmp_path, monkeypatch, 'plugins.yml', text)
    with pytest.raises(data.DataFileError, match=message):
        data.load_file('plugins.yml')


def test_load_file_reports_yaml_errors_with_location(tmp_path, monkeypatch):
    write(tmp_path, monkeypatch, 'plugins.yml', 'plugins:\n  - name: a\n   url: b\n')
    with pytest.raises(data.DataFileError) as info:
        data.load_file('plugins.yml')
    text = str(info.value)
    assert text.startswith('plugins.yml:3:')
    assert '>    3 | ' in text


def test_load_file_reports_missing_file(tmp_path, monkeypatch):
    monkeypatch.setattr(data, 'DATA_DIR', str(tmp_path))
    with pytest.raises(data.DataFileError, match='plugins.yml: cannot be read'):
        data.load_file('plugins.yml')


def test_load_file_accepts_a_valid_document(tmp_path, monkeypatch):
    write(tmp_path, monkeypatch, 'themes.yml', 'themes:\n  - name: a\n    url: https://x\n')
    assert data.load_file('themes.yml') == {'themes': [{'name': 'a', 'url': 'https://x'}]}


@pytest.mark.parametrize('url, expected', [
    ('https://github.com/ozh/plugin', '@ozh'),
    ('https://gist.github.com/someone/abc', '@someone'),
    ('https://gitlab.com/group/project', '@group'),
    ('https://github.com/', 'github.com'),
    ('https://example.org/some/path', 'example.org'),
    ('http://example.org', 'example.org'),
])
def test_owner(url, expected):
    assert data.owner(url) == expected


def test_sort_key_ignores_case_and_punctuation():
    assert data.sort_key('  ∞² Theme!') == '² theme'
    assert data.sort_key('QR-Code') == 'qrcode'
    assert sorted(['b', 'A', '_c'], key=data.sort_key) == ['A', 'b', '_c']


def test_children_only_returns_mappings():
    assert data.children({'urls': [{'url': 'a'}, 'oops', 3]}, 'urls') == [{'url': 'a'}]
    assert data.children({'urls': 'not a list'}, 'urls') == []
    assert data.children({}, 'urls') == []


def test_describe_uses_the_field_or_a_placeholder():
    assert data.describe('plugin', {'name': 'QR'}, 'name') == 'plugin "QR"'
    assert data.describe('plugin', {}, 'name') == 'plugin "<no name>"'
    assert data.describe('guide', {'title': ''}, 'title') == 'guide "<no title>"'


def test_describe_child_extends_the_parent_label_when_children_are_named():
    integrations = data.SECTIONS['integrations.yml']
    translations = data.SECTIONS['translations.yml']
    assert data.describe_child(integrations, 'integration platform "Chrome"', {'name': 'X'}) \
        == 'integration platform "Chrome" / "X"'
    assert data.describe_child(integrations, 'integration platform "Chrome"', {}) \
        == 'integration platform "Chrome" / "<no name>"'
    assert data.describe_child(translations, 'translation "French"', {'url': 'x'}) == 'translation "French"'


def test_all_urls_walks_every_section(documents):
    found = dict(data.all_urls(documents))
    assert found['https://yourls.org/docs'] == 'official link "Docs"'
    assert found['https://github.com/a/beta'] == 'plugin "Beta"'
    assert found['https://github.com/a/sleek'] == 'theme "Sleek"'
    assert found['https://example.org/pt/'] == 'translation "Portuguese"'
    assert found['https://github.com/a/pyourls'] == 'integration platform "Python" / "pyourls"'
    assert found['https://hub.docker.com/_/yourls/'] == 'deployment "Image"'
    assert found['https://example.org/azure'] == 'guide "YOURLS on Azure"'
    assert found['https://oe.cd/'] == 'showcase "https://oe.cd/"'


def test_all_urls_skips_cross_listed_missing_and_malformed(documents):
    documents['integrations.yml']['integrations'][0]['entries'].append(
        {'name': 'Twice', 'url': 'https://example.org/twice', 'cross_listed': True}
    )
    documents['plugins.yml']['plugins'].append({'name': 'No url'})
    documents['plugins.yml']['plugins'].append({'name': 'Bad url', 'url': ['https://x']})
    documents['translations.yml']['translations'].append({'language': 'Broken', 'urls': 'https://x'})
    urls = [url for url, _ in data.all_urls(documents)]
    assert 'https://example.org/twice' not in urls
    assert len(urls) == len(data.all_urls(documents))
    assert all(isinstance(url, str) for url in urls)


def test_sections_cover_the_real_data_files():
    """Smoke test: every registered file loads and has its root key."""
    documents = data.load_all()
    for filename, section in data.SECTIONS.items():
        assert documents[filename][section.key]
        assert ('categories' in documents[filename]) == section.categories
