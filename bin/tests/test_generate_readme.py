"""Tests for generate_readme: building blocks, renderers and assembly."""

import pytest

import generate_readme as readme


# --- Building blocks ---------------------------------------------------------

@pytest.mark.parametrize('label, expected', [
    ('Plugins', 'plugins'),
    ('Install & deploy', 'install--deploy'),
    ('Guides & Tutorials', 'guides--tutorials'),
    ('foo_bar baz', 'foo_bar-baz'),
    ('Plugins ▴', 'plugins-'),
    ('Misc / Others / Unsorted', 'misc--others--unsorted'),
])
def test_anchor_follows_github_rules(label, expected):
    assert readme.anchor(label) == expected


@pytest.mark.parametrize('entry, expected', [
    ({}, ''),
    ({'official': True}, ' ☑️'),
    ({'tested': True}, ' 🧪'),
    ({'official': True, 'tested': True}, ' ☑️🧪'),
    ({'official': False, 'tested': False}, ''),
])
def test_badges_always_start_with_a_single_space(entry, expected):
    assert readme.badges(entry) == expected


def test_parse_heading():
    assert readme.parse_heading('## Plugins ') == (2, 'Plugins')
    assert readme.parse_heading('#### Deep') == (4, 'Deep')
    assert readme.parse_heading('#hashtag') is None
    assert readme.parse_heading('- not a heading') is None


def test_tail_link_and_bullet():
    entry = {'name': 'QR', 'url': 'https://x', 'description': 'Codes.', 'tested': True}
    assert readme.tail('') == ''
    assert readme.tail(None) == ''
    assert readme.tail('Note.') == ' - Note.'
    assert readme.link(entry) == '[QR](https://x) 🧪'
    assert readme.bullet(entry) == '- [QR](https://x) 🧪 - Codes.'
    assert readme.bullet(entry, indent='  ', prefix='Chrome: ') == '  - Chrome: [QR](https://x) 🧪 - Codes.'
    assert readme.bullet({'title': 'T', 'url': 'u'}, 'title', 'note') == '- [T](u)'


def test_bullets_are_sorted_case_insensitively():
    entries = [
        {'name': 'beta', 'url': 'b', 'description': 'B.'},
        {'name': 'Alpha', 'url': 'a', 'description': 'A.'},
    ]
    assert readme.bullets(entries) == ['- [Alpha](a) - A.', '- [beta](b) - B.']


def test_group_by_keeps_order_and_defaults_to_empty():
    groups = readme.group_by([1, 2, 3, 4], lambda n: n % 2)
    assert groups[1] == [1, 3]
    assert groups[0] == [2, 4]
    assert groups[7] == []


def test_section_heading():
    category = {'label': 'Links', 'description': ' Blurb. '}
    assert readme.section(category) == ['### Links', '', 'Blurb.', '']
    assert readme.section(category, ' in other languages', blurb=False) == ['### Links in other languages', '']


def test_render_by_category_skips_empty_categories(documents):
    plugins = documents['plugins.yml']
    block = readme.render_by_category(plugins, 'plugins', readme.bullets)
    assert block == '### Links\n\nBlurb.\n\n- [alpha](https://github.com/a/alpha) ☑️🧪 - First.\n- [Beta](https://github.com/a/beta) - Second.'
    assert '### Misc' not in block


# --- Renderers ---------------------------------------------------------------

def test_render_plugin_index_skips_empty_categories(documents):
    table = readme.render_plugin_index(documents['plugins.yml'])
    assert table == '| Category | Plugins |\n| --- | ---: |\n| [Links](#links) | 2 |'


def test_render_themes(documents):
    assert readme.render_themes(documents['themes.yml']) == '- [Sleek](https://github.com/a/sleek) - A theme.'


def test_render_translations_single_and_multiple_repositories(documents):
    documents['translations.yml']['translations'][0]['official'] = True
    lines = readme.render_translations(documents['translations.yml']).split('\n')
    assert lines == [
        '- [French](https://github.com/a/fr) ☑️ (`fr_FR`)',
        '- Portuguese (`pt_PT`)',
        '  - [@a](https://github.com/a/pt) - Older.',
        '  - [Example](https://example.org/pt/)',
    ]


