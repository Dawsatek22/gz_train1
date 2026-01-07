from setuptools import find_packages
from setuptools import setup

setup(
    name='ros_gz_sim',
    version='3.0.3',
    packages=find_packages(
        include=('ros_gz_sim', 'ros_gz_sim.*')),
)
