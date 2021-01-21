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
from aliyunsdkros.endpoint import endpoint_data

class SetTemplatePermissionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ROS', '2019-09-10', 'SetTemplatePermission','ros')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TemplateVersion(self):
		return self.get_query_params().get('TemplateVersion')

	def set_TemplateVersion(self,TemplateVersion):
		self.add_query_param('TemplateVersion',TemplateVersion)

	def get_TemplateId(self):
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self,TemplateId):
		self.add_query_param('TemplateId',TemplateId)

	def get_VersionOption(self):
		return self.get_query_params().get('VersionOption')

	def set_VersionOption(self,VersionOption):
		self.add_query_param('VersionOption',VersionOption)

	def get_ShareOption(self):
		return self.get_query_params().get('ShareOption')

	def set_ShareOption(self,ShareOption):
		self.add_query_param('ShareOption',ShareOption)

	def get_AccountIds(self):
		return self.get_query_params().get('AccountIds')

	def set_AccountIds(self, AccountIdss):
		for depth1 in range(len(AccountIdss)):
			if AccountIdss[depth1] is not None:
				self.add_query_param('AccountIds.' + str(depth1 + 1) , AccountIdss[depth1])