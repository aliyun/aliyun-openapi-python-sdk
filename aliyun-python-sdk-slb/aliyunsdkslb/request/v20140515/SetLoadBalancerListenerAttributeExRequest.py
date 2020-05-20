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
from aliyunsdkslb.endpoint import endpoint_data

class SetLoadBalancerListenerAttributeExRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Slb', '2014-05-15', 'SetLoadBalancerListenerAttributeEx','slb')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ListenerPort(self):
		return self.get_query_params().get('ListenerPort')

	def set_ListenerPort(self,ListenerPort):
		self.add_query_param('ListenerPort',ListenerPort)

	def get_KvAttributes(self):
		return self.get_query_params().get('KvAttributes')

	def set_KvAttributes(self, KvAttributes):
		for depth1 in range(len(KvAttributes)):
			if KvAttributes[depth1].get('Value') is not None:
				self.add_query_param('KvAttribute.' + str(depth1 + 1) + '.Value', KvAttributes[depth1].get('Value'))
			if KvAttributes[depth1].get('Key') is not None:
				self.add_query_param('KvAttribute.' + str(depth1 + 1) + '.Key', KvAttributes[depth1].get('Key'))

	def get_Protocol(self):
		return self.get_query_params().get('Protocol')

	def set_Protocol(self,Protocol):
		self.add_query_param('Protocol',Protocol)

	def get_LoadBalancerId(self):
		return self.get_query_params().get('LoadBalancerId')

	def set_LoadBalancerId(self,LoadBalancerId):
		self.add_query_param('LoadBalancerId',LoadBalancerId)