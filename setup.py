#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
from os import path

from setuptools import find_packages, setup

root_dir = path.dirname(__file__)


# Read a file and return its as a string
def read(file_name):
    return io.open(path.join(root_dir, file_name)).read()


name = 'sls'
version = read(path.join('sls', 'version.py')).split('\'')[1].strip()
description = read('README.md')
short_description = ('SLS is the Storyscript Language Server. It provides '
                     'common editor features like completion to its clients.')

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Environment :: Plugins',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Programming Language :: Other Scripting Engines',
    'Topic :: Office/Business',
    'Topic :: Software Development :: Build Tools',
    'Topic :: Software Development :: Code Generators',
]

requirements = [
    'python-jsonrpc-server==0.1.2',
    'storyscript>=0.12.0',
]


setup(name=name,
      version=version,
      description=short_description,
      long_description=description,
      long_description_content_type='text/markdown',
      classifiers=classifiers,
      download_url=('https://github.com/asyncy/sls/archive/'
                    f'{version}.zip'),
      keywords='storyscript language server vscode asyncy',
      author='Asyncy',
      author_email='support@asyncy.com',
      url='http://storyscript.org',
      license='Apache 2.0',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=requirements,
      entry_points={
          'console_scripts': ['sls=sls.main:cli']
      })
