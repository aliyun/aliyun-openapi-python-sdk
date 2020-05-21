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

class ApplyNodesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'ApplyNodes')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_Memory(self):
		return self.get_query_params().get('Memory')

	def set_Memory(self,Memory):
		self.add_query_param('Memory',Memory)

	def get_AllocatePublicAddress(self):
		return self.get_query_params().get('AllocatePublicAddress')

	def set_AllocatePublicAddress(self,AllocatePublicAddress):
		self.add_query_param('AllocatePublicAddress',AllocatePublicAddress)

	def get_InternetMaxBandWidthOut(self):
		return self.get_query_params().get('InternetMaxBandWidthOut')

	def set_InternetMaxBandWidthOut(self,InternetMaxBandWidthOut):
		self.add_query_param('InternetMaxBandWidthOut',InternetMaxBandWidthOut)

	def get_ResourceAmountType(self):
		return self.get_query_params().get('ResourceAmountType')

	def set_ResourceAmountType(self,ResourceAmountType):
		self.add_query_param('ResourceAmountType',ResourceAmountType)

	def get_SystemDiskType(self):
		return self.get_query_params().get('SystemDiskType')

	def set_SystemDiskType(self,SystemDiskType):
		self.add_query_param('SystemDiskType',SystemDiskType)

	def get_Cores(self):
		return self.get_query_params().get('Cores')

	def set_Cores(self,Cores):
		self.add_query_param('Cores',Cores)

	def get_SystemDiskSize(self):
		return self.get_query_params().get('SystemDiskSize')

	def set_SystemDiskSize(self,SystemDiskSize):
		self.add_query_param('SystemDiskSize',SystemDiskSize)

	def get_ZoneInfoss(self):
		return self.get_query_params().get('ZoneInfoss')

	def set_ZoneInfoss(self, ZoneInfoss):
		for depth1 in range(len(ZoneInfoss)):
			if ZoneInfoss[depth1].get('VSwitchId') is not None:
				self.add_query_param('ZoneInfos.' + str(depth1 + 1) + '.VSwitchId', ZoneInfoss[depth1].get('VSwitchId'))
			if ZoneInfoss[depth1].get('ZoneId') is not None:
				self.add_query_param('ZoneInfos.' + str(depth1 + 1) + '.ZoneId', ZoneInfoss[depth1].get('ZoneId'))

	def get_HostNamePrefix(self):
		return self.get_query_params().get('HostNamePrefix')

	def set_HostNamePrefix(self,HostNamePrefix):
		self.add_query_param('HostNamePrefix',HostNamePrefix)

	def get_ComputeSpotPriceLimit(self):
		return self.get_query_params().get('ComputeSpotPriceLimit')

	def set_ComputeSpotPriceLimit(self,ComputeSpotPriceLimit):
		self.add_query_param('ComputeSpotPriceLimit',ComputeSpotPriceLimit)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_ComputeSpotStrategy(self):
		return self.get_query_params().get('ComputeSpotStrategy')

	def set_ComputeSpotStrategy(self,ComputeSpotStrategy):
		self.add_query_param('ComputeSpotStrategy',ComputeSpotStrategy)

	def get_HostNameSuffix(self):
		return self.get_query_params().get('HostNameSuffix')

	def set_HostNameSuffix(self,HostNameSuffix):
		self.add_query_param('HostNameSuffix',HostNameSuffix)

	def get_PriorityStrategy(self):
		return self.get_query_params().get('PriorityStrategy')

	def set_PriorityStrategy(self,PriorityStrategy):
		self.add_query_param('PriorityStrategy',PriorityStrategy)

	def get_InstanceFamilyLevel(self):
		return self.get_query_params().get('InstanceFamilyLevel')

	def set_InstanceFamilyLevel(self,InstanceFamilyLevel):
		self.add_query_param('InstanceFamilyLevel',InstanceFamilyLevel)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_InstanceTypeModels(self):
		return self.get_query_params().get('InstanceTypeModels')

	def set_InstanceTypeModels(self, InstanceTypeModels):
		for depth1 in range(len(InstanceTypeModels)):
			if InstanceTypeModels[depth1].get('MaxPrice') is not None:
				self.add_query_param('InstanceTypeModel.' + str(depth1 + 1) + '.MaxPrice', InstanceTypeModels[depth1].get('MaxPrice'))
			if InstanceTypeModels[depth1].get('InstanceType') is not None:
				self.add_query_param('InstanceTypeModel.' + str(depth1 + 1) + '.InstanceType', InstanceTypeModels[depth1].get('InstanceType'))

	def get_InternetMaxBandWidthIn(self):
		return self.get_query_params().get('InternetMaxBandWidthIn')

	def set_InternetMaxBandWidthIn(self,InternetMaxBandWidthIn):
		self.add_query_param('InternetMaxBandWidthIn',InternetMaxBandWidthIn)

	def get_TargetCapacity(self):
		return self.get_query_params().get('TargetCapacity')

	def set_TargetCapacity(self,TargetCapacity):
		self.add_query_param('TargetCapacity',TargetCapacity)

	def get_StrictSatisfiedTargetCapacity(self):
		return self.get_query_params().get('StrictSatisfiedTargetCapacity')

	def set_StrictSatisfiedTargetCapacity(self,StrictSatisfiedTargetCapacity):
		self.add_query_param('StrictSatisfiedTargetCapacity',StrictSatisfiedTargetCapacity)