import os
from setuptools import setup, find_packages

BASEDIR = os.path.dirname(os.path.abspath(__file__))
VERSION = '0.0.3'

# allow setup.py to be run from any path
os.chdir(os.path.normpath(BASEDIR))

setup(
    name='myretail',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    description='myRetail RESTful service',
    long_description='myRetail RESTful service',
    url='https://github.com/meganlkm/myretail-api',
    author='meganlkm'
)