def test_render_platforms_prefixes_lone_entries_and_nests_the_rest(documents):
    lines = readme.render_platforms(documents['integrations.yml']['integrations'])
    assert lines == [
        # Entry name equals the platform: no prefix.
        '- Chrome: [YOURLS](https://example.org/chrome) - An add-on.',
        # A note forces the nested form even with a single entry.
        '- Linux',
        '  - [Desktop](https://example.org/desktop) - An app.',
        '  - Also on Windows.',
        '- Python: [pyourls](https://github.com/a/pyourls) - A client.',
    ]


def test_render_platforms_drops_the_prefix_when_it_repeats_the_name():
    platforms = [{'platform': 'Ruby', 'entries': [{'name': 'ruby', 'url': 'u', 'description': 'Gem.'}]}]
    assert readme.render_platforms(platforms) == ['- [ruby](u) - Gem.']


def test_render_guide_entries(documents):
    english = [g for g in documents['guides.yml']['guides'] if 'lang' not in g]
    # Platforms sort by name. Azure is in the title so no prefix, Ubuntu has
    # two guides so it nests, Windows is not in the title so it is prefixed.
    assert readme.render_guide_entries(english) == [
        '- [YOURLS on Azure](https://example.org/azure)',
        '- Ubuntu',
        '  - [Ubuntu one](https://example.org/u1)',
        '  - [Ubuntu two](https://example.org/u2) - Newer.',
        '- Windows: [With WAMP](https://example.org/wamp)',
    ]


def test_render_guides_splits_other_languages(documents):
    block = readme.render_guides(documents['guides.yml'])
    assert block.startswith('### Installation guides\n\nBlurb.\n\n')
    assert '\n\n### Installation guides in other languages\n\n- [Sans plateforme](https://example.org/fr)' in block
    assert block.count('Blurb.') == 1
    assert 'Other tutorials' not in block


def test_render_showcases(documents):
    block = readme.render_showcases(documents['showcases.yml'])
    assert '- https://oe.cd/ - Neat.' in block
    assert '- https://mclrn.co/ by [McLaren](https://www.mclaren.com/).' in block


# --- Assembly ----------------------------------------------------------------

def test_add_navigation_marks_headings_and_repoints_links():
    content = '\n'.join([
        '- [Plugins](#plugins) - [Links](#links)',
        '## Plugins',
        '### Links',
        '## Misc',
    ])
    lines = readme.add_navigation(content).split('\n')
    assert lines[0] == '- [Plugins](#plugins-) - [Links](#links-)'
    assert lines[1] == '## Plugins [▴](#custom-top "Back to top")'
    assert lines[2] == '### Links [▵](#plugins- "Back to plugins")'
    assert lines[3] == '## Misc [▴](#custom-top "Back to top")'


def test_check_anchors_reports_dangling_and_duplicated():
    content = '<a name="custom-top"></a>\n## A\n## A\n### B [x](#a "t")\n[x](#a)\n[y](#zz)\n[top](#custom-top)'
    assert readme.check_anchors(content) == (['zz'], ['a'])
    assert readme.check_anchors('## Only\n[l](#only)') == ([], [])


def test_fill_replaces_placeholders_and_rejects_unknown_ones():
    assert readme.fill('a {{ x }} b {{x}}', {'x': 'X\\1'}) == 'a X\\1 b X\\1'
    with pytest.raises(SystemExit, match='unknown placeholder\\(s\\) in template: nope'):
        readme.fill('{{ nope }}', {})


def test_build_from_the_minimal_dataset(documents):
    content = readme.build(documents)
    assert content.startswith(readme.BANNER)
    assert '**2** plugins' in content
    assert readme.check_anchors(content) == ([], [])


def test_build_from_the_real_data():
    """Smoke test: the real data renders without dangling anchors."""
    assert readme.build().startswith(readme.BANNER)


def test_main_check_and_write(tmp_path, monkeypatch, documents, capsys):
    output = tmp_path / 'README.md'
    monkeypatch.setattr(readme, 'OUTPUT', str(output))
    monkeypatch.setattr(readme.data, 'load_all', lambda: documents)

    assert readme.main(['--check']) == 1
    assert 'cannot be read' in capsys.readouterr().err

    assert readme.main([]) == 0
    assert output.read_text(encoding='utf-8') == readme.build(documents)
    assert readme.main(['--check']) == 0

    output.write_text('stale', encoding='utf-8')
    assert readme.main(['--check']) == 1
    assert 'out of date' in capsys.readouterr().err


def test_main_rejects_abbreviated_and_unknown_flags():
    with pytest.raises(SystemExit):
        readme.parse_args(['--che'])
    with pytest.raises(SystemExit):
        readme.parse_args(['--cheque'])
