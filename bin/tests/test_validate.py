"""Tests for validate: every rule, through validate_all on mutated data."""

import pytest

import awesome_data as data
import validate


def errors(documents):
    """Validate and return the errors only.

    :param documents: Dict shaped like awesome_data.load_all().
    :return: List of error messages.
    """
    return validate.validate_all(documents).errors


def plugin(documents, index=0):
    """Shortcut to one plugin of the fixture.

    :param documents: The fixture.
    :param index: Position in the list.
    :return: The plugin dict.
    """
    return documents['plugins.yml']['plugins'][index]


def test_the_minimal_dataset_is_valid(documents):
    report = validate.validate_all(documents)
    assert report.errors == []
    assert report.warnings == []


def test_the_real_data_is_valid():
    """Smoke test: data/ passes, whatever it contains today."""
    assert validate.validate_all(data.load_all()).errors == []


def test_every_schema_kind_is_reachable_from_the_sections():
    used = {'category'}
    for section in data.SECTIONS.values():
        used.add(section.noun)
        if section.child_kind:
            used.add(section.child_kind)
    assert used == set(validate.SCHEMAS)


# --- Fields ------------------------------------------------------------------

def test_unknown_field_with_a_hint(documents):
    plugin(documents)['descripton'] = 'x'
    assert errors(documents) == ['plugin "Beta": unknown field "descripton", did you mean "description"?']


def test_unknown_field_without_a_hint_and_case_insensitive(documents):
    plugin(documents)['completely_wrong'] = 'x'
    plugin(documents)['URL'] = 'x'
    found = errors(documents)
    assert 'plugin "Beta": unknown field "completely_wrong"' in found
    assert 'plugin "Beta": unknown field "URL", did you mean "url"?' in found


def test_unknown_fields_are_checked_on_every_kind(documents):
    documents['deployments.yml']['deployments'][0]['typo'] = 1
    documents['guides.yml']['guides'][0]['titel'] = 1
    documents['showcases.yml']['showcases'][0]['typo'] = 1
    documents['themes.yml']['themes'][0]['category'] = 'x'
    documents['translations.yml']['translations'][0]['urls'][0]['ulr'] = 'x'
    documents['integrations.yml']['integrations'][0]['entries'][0]['descripton'] = 'x'
    documents['integrations.yml']['integrations'][0]['typo'] = 'x'
    documents['official.yml']['categories'][0]['typo'] = 'x'
    documents['guides.yml']['extra'] = 1
    found = errors(documents)
    assert len(found) == 9
    assert 'theme "Sleek": unknown field "category"' in found
    # Two edits away from "url", too far for a three-letter field: no hint.
    assert 'translation "French": unknown field "ulr"' in found
    assert 'integration platform "Python" / "pyourls": unknown field "descripton", did you mean "description"?' in found
    assert 'official.yml category "material": unknown field "typo"' in found
    assert 'guides.yml: unknown field "extra"' in found


def test_missing_required_fields(documents):
    del plugin(documents)['url']
    del documents['guides.yml']['guides'][0]['title']
    documents['translations.yml']['translations'][0]['urls'].append({'note': 'no url'})
    found = errors(documents)
    assert 'plugin "Beta": missing field "url"' in found
    assert 'guide "<no title>": missing field "title"' in found
    assert 'translation "French": missing field "url"' in found


def test_missing_document_level_keys(documents):
    del documents['plugins.yml']['categories']
    assert 'plugins.yml: missing top level key "categories"' in errors(documents)


# --- Categories --------------------------------------------------------------

def test_category_must_be_a_single_known_slug(documents):
    plugin(documents, 0)['category'] = 'nope'
    plugin(documents, 1)['category'] = ['links']
    documents['integrations.yml']['integrations'][0]['category'] = 'nope'
    del documents['showcases.yml']['showcases'][0]['category']
    found = errors(documents)
    assert 'plugin "Beta": unknown category "nope"' in found
    assert 'plugin "alpha": "category" takes a single slug, use "tags" for the rest' in found
    assert 'integration platform "Python": unknown category "nope"' in found
    assert 'showcase "https://oe.cd/": missing field "category"' in found
    assert len(found) == 4


def test_malformed_categories_block(documents):
    documents['plugins.yml']['categories'][0] = 'oops'
    del documents['guides.yml']['categories'][0]['slug']
    documents['showcases.yml']['categories'] = 'oops'
    found = errors(documents)
    assert 'plugins.yml: an entry in "categories" is not a mapping, check for a stray or missing "-"' in found
    assert 'guides.yml category "<no slug>": missing field "slug"' in found
    assert 'showcases.yml: "categories" must be a list' in found


# --- Descriptions ------------------------------------------------------------

@pytest.mark.parametrize('description, message', [
    ('No end', 'does not end with punctuation'),
    ('lower.', 'must start with a capital letter'),
    ('Em — dash.', 'uses an em dash'),
    ('A' * 250 + '.', 'is 251 characters, max is 200'),
    (2024, 'must be text, quote it'),
    (True, 'must be text, quote it'),
])
def test_description_rules(documents, description, message):
    plugin(documents)['description'] = description
    found = errors(documents)
    assert len(found) == 1
    assert found[0].startswith(f'plugin "Beta": description {message}')


def test_description_is_checked_wherever_it_is_allowed(documents):
    documents['showcases.yml']['showcases'][0]['description'] = 'No end'
    documents['integrations.yml']['integrations'][0]['entries'][0]['description'] = 'No end'
    documents['official.yml']['categories'][0]['description'] = 'No end'
    found = errors(documents)
    assert len(found) == 3
    assert 'official.yml category "material": description does not end with punctuation' in found


