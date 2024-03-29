# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import sys
from setuptools import setup, find_packages
from sopel_modules.tableflip import __version__


if __name__ == '__main__':
    print('Sopel does not correctly load modules installed with setup.py '
          'directly. Please use "pip install .", or add {}/sopel_modules to '
          'core.extra in your config.'.format(
              os.path.dirname(os.path.abspath(__file__))),
          file=sys.stderr)

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('NEWS') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = [req for req in requirements_file.readlines()]

with open('dev-requirements.txt') as dev_requirements_file:
    dev_requirements = [req for req in dev_requirements_file.readlines()]


setup(
    name='sopel_modules.tableflip',
    version=__version__,
    description='TableFlip module for Sopel',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    author='Walter A. Boring IV',
    author_email='waboring@hemna.com',
    url='https://github.com/hemna/sopel-tableflip',
    packages=find_packages('.'),
    namespace_packages=['sopel_modules'],
    include_package_data=True,
    install_requires=requirements,
    tests_require=dev_requirements,
    test_suite='tests',
    license='Eiffel Forum License, version 2',
)
