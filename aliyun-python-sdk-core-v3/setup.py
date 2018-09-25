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

from setuptools import setup, find_packages
import os
import platform
import logging

"""
setup module for core.

Created on 6/24/2015

@author: alex
"""
PACKAGE = "aliyunsdkcore"
NAME = "aliyun-python-sdk-core-v3"
DESCRIPTION = "The core module of Aliyun Python3 SDK."
AUTHOR = "Aliyun"
AUTHOR_EMAIL = "aliyun-developers-efficiency@list.alibaba-inc.com"
URL = "http://develop.aliyun.com/sdk/python"

TOPDIR = os.path.dirname(__file__) or "."
VERSION = __import__(PACKAGE).__version__

desc_file = open("README.rst")
try:
    LONG_DESCRIPTION = desc_file.read()
finally:
    desc_file.close()

requires = []
if platform.system() != "Windows":
    requires.append("pycryptodome>=3.4.7")
else:
    logging.warning(
        "auth type [publicKeyId] is disabled because 'pycrypto' not support windows, we will resolve this soon")


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache",
    url=URL,
    keywords=["aliyun", "sdk", "core"],
    packages=find_packages(exclude=["tests*"]),
    package_data={'aliyunsdkcore' : ['endpoint/*.json']},
    # include_package_data=True,   # FIXME this line must be deleted to enable package_data to take effect, why?
    python_requires='>=3',
    platforms='any',
    install_requires=requires,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development',
    )
)
