# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8

import os

from aliyunsdkcore.acs_exception import error_code, error_msg
from aliyunsdkcore.acs_exception.exceptions import ClientException
from xml.dom.minidom import parse
from ..profile import location_service

"""
Region&Endpoint provider module.

Created on 6/12/2015

@author: alex

modified by wenyang@2018-03-14:
    reconstruction the smelly codes and keep compatibility

"""


user_config_endpoints = dict()


def add_endpoint(product_name, region_id, end_point):
    modify_point(product_name, region_id, end_point)


def modify_point(product_name, region_id, end_point):
    if product_name not in user_config_endpoints:
        user_config_endpoints[product_name] = dict()
    product_data = user_config_endpoints[product_name]
    product_data[region_id] = end_point