# --- Tags --------------------------------------------------------------------

def test_tag_rules(documents):
    plugin(documents)['tags'] = ['Links ', 'links', 'a' * 40, '', 'x', 'y', 'z']
    found = errors(documents)
    assert 'plugin "Beta": tag "Links " must be lowercase and trimmed' in found
    assert 'plugin "Beta": empty or non-text tag' in found
    assert 'plugin "Beta": 7 tags, max is 5 - keep the most useful ones' in found
    assert 'plugin "Beta": tag "links" cannot be the same as the entry category' in found
    assert any(found_one.startswith('plugin "Beta": tag "aaaaaaaaaa') for found_one in found)


def test_tags_must_be_a_list_of_strings(documents):
    plugin(documents)['tags'] = 'keyword'
    assert errors(documents) == ['plugin "Beta": "tags" must be a list, eg `[database, driver, pgsql]`']
    plugin(documents)['tags'] = ['a', ['b'], 'a']
    found = errors(documents)
    assert 'plugin "Beta": empty or non-text tag' in found
    assert 'plugin "Beta": duplicate tag' in found


# --- Per field rules ---------------------------------------------------------

def test_screenshot_must_be_a_raw_https_file(documents):
    documents['themes.yml']['themes'][0]['screenshot'] = 'http://github.com/a/b/blob/main/shot.png'
    assert errors(documents) == [
        'theme "Sleek": screenshot must be an https URL',
        'theme "Sleek": screenshot points at a GitHub page, use the raw file URL',
    ]


def test_locale_form_is_a_warning(documents):
    # A bare "uk" is accepted on purpose, see LOCALE.
    documents['translations.yml']['translations'][0]['locale'] = 'en-US'
    report = validate.validate_all(documents)
    assert report.errors == []
    assert report.warnings == ['translation "French": locale "en-US" is not in xx_XX form']


def test_native_is_required_and_must_not_be_blank(documents):
    del documents['translations.yml']['translations'][0]['native']
    assert errors(documents) == ['translation "French": missing field "native"']

    # A blank string passes the required check, which only rejects empty values.
    documents['translations.yml']['translations'][0]['native'] = '  '
    assert errors(documents) == ['translation "French": "native" is blank']


def test_by_url_requires_by(documents):
    del documents['showcases.yml']['showcases'][1]['by']
    assert errors(documents) == ['showcase "https://mclrn.co/": has "by_url" but no "by"']


# --- Uniqueness --------------------------------------------------------------

def test_plugin_names_must_be_unique(documents):
    plugin(documents, 1)['name'] = 'Beta'
    assert errors(documents) == [
        'plugin name "Beta" is used 2 times, it must be unique, '
        'qualify it with the repository name, @author or the site'
    ]


def test_locales_must_be_unique(documents):
    documents['translations.yml']['translations'][1]['locale'] = 'fr_FR'
    assert errors(documents) == ['translation locale "fr_FR" is used 2 times, it must be unique']


def test_missing_locales_are_not_reported_as_duplicates(documents):
    for entry in documents['translations.yml']['translations']:
        del entry['locale']
    assert errors(documents) == [
        'translation "French": missing field "locale"',
        'translation "Portuguese": missing field "locale"',
    ]


# --- Nested lists ------------------------------------------------------------

def test_nested_lists_must_hold_mappings(documents):
    documents['translations.yml']['translations'][0]['urls'] = 'https://x'
    documents['integrations.yml']['integrations'][0]['entries'].append('oops')
    del documents['integrations.yml']['integrations'][1]['entries']
    found = errors(documents)
    assert 'translation "French": "urls" must be a list' in found
    assert 'integration platform "Python": an entry in "entries" is not a mapping, check for a stray or missing "-"' in found
    assert 'integration platform "Chrome": missing field "entries"' in found
    assert len(found) == 3


# --- URLs --------------------------------------------------------------------

def test_urls_must_be_https(documents):
    plugin(documents)['url'] = 'http://github.com/a/beta'
    assert errors(documents) == ['plugin "Beta": url is not https']


def test_shared_urls_are_warnings_unless_cross_listed(documents):
    plugin(documents, 1)['url'] = plugin(documents, 0)['url']
    documents['integrations.yml']['integrations'][1]['entries'].append(
        {'name': 'Twice', 'url': 'https://example.org/desktop', 'description': 'Same app.', 'cross_listed': True}
    )
    report = validate.validate_all(documents)
    assert report.errors == []
    assert report.warnings == ['plugin "alpha": shares its URL with plugin "Beta"']


# --- Command line ------------------------------------------------------------

def test_main_reports_errors_and_exit_code(monkeypatch, documents, capsys):
    plugin(documents)['url'] = 'http://x'
    monkeypatch.setattr(data, 'load_all', lambda: documents)
    assert validate.main(['--quiet']) == 1
    assert '1 error(s):' in capsys.readouterr().err


def test_main_prints_a_summary_unless_quiet(monkeypatch, documents, capsys):
    monkeypatch.setattr(data, 'load_all', lambda: documents)
    assert validate.main([]) == 0
    out = capsys.readouterr().out
    assert 'PLUGIN CATEGORY' in out
    assert 'integrations.yml        3 entries' in out
    assert validate.main(['--quiet']) == 0
    assert capsys.readouterr().out == ''


def test_main_rejects_abbreviated_flags():
    with pytest.raises(SystemExit):
        validate.parse_args(['--quie'])


def test_distance():
    assert validate.distance('kitten', 'sitting') == 3
    assert validate.distance('', 'abc') == 3
    assert validate.distance('same', 'same') == 0
