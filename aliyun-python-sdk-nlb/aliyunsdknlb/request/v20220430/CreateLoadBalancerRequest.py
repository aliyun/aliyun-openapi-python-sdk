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
from aliyunsdknlb.endpoint import endpoint_data

class CreateLoadBalancerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Nlb', '2022-04-30', 'CreateLoadBalancer','nlb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_ModificationProtectionConfig(self): # Struct
		return self.get_body_params().get('ModificationProtectionConfig')

	def set_ModificationProtectionConfig(self, ModificationProtectionConfig):  # Struct
		if ModificationProtectionConfig.get('Status') is not None:
			self.add_body_params('ModificationProtectionConfig.Status', ModificationProtectionConfig.get('Status'))
		if ModificationProtectionConfig.get('Reason') is not None:
			self.add_body_params('ModificationProtectionConfig.Reason', ModificationProtectionConfig.get('Reason'))
	def get_LoadBalancerBillingConfig(self): # Struct
		return self.get_body_params().get('LoadBalancerBillingConfig')

	def set_LoadBalancerBillingConfig(self, LoadBalancerBillingConfig):  # Struct
		if LoadBalancerBillingConfig.get('PayType') is not None:
			self.add_body_params('LoadBalancerBillingConfig.PayType', LoadBalancerBillingConfig.get('PayType'))
	def get_DeletionProtectionConfig(self): # Struct
		return self.get_body_params().get('DeletionProtectionConfig')

	def set_DeletionProtectionConfig(self, DeletionProtectionConfig):  # Struct
		if DeletionProtectionConfig.get('Enabled') is not None:
			self.add_body_params('DeletionProtectionConfig.Enabled', DeletionProtectionConfig.get('Enabled'))
		if DeletionProtectionConfig.get('Reason') is not None:
			self.add_body_params('DeletionProtectionConfig.Reason', DeletionProtectionConfig.get('Reason'))
	def get_AddressIpVersion(self): # String
		return self.get_body_params().get('AddressIpVersion')

	def set_AddressIpVersion(self, AddressIpVersion):  # String
		self.add_body_params('AddressIpVersion', AddressIpVersion)
	def get_ResourceGroupId(self): # String
		return self.get_body_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_body_params('ResourceGroupId', ResourceGroupId)
	def get_LoadBalancerName(self): # String
		return self.get_body_params().get('LoadBalancerName')

	def set_LoadBalancerName(self, LoadBalancerName):  # String
		self.add_body_params('LoadBalancerName', LoadBalancerName)
	def get_AddressType(self): # String
		return self.get_body_params().get('AddressType')

	def set_AddressType(self, AddressType):  # String
		self.add_body_params('AddressType', AddressType)
	def get_BandwidthPackageId(self): # String
		return self.get_body_params().get('BandwidthPackageId')

	def set_BandwidthPackageId(self, BandwidthPackageId):  # String
		self.add_body_params('BandwidthPackageId', BandwidthPackageId)
	def get_DryRun(self): # Boolean
		return self.get_body_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_body_params('DryRun', DryRun)
	def get_ZoneMappings(self): # Array
		return self.get_body_params().get('ZoneMappings')

	def set_ZoneMappings(self, ZoneMappings):  # Array
		for index1, value1 in enumerate(ZoneMappings):
			if value1.get('VSwitchId') is not None:
				self.add_body_params('ZoneMappings.' + str(index1 + 1) + '.VSwitchId', value1.get('VSwitchId'))
			if value1.get('ZoneId') is not None:
				self.add_body_params('ZoneMappings.' + str(index1 + 1) + '.ZoneId', value1.get('ZoneId'))
			if value1.get('PrivateIPv4Address') is not None:
				self.add_body_params('ZoneMappings.' + str(index1 + 1) + '.PrivateIPv4Address', value1.get('PrivateIPv4Address'))
			if value1.get('AllocationId') is not None:
				self.add_body_params('ZoneMappings.' + str(index1 + 1) + '.AllocationId', value1.get('AllocationId'))
	def get_LoadBalancerType(self): # String
		return self.get_body_params().get('LoadBalancerType')

	def set_LoadBalancerType(self, LoadBalancerType):  # String
		self.add_body_params('LoadBalancerType', LoadBalancerType)
	def get_VpcId(self): # String
		return self.get_body_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_body_params('VpcId', VpcId)
