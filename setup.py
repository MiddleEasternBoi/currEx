try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A Python program that uses the "Currency Data API" (https://apilayer.com/marketplace/currency_data-api#documentation-tab) to convert currency values between two currencies.',
    'author': 'Siavash Raissi',
    'url': 'http://nowhereyet.com',
    'download_url': 'http://nowhereyet.com/download',
    'author_email': 'raissisiavash23@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['currEx'],
    'scripts': [],
    'name': 'Currency Exchanger'
}

setup(**config)