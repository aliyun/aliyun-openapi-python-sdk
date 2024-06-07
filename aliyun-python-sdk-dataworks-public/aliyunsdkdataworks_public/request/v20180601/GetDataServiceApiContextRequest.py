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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class GetDataServiceApiContextRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2018-06-01', 'GetDataServiceApiContext')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ApiStatus(self): # Integer
		return self.get_query_params().get('ApiStatus')

	def set_ApiStatus(self, ApiStatus):  # Integer
		self.add_query_param('ApiStatus', ApiStatus)
	def get_CacheKey(self): # String
		return self.get_query_params().get('CacheKey')

	def set_CacheKey(self, CacheKey):  # String
		self.add_query_param('CacheKey', CacheKey)
	def get_ApiId(self): # Long
		return self.get_query_params().get('ApiId')

	def set_ApiId(self, ApiId):  # Long
		self.add_query_param('ApiId', ApiId)
	def get_Verbose(self): # Boolean
		return self.get_query_params().get('Verbose')

	def set_Verbose(self, Verbose):  # Boolean
		self.add_query_param('Verbose', Verbose)
	def get_ForPrivateResGroup(self): # Boolean
		return self.get_query_params().get('ForPrivateResGroup')

	def set_ForPrivateResGroup(self, ForPrivateResGroup):  # Boolean
		self.add_query_param('ForPrivateResGroup', ForPrivateResGroup)
