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
from aliyunsdkmaxcompute.endpoint import endpoint_data

class ListProjectsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'MaxCompute', '2022-01-04', 'ListProjects')
		self.set_uri_pattern('/api/v1/projects')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_saleTags(self): # String
		return self.get_query_params().get('saleTags')

	def set_saleTags(self, saleTags):  # String
		self.add_query_param('saleTags', saleTags)
	def get_prefix(self): # String
		return self.get_query_params().get('prefix')

	def set_prefix(self, prefix):  # String
		self.add_query_param('prefix', prefix)
	def get_marker(self): # String
		return self.get_query_params().get('marker')

	def set_marker(self, marker):  # String
		self.add_query_param('marker', marker)
	def get_tenantId(self): # String
		return self.get_query_params().get('tenantId')

	def set_tenantId(self, tenantId):  # String
		self.add_query_param('tenantId', tenantId)
	def get_region(self): # String
		return self.get_query_params().get('region')

	def set_region(self, region):  # String
		self.add_query_param('region', region)
	def get_type(self): # String
		return self.get_query_params().get('type')

	def set_type(self, type):  # String
		self.add_query_param('type', type)
	def get_quotaNickName(self): # String
		return self.get_query_params().get('quotaNickName')

	def set_quotaNickName(self, quotaNickName):  # String
		self.add_query_param('quotaNickName', quotaNickName)
	def get_quotaName(self): # String
		return self.get_query_params().get('quotaName')

	def set_quotaName(self, quotaName):  # String
		self.add_query_param('quotaName', quotaName)
	def get_maxItem(self): # Integer
		return self.get_query_params().get('maxItem')

	def set_maxItem(self, maxItem):  # Integer
		self.add_query_param('maxItem', maxItem)
