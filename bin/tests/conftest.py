"""Shared fixtures. Makes bin/ importable and provides a minimal valid dataset.

Tests don't read data/ for their assertions - see MINIMAL below.
"""

import copy
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def category(slug, label='Label', description='Blurb.'):
    """Build one category dict.

    :param slug: The category slug.
    :param label: The heading text.
    :param description: The blurb quoted under the heading.
    :return: A category dict.
    """
    return {'slug': slug, 'label': label, 'description': description}


MINIMAL = {
    'official.yml': {
        'categories': [category('material', 'Official material')],
        'official': [
            {'name': 'Docs', 'url': 'https://yourls.org/docs', 'description': 'The docs.', 'category': 'material'},
        ],
    },
    'plugins.yml': {
        'categories': [category('links', 'Links'), category('misc', 'Misc')],
        'plugins': [
            {'name': 'Beta', 'url': 'https://github.com/a/beta', 'description': 'Second.', 'category': 'links',
             'tags': ['keyword']},
            {'name': 'alpha', 'url': 'https://github.com/a/alpha', 'description': 'First.', 'category': 'links',
             'official': True, 'tested': True},
        ],
    },
    'themes.yml': {
        'themes': [
            {'name': 'Sleek', 'url': 'https://github.com/a/sleek', 'description': 'A theme.',
             'screenshot': 'https://raw.githubusercontent.com/a/sleek/main/shot.png'},
        ],
    },
    'translations.yml': {
        'translations': [
            {'language': 'French', 'locale': 'fr_FR', 'native': 'Français',
             'urls': [{'url': 'https://github.com/a/fr'}]},
            {'language': 'Portuguese', 'locale': 'pt_PT', 'native': 'Português',
             'urls': [{'url': 'https://github.com/a/pt', 'note': 'Older.'},
                      {'url': 'https://example.org/pt/', 'label': 'Example'}]},
        ],
    },
    'integrations.yml': {
        'categories': [category('clients', 'Clients'), category('apps', 'Apps')],
        'integrations': [
            {'platform': 'Python', 'category': 'clients',
             'entries': [{'name': 'pyourls', 'url': 'https://github.com/a/pyourls', 'description': 'A client.'}]},
            {'platform': 'Chrome', 'category': 'apps',
             'entries': [{'name': 'YOURLS', 'url': 'https://example.org/chrome', 'description': 'An add-on.'}]},
            {'platform': 'Linux', 'category': 'apps', 'note': 'Also on Windows.',
             'entries': [{'name': 'Desktop', 'url': 'https://example.org/desktop', 'description': 'An app.'}]},
        ],
    },
    'deployments.yml': {
        'categories': [category('container', 'Containers')],
        'deployments': [
            {'name': 'Image', 'url': 'https://hub.docker.com/_/yourls/', 'description': 'An image.',
             'category': 'container', 'official': True},
        ],
    },
    'guides.yml': {
        'categories': [category('install', 'Installation guides'), category('tutorial', 'Other tutorials')],
        'guides': [
            {'title': 'YOURLS on Azure', 'url': 'https://example.org/azure', 'category': 'install',
             'platform': 'Azure'},
            {'title': 'With WAMP', 'url': 'https://example.org/wamp', 'category': 'install',
             'platform': 'Windows'},
            {'title': 'Ubuntu two', 'url': 'https://example.org/u2', 'category': 'install',
             'platform': 'Ubuntu', 'note': 'Newer.'},
            {'title': 'Ubuntu one', 'url': 'https://example.org/u1', 'category': 'install',
             'platform': 'Ubuntu'},
            {'title': 'Sans plateforme', 'url': 'https://example.org/fr', 'category': 'install', 'lang': 'fr'},
        ],
    },
    'showcases.yml': {
        'categories': [category('design', 'Designs'), category('endorsement', 'Endorsements')],
        'showcases': [
            {'url': 'https://oe.cd/', 'category': 'design', 'description': 'Neat.'},
            {'url': 'https://mclrn.co/', 'category': 'endorsement', 'by': 'McLaren',
             'by_url': 'https://www.mclaren.com/'},
        ],
    },
}


@pytest.fixture
def documents():
    """A fresh deep copy of the minimal valid dataset.

    :return: Dict shaped like awesome_data.load_all().
    """
    return copy.deepcopy(MINIMAL)
