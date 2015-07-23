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

#coding=utf-8

import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parent_dir)
from ..acs_exception import error_code, error_msg
from ..acs_exception.exceptions import ClientException
from xml.dom.minidom import parse


"""
Region&Endpoint provider module.

Created on 6/12/2015

@author: alex
"""

#endpoint list
__endpoints = dict()

#load endpoints info from endpoints.xml file and parse to dict.
__endpoints_file = os.path.join(parent_dir, 'endpoints.xml')
try:
	DOMTree = parse(__endpoints_file)
	root = DOMTree.documentElement
	eps = root.getElementsByTagName('Endpoint')
	for endpoint in eps:
		region_list = []
		product_list = []
		regions = endpoint.getElementsByTagName('RegionId')
		products = endpoint.getElementsByTagName('Product')
		for region in regions:
			region_list.append(region.childNodes[0].nodeValue)
		for product in products:
			name_node = product.getElementsByTagName('ProductName')[0]
			name = name_node.childNodes[0].nodeValue
			domain_node = product.getElementsByTagName('DomainName')[0]
			domain = domain_node.childNodes[0].nodeValue
			product_list.append({name: domain})

		__endpoints[endpoint.getAttribute('name')] = dict(regions=region_list, products=product_list)

except Exception, ex:
	raise ClientException(error_code.SDK_MISSING_ENDPOINTS_FILER, error_msg.get_msg('SDK_MISSING_ENDPOINTS_FILER'))


def find_product_domain(regionid,prod_name):
	"""
	Fetch endpoint url with given region id, product name and endpoint list
	:param regionid: region id
	:param product: product name
	:param endpoints: product list
	:return: endpoint url
	"""
	if regionid is not None and product is not None:
		for point in __endpoints:
			point_info = __endpoints.get(point)
			if regionid in point_info.get('regions'):
				prod_info = point_info.get('products')
				for prod in prod_info:
					if prod_name in prod:
						return prod.get(prod_name)
	return None

if __name__=='__main__':
	print find_product_domain('cn-hangzhou','Rds')