from setuptools import setup, find_packages

__component_name__ = "bink_test"
__author__ = "Michal Jozwiak"
__author_email__ = "jozw.michal@gmail.com"
__version__ = "0.1"
__description__ = "bink_test"
__long_description__ = """"""


setup(
    name=__component_name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    long_description=__long_description__
    if __long_description__ else __description__,
    packages=find_packages('.')
)