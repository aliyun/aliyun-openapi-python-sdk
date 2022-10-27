# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest
from aliyunsdkelasticsearch.endpoint import endpoint_data

class ListInstanceRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'elasticsearch', '2017-06-13', 'ListInstance','elasticsearch')
		self.set_uri_pattern('/openapi/instances')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_description(self): # string
		return self.get_query_params().get('description')

	def set_description(self, description):  # string
		self.add_query_param('description', description)
	def get_instanceCategory(self): # string
		return self.get_query_params().get('instanceCategory')

	def set_instanceCategory(self, instanceCategory):  # string
		self.add_query_param('instanceCategory', instanceCategory)
	def get_tags(self): # string
		return self.get_query_params().get('tags')

	def set_tags(self, tags):  # string
		self.add_query_param('tags', tags)
	def get_resourceGroupId(self): # string
		return self.get_query_params().get('resourceGroupId')

	def set_resourceGroupId(self, resourceGroupId):  # string
		self.add_query_param('resourceGroupId', resourceGroupId)
	def get_instanceId(self): # string
		return self.get_query_params().get('instanceId')

	def set_instanceId(self, instanceId):  # string
		self.add_query_param('instanceId', instanceId)
	def get_size(self): # integer
		return self.get_query_params().get('size')

	def set_size(self, size):  # integer
		self.add_query_param('size', size)
	def get_esVersion(self): # string
		return self.get_query_params().get('esVersion')

	def set_esVersion(self, esVersion):  # string
		self.add_query_param('esVersion', esVersion)
	def get_vpcId(self): # string
		return self.get_query_params().get('vpcId')

	def set_vpcId(self, vpcId):  # string
		self.add_query_param('vpcId', vpcId)
	def get_zoneId(self): # string
		return self.get_query_params().get('zoneId')

	def set_zoneId(self, zoneId):  # string
		self.add_query_param('zoneId', zoneId)
	def get_page(self): # integer
		return self.get_query_params().get('page')

	def set_page(self, page):  # integer
		self.add_query_param('page', page)
	def get_paymentType(self): # string
		return self.get_query_params().get('paymentType')

	def set_paymentType(self, paymentType):  # string
		self.add_query_param('paymentType', paymentType)
