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
from aliyunsdkehpc.endpoint import endpoint_data

class ModifyImageGatewayConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'ModifyImageGatewayConfig')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Repos(self):
		return self.get_query_params().get('Repo')

	def set_Repos(self, Repos):
		for depth1 in range(len(Repos)):
			if Repos[depth1].get('Auth') is not None:
				self.add_query_param('Repo.' + str(depth1 + 1) + '.Auth', Repos[depth1].get('Auth'))
			if Repos[depth1].get('Location') is not None:
				self.add_query_param('Repo.' + str(depth1 + 1) + '.Location', Repos[depth1].get('Location'))
			if Repos[depth1].get('URL') is not None:
				self.add_query_param('Repo.' + str(depth1 + 1) + '.URL', Repos[depth1].get('URL'))

	def get_DBServerInfo(self):
		return self.get_query_params().get('DBServerInfo')

	def set_DBServerInfo(self,DBServerInfo):
		self.add_query_param('DBServerInfo',DBServerInfo)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_DefaultRepoLocation(self):
		return self.get_query_params().get('DefaultRepoLocation')

	def set_DefaultRepoLocation(self,DefaultRepoLocation):
		self.add_query_param('DefaultRepoLocation',DefaultRepoLocation)

	def get_DBPassword(self):
		return self.get_query_params().get('DBPassword')

	def set_DBPassword(self,DBPassword):
		self.add_query_param('DBPassword',DBPassword)

	def get_DBType(self):
		return self.get_query_params().get('DBType')

	def set_DBType(self,DBType):
		self.add_query_param('DBType',DBType)

	def get_DBUsername(self):
		return self.get_query_params().get('DBUsername')

	def set_DBUsername(self,DBUsername):
		self.add_query_param('DBUsername',DBUsername)

	def get_PullUpdateTimeout(self):
		return self.get_query_params().get('PullUpdateTimeout')

	def set_PullUpdateTimeout(self,PullUpdateTimeout):
		self.add_query_param('PullUpdateTimeout',PullUpdateTimeout)

	def get_ImageExpirationTimeout(self):
		return self.get_query_params().get('ImageExpirationTimeout')

	def set_ImageExpirationTimeout(self,ImageExpirationTimeout):
		self.add_query_param('ImageExpirationTimeout',ImageExpirationTimeout)