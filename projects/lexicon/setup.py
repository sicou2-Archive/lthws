try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Lexicon',
    'author': 'sicou2',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['Lexicon'],
    'scripts': [],
    'name': 'lexicon',
}

setup(**config)
