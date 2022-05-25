from distutils.core import setup
from setuptools import find_packages


setup(
    name='Raider',
    version='0.1.0',
    description='Find-and-replace tool for nested data structures.',
    author='Automated Insights',
    author_email='developers@automatedinsights.com',
    url='https://www.automatedinsights.com',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    test_suite='pytest',
    tests_require=['pytest==3.4.0']
)
