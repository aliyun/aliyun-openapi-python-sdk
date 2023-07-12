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
from aliyunsdkess.endpoint import endpoint_data

class AttachLoadBalancersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'AttachLoadBalancers','ess')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ScalingGroupId(self): # String
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self, ScalingGroupId):  # String
		self.add_query_param('ScalingGroupId', ScalingGroupId)
	def get_ForceAttach(self): # Boolean
		return self.get_query_params().get('ForceAttach')

	def set_ForceAttach(self, ForceAttach):  # Boolean
		self.add_query_param('ForceAttach', ForceAttach)
	def get_LoadBalancerConfigs(self): # RepeatList
		return self.get_query_params().get('LoadBalancerConfig')

	def set_LoadBalancerConfigs(self, LoadBalancerConfig):  # RepeatList
		for depth1 in range(len(LoadBalancerConfig)):
			if LoadBalancerConfig[depth1].get('LoadBalancerId') is not None:
				self.add_query_param('LoadBalancerConfig.' + str(depth1 + 1) + '.LoadBalancerId', LoadBalancerConfig[depth1].get('LoadBalancerId'))
			if LoadBalancerConfig[depth1].get('Weight') is not None:
				self.add_query_param('LoadBalancerConfig.' + str(depth1 + 1) + '.Weight', LoadBalancerConfig[depth1].get('Weight'))
	def get_LoadBalancers(self): # RepeatList
		return self.get_query_params().get('LoadBalancer')

	def set_LoadBalancers(self, LoadBalancer):  # RepeatList
		for depth1 in range(len(LoadBalancer)):
			self.add_query_param('LoadBalancer.' + str(depth1 + 1), LoadBalancer[depth1])
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Async(self): # Boolean
		return self.get_query_params().get('Async')

	def set_Async(self, _Async):  # Boolean
		self.add_query_param('Async', _Async)
