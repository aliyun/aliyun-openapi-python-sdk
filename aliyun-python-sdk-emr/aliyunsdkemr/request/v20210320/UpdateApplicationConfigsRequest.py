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
from aliyunsdkemr.endpoint import endpoint_data

class UpdateApplicationConfigsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2021-03-20', 'UpdateApplicationConfigs','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Configs(self):
		return self.get_query_params().get('Configs')

	def set_Configs(self,Configs):
		self.add_query_param('Configs',Configs)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_RefreshNodeConfig(self):
		return self.get_query_params().get('RefreshNodeConfig')

	def set_RefreshNodeConfig(self,RefreshNodeConfig):
		self.add_query_param('RefreshNodeConfig',RefreshNodeConfig)

	def get_ApplicationConfigs(self):
		return self.get_query_params().get('ApplicationConfigs')

	def set_ApplicationConfigs(self,ApplicationConfigs):
		self.add_query_param('ApplicationConfigs',ApplicationConfigs)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_RefreshConfig(self):
		return self.get_query_params().get('RefreshConfig')

	def set_RefreshConfig(self,RefreshConfig):
		self.add_query_param('RefreshConfig',RefreshConfig)

	def get_ApplicationName(self):
		return self.get_query_params().get('ApplicationName')

	def set_ApplicationName(self,ApplicationName):
		self.add_query_param('ApplicationName',ApplicationName)