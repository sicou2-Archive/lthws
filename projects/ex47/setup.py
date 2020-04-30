try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'Project for Ex 47',
    'author': 'sicou2',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47',
    }
    
setup(**config)