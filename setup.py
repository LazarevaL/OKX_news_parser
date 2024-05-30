from setuptools import setup

__version__: str = "1.0"

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")


setup(
    name="OKX_news_parser",
    version=__version__,
    install_requires=install_requires,
), 
url = 'ttps://github.com/LazarevaL/OKX_news_parser',
download_url = 'https://github.com/LazarevaL/OKX_news_parser/tree/main.zip'
