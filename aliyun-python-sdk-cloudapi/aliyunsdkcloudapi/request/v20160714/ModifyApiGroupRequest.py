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
from aliyunsdkcloudapi.endpoint import endpoint_data

class ModifyApiGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'ModifyApiGroup','apigateway')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DefaultDomain(self): # String
		return self.get_query_params().get('DefaultDomain')

	def set_DefaultDomain(self, DefaultDomain):  # String
		self.add_query_param('DefaultDomain', DefaultDomain)
	def get_BasePath(self): # String
		return self.get_query_params().get('BasePath')

	def set_BasePath(self, BasePath):  # String
		self.add_query_param('BasePath', BasePath)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_RpcPattern(self): # String
		return self.get_query_params().get('RpcPattern')

	def set_RpcPattern(self, RpcPattern):  # String
		self.add_query_param('RpcPattern', RpcPattern)
	def get_UserLogConfig(self): # String
		return self.get_query_params().get('UserLogConfig')

	def set_UserLogConfig(self, UserLogConfig):  # String
		self.add_query_param('UserLogConfig', UserLogConfig)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_CustomerConfigs(self): # String
		return self.get_query_params().get('CustomerConfigs')

	def set_CustomerConfigs(self, CustomerConfigs):  # String
		self.add_query_param('CustomerConfigs', CustomerConfigs)
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_GroupName(self): # String
		return self.get_query_params().get('GroupName')

	def set_GroupName(self, GroupName):  # String
		self.add_query_param('GroupName', GroupName)
	def get_PassthroughHeaders(self): # String
		return self.get_query_params().get('PassthroughHeaders')

	def set_PassthroughHeaders(self, PassthroughHeaders):  # String
		self.add_query_param('PassthroughHeaders', PassthroughHeaders)
	def get_CompatibleFlags(self): # String
		return self.get_query_params().get('CompatibleFlags')

	def set_CompatibleFlags(self, CompatibleFlags):  # String
		self.add_query_param('CompatibleFlags', CompatibleFlags)
	def get_CustomTraceConfig(self): # String
		return self.get_query_params().get('CustomTraceConfig')

	def set_CustomTraceConfig(self, CustomTraceConfig):  # String
		self.add_query_param('CustomTraceConfig', CustomTraceConfig)
