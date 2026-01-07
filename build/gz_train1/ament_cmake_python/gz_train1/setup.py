from setuptools import find_packages
from setuptools import setup

setup(
    name='gz_train1',
    version='0.0.0',
    packages=find_packages(
        include=('gz_train1', 'gz_train1.*')),
)
