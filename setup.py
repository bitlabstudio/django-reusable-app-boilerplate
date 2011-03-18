import os
from setuptools import setup, find_packages
import appname as project_module


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="appname",
    version=project_module.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    keywords='the_keywords',
    packages=find_packages(),
    author='the_author',
    author_email='the_email',
    url="the_url",
    include_package_data=True,
    test_suite='project_module.tests.runtests.runtests',
)
