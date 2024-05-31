from setuptools import setup , find_packages

__version__: str = "1.0.0"

setup(
    name="OKX_news_parser",
    version=__version__,
    packages=find_packages(),
    # python_requires=">=3.10.0",
    install_requires=["beautifulsoup4==4.12.2", "requests==2.32.3"],
)
