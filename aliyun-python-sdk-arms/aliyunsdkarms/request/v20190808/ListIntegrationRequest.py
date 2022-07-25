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

from aliyunsdkcore.request import RpcRequest
from aliyunsdkarms.endpoint import endpoint_data

class ListIntegrationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'ListIntegration','arms')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Size(self): # Long
		return self.get_query_params().get('Size')

	def set_Size(self, Size):  # Long
		self.add_query_param('Size', Size)
	def get_IntegrationName(self): # String
		return self.get_query_params().get('IntegrationName')

	def set_IntegrationName(self, IntegrationName):  # String
		self.add_query_param('IntegrationName', IntegrationName)
	def get_IsDetail(self): # Boolean
		return self.get_query_params().get('IsDetail')

	def set_IsDetail(self, IsDetail):  # Boolean
		self.add_query_param('IsDetail', IsDetail)
	def get_Page(self): # Long
		return self.get_query_params().get('Page')

	def set_Page(self, Page):  # Long
		self.add_query_param('Page', Page)
	def get_IntegrationProductType(self): # String
		return self.get_query_params().get('IntegrationProductType')

	def set_IntegrationProductType(self, IntegrationProductType):  # String
		self.add_query_param('IntegrationProductType', IntegrationProductType)
