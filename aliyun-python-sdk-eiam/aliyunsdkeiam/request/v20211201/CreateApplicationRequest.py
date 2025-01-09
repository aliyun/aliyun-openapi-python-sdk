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

class CreateApplicationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'CreateApplication','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_ApplicationSourceType(self): # String
		return self.get_query_params().get('ApplicationSourceType')

	def set_ApplicationSourceType(self, ApplicationSourceType):  # String
		self.add_query_param('ApplicationSourceType', ApplicationSourceType)
	def get_LogoUrl(self): # String
		return self.get_query_params().get('LogoUrl')

	def set_LogoUrl(self, LogoUrl):  # String
		self.add_query_param('LogoUrl', LogoUrl)
	def get_ApplicationName(self): # String
		return self.get_query_params().get('ApplicationName')

	def set_ApplicationName(self, ApplicationName):  # String
		self.add_query_param('ApplicationName', ApplicationName)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_SsoType(self): # String
		return self.get_query_params().get('SsoType')

	def set_SsoType(self, SsoType):  # String
		self.add_query_param('SsoType', SsoType)
	def get_ApplicationTemplateId(self): # String
		return self.get_query_params().get('ApplicationTemplateId')

	def set_ApplicationTemplateId(self, ApplicationTemplateId):  # String
		self.add_query_param('ApplicationTemplateId', ApplicationTemplateId)
