# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class SaveApPortalConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'SaveApPortalConfig','cloudwf')

	def get_AuthKey(self):
		return self.get_query_params().get('AuthKey')

	def set_AuthKey(self,AuthKey):
		self.add_query_param('AuthKey',AuthKey)

	def get_PortalUrl(self):
		return self.get_query_params().get('PortalUrl')

	def set_PortalUrl(self,PortalUrl):
		self.add_query_param('PortalUrl',PortalUrl)

	def get_PortalStatus(self):
		return self.get_query_params().get('PortalStatus')

	def set_PortalStatus(self,PortalStatus):
		self.add_query_param('PortalStatus',PortalStatus)

	def get_Whitelist(self):
		return self.get_query_params().get('Whitelist')

	def set_Whitelist(self,Whitelist):
		self.add_query_param('Whitelist',Whitelist)

	def get_CheckUrl(self):
		return self.get_query_params().get('CheckUrl')

	def set_CheckUrl(self,CheckUrl):
		self.add_query_param('CheckUrl',CheckUrl)

	def get_ApConfigId(self):
		return self.get_query_params().get('ApConfigId')

	def set_ApConfigId(self,ApConfigId):
		self.add_query_param('ApConfigId',ApConfigId)

	def get_AuthSecret(self):
		return self.get_query_params().get('AuthSecret')

	def set_AuthSecret(self,AuthSecret):
		self.add_query_param('AuthSecret',AuthSecret)

	def get_WebAuthUrl(self):
		return self.get_query_params().get('WebAuthUrl')

	def set_WebAuthUrl(self,WebAuthUrl):
		self.add_query_param('WebAuthUrl',WebAuthUrl)

	def get_Network(self):
		return self.get_query_params().get('Network')

	def set_Network(self,Network):
		self.add_query_param('Network',Network)