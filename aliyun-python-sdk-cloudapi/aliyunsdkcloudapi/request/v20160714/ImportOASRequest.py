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

class ImportOASRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'ImportOAS','apigateway')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Data(self): # String
		return self.get_body_params().get('Data')

	def set_Data(self, Data):  # String
		self.add_body_params('Data', Data)
	def get_AuthType(self): # String
		return self.get_query_params().get('AuthType')

	def set_AuthType(self, AuthType):  # String
		self.add_query_param('AuthType', AuthType)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_Overwrite(self): # Boolean
		return self.get_query_params().get('Overwrite')

	def set_Overwrite(self, Overwrite):  # Boolean
		self.add_query_param('Overwrite', Overwrite)
	def get_IgnoreWarning(self): # Boolean
		return self.get_query_params().get('IgnoreWarning')

	def set_IgnoreWarning(self, IgnoreWarning):  # Boolean
		self.add_query_param('IgnoreWarning', IgnoreWarning)
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_RequestMode(self): # String
		return self.get_query_params().get('RequestMode')

	def set_RequestMode(self, RequestMode):  # String
		self.add_query_param('RequestMode', RequestMode)
	def get_BackendName(self): # String
		return self.get_query_params().get('BackendName')

	def set_BackendName(self, BackendName):  # String
		self.add_query_param('BackendName', BackendName)
	def get_SkipDryRun(self): # Boolean
		return self.get_query_params().get('SkipDryRun')

	def set_SkipDryRun(self, SkipDryRun):  # Boolean
		self.add_query_param('SkipDryRun', SkipDryRun)
	def get_OASVersion(self): # String
		return self.get_query_params().get('OASVersion')

	def set_OASVersion(self, OASVersion):  # String
		self.add_query_param('OASVersion', OASVersion)
