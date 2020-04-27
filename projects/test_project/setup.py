try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'Test Project Ex46',
    'author': 'BCL',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['TEST_PROJECT'],
    'scripts': [],
    'name': 'testproject',
    }
    
setup(**config)