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
from aliyunsdkddoscoo.endpoint import endpoint_data

class ModifyWebRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ddoscoo', '2020-01-01', 'ModifyWebRule')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_RsType(self):
		return self.get_query_params().get('RsType')

	def set_RsType(self,RsType):
		self.add_query_param('RsType',RsType)

	def get_RealServerss(self):
		return self.get_query_params().get('RealServers')

	def set_RealServerss(self, RealServerss):
		for depth1 in range(len(RealServerss)):
			if RealServerss[depth1] is not None:
				self.add_query_param('RealServers.' + str(depth1 + 1) , RealServerss[depth1])

	def get_ProxyTypes(self):
		return self.get_query_params().get('ProxyTypes')

	def set_ProxyTypes(self,ProxyTypes):
		self.add_query_param('ProxyTypes',ProxyTypes)

	def get_InstanceIdss(self):
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIdss(self, InstanceIdss):
		for depth1 in range(len(InstanceIdss)):
			if InstanceIdss[depth1] is not None:
				self.add_query_param('InstanceIds.' + str(depth1 + 1) , InstanceIdss[depth1])

	def get_Domain(self):
		return self.get_query_params().get('Domain')

	def set_Domain(self,Domain):
		self.add_query_param('Domain',Domain)