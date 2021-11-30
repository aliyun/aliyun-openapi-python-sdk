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
		if ModificationProtectionConfig.get('Reason') is not None:
			self.add_query_param('ModificationProtectionConfig.Reason', ModificationProtectionConfig.get('Reason'))
		if ModificationProtectionConfig.get('Status') is not None:
			self.add_query_param('ModificationProtectionConfig.Status', ModificationProtectionConfig.get('Status'))
	def get_LoadBalancerBillingConfig(self): # Struct
		return self.get_query_params().get('LoadBalancerBillingConfig')

	def set_LoadBalancerBillingConfig(self, LoadBalancerBillingConfig):  # Struct
		if LoadBalancerBillingConfig.get('BandwidthPackageId') is not None:
			self.add_query_param('LoadBalancerBillingConfig.BandwidthPackageId', LoadBalancerBillingConfig.get('BandwidthPackageId'))
		if LoadBalancerBillingConfig.get('InternetChargeType') is not None:
			self.add_query_param('LoadBalancerBillingConfig.InternetChargeType', LoadBalancerBillingConfig.get('InternetChargeType'))
		if LoadBalancerBillingConfig.get('InternetBandwidth') is not None:
			self.add_query_param('LoadBalancerBillingConfig.InternetBandwidth', LoadBalancerBillingConfig.get('InternetBandwidth'))
		if LoadBalancerBillingConfig.get('PayType') is not None:
			self.add_query_param('LoadBalancerBillingConfig.PayType', LoadBalancerBillingConfig.get('PayType'))
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
			if value1.get('VSwitchId') is not None:
				self.add_query_param('ZoneMappings.' + str(index1 + 1) + '.VSwitchId', value1.get('VSwitchId'))
			if value1.get('ZoneId') is not None:
				self.add_query_param('ZoneMappings.' + str(index1 + 1) + '.ZoneId', value1.get('ZoneId'))
			if value1.get('AllocationId') is not None:
				self.add_query_param('ZoneMappings.' + str(index1 + 1) + '.AllocationId', value1.get('AllocationId'))
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
