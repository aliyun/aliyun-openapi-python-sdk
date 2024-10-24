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
from aliyunsdkdypnsapi.endpoint import endpoint_data

class GetAuthTokenRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dypnsapi', '2017-05-25', 'GetAuthToken','dypnsapi')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_Origin(self): # String
		return self.get_query_params().get('Origin')

	def set_Origin(self, Origin):  # String
		self.add_query_param('Origin', Origin)
	def get_SceneCode(self): # String
		return self.get_query_params().get('SceneCode')

	def set_SceneCode(self, SceneCode):  # String
		self.add_query_param('SceneCode', SceneCode)
	def get_CuApiCode(self): # Integer
		return self.get_query_params().get('CuApiCode')

	def set_CuApiCode(self, CuApiCode):  # Integer
		self.add_query_param('CuApiCode', CuApiCode)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_CtApiCode(self): # Integer
		return self.get_query_params().get('CtApiCode')

	def set_CtApiCode(self, CtApiCode):  # Integer
		self.add_query_param('CtApiCode', CtApiCode)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Version(self): # String
		return self.get_query_params().get('Version')

	def set_Version(self, Version):  # String
		self.add_query_param('Version', Version)
	def get_Url(self): # String
		return self.get_query_params().get('Url')

	def set_Url(self, Url):  # String
		self.add_query_param('Url', Url)
	def get_BizType(self): # Integer
		return self.get_query_params().get('BizType')

	def set_BizType(self, BizType):  # Integer
		self.add_query_param('BizType', BizType)
	def get_CmApiCode(self): # Integer
		return self.get_query_params().get('CmApiCode')

	def set_CmApiCode(self, CmApiCode):  # Integer
		self.add_query_param('CmApiCode', CmApiCode)
