try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Super awesome Tic Tac Toe game',
    'author': 'Magnus Walbeck',
    'url': '',
    'download_url': '',
    'author_email': 'mw@mwalbeck.org',
    'version': '0.1',
    'install_requires': [''],
    'packages': ['tictactoe'],
    'scripts': [],
    'name': 'tictactoe'
}

setup(**config)
