#!/usr/bin/python
'''
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
'''

import logging
import os
import platform

from setuptools import setup, find_packages

"""
Setup module for core.

Created on 6/24/2015

@author: Alibaba Cloud
"""

PACKAGE = "aliyunsdkcore"
DESCRIPTION = "The core module of Aliyun Python SDK."
AUTHOR = "Alibaba Cloud"
AUTHOR_EMAIL = "alibaba-cloud-sdk-dev-team@list.alibaba-inc.com"
URL = "https://github.com/aliyun/aliyun-openapi-python-sdk"

TOPDIR = os.path.dirname(__file__) or "."
VERSION = __import__(PACKAGE).__version__

with open("README.rst") as fp:
    LONG_DESCRIPTION = fp.read()

requires = [
    "jmespath>=0.9.3,<1.0.0"
]

if platform.system() != "Windows":
    requires.append("pycryptodome>=3.4.7")
else:
    logging.warning(
        "auth type [publicKeyId] is disabled because "
        "'pycrypto' not support windows, we will resolve this soon")

setup_args = {
    'version': VERSION,
    'description': DESCRIPTION,
    'long_description': LONG_DESCRIPTION,
    'author': AUTHOR,
    'author_email': AUTHOR_EMAIL,
    'license': "Apache License 2.0",
    'url': URL,
    'keywords': ["aliyun", "sdk", "core"],
    'packages': find_packages(exclude=["tests*"]),
    'package_data': {'aliyunsdkcore': ['data/*.json', '*.pem', "vendored/*.pem"],
                     'aliyunsdkcore.vendored.requests.packages.certifi': ['cacert.pem']},
    'platforms': 'any',
    'install_requires': requires,
    'classifiers': (
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
    )
}

setup(name='aliyun-python-sdk-core', **setup_args)
