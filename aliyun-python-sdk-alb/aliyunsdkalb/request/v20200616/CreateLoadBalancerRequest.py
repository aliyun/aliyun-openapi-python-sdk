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
from aliyunsdkalb.endpoint import endpoint_data

class CreateLoadBalancerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'CreateLoadBalancer','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_LoadBalancerEdition(self): # String
		return self.get_query_params().get('LoadBalancerEdition')

	def set_LoadBalancerEdition(self, LoadBalancerEdition):  # String
		self.add_query_param('LoadBalancerEdition', LoadBalancerEdition)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ModificationProtectionConfig(self): # Struct
		return self.get_query_params().get('ModificationProtectionConfig')

	def set_ModificationProtectionConfig(self, ModificationProtectionConfig):  # Struct
		for key1, value1 in ModificationProtectionConfig.items():
			self.add_query_param('ModificationProtectionConfig.' + key1 + '.Reason', value1)
			self.add_query_param('ModificationProtectionConfig.' + key1 + '.Status', value1)
	def get_LoadBalancerBillingConfig(self): # Struct
		return self.get_query_params().get('LoadBalancerBillingConfig')

	def set_LoadBalancerBillingConfig(self, LoadBalancerBillingConfig):  # Struct
		for key1, value1 in LoadBalancerBillingConfig.items():
			self.add_query_param('LoadBalancerBillingConfig.' + key1 + '.PayType', value1)
	def get_DeletionProtectionEnabled(self): # Boolean
		return self.get_query_params().get('DeletionProtectionEnabled')

	def set_DeletionProtectionEnabled(self, DeletionProtectionEnabled):  # Boolean
		self.add_query_param('DeletionProtectionEnabled', DeletionProtectionEnabled)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_LoadBalancerName(self): # String
		return self.get_query_params().get('LoadBalancerName')

	def set_LoadBalancerName(self, LoadBalancerName):  # String
		self.add_query_param('LoadBalancerName', LoadBalancerName)
	def get_AddressType(self): # String
		return self.get_query_params().get('AddressType')

	def set_AddressType(self, AddressType):  # String
		self.add_query_param('AddressType', AddressType)
	def get_AddressAllocatedMode(self): # String
		return self.get_query_params().get('AddressAllocatedMode')

	def set_AddressAllocatedMode(self, AddressAllocatedMode):  # String
		self.add_query_param('AddressAllocatedMode', AddressAllocatedMode)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_ZoneMappings(self): # Array
		return self.get_query_params().get('ZoneMappings')

	def set_ZoneMappings(self, ZoneMappings):  # Array
		for index1, value1 in enumerate(ZoneMappings):
			for key2, value2 in value1.items():
				self.add_query_param('ZoneMappings.' + str(index1 + 1) + '.' + key2 + '.VSwitchId', value2)
				self.add_query_param('ZoneMappings.' + str(index1 + 1) + '.' + key2 + '.ZoneId', value2)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
