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

	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_Memory(self): # Integer
		return self.get_query_params().get('Memory')

	def set_Memory(self, Memory):  # Integer
		self.add_query_param('Memory', Memory)
	def get_SystemDiskLevel(self): # String
		return self.get_query_params().get('SystemDiskLevel')

	def set_SystemDiskLevel(self, SystemDiskLevel):  # String
		self.add_query_param('SystemDiskLevel', SystemDiskLevel)
	def get_AllocatePublicAddress(self): # Boolean
		return self.get_query_params().get('AllocatePublicAddress')

	def set_AllocatePublicAddress(self, AllocatePublicAddress):  # Boolean
		self.add_query_param('AllocatePublicAddress', AllocatePublicAddress)
	def get_InternetMaxBandWidthOut(self): # Integer
		return self.get_query_params().get('InternetMaxBandWidthOut')

	def set_InternetMaxBandWidthOut(self, InternetMaxBandWidthOut):  # Integer
		self.add_query_param('InternetMaxBandWidthOut', InternetMaxBandWidthOut)
	def get_ResourceAmountType(self): # String
		return self.get_query_params().get('ResourceAmountType')

	def set_ResourceAmountType(self, ResourceAmountType):  # String
		self.add_query_param('ResourceAmountType', ResourceAmountType)
	def get_StrictResourceProvision(self): # Boolean
		return self.get_query_params().get('StrictResourceProvision')

	def set_StrictResourceProvision(self, StrictResourceProvision):  # Boolean
		self.add_query_param('StrictResourceProvision', StrictResourceProvision)
	def get_JobQueue(self): # String
		return self.get_query_params().get('JobQueue')

	def set_JobQueue(self, JobQueue):  # String
		self.add_query_param('JobQueue', JobQueue)
	def get_SystemDiskType(self): # String
		return self.get_query_params().get('SystemDiskType')

	def set_SystemDiskType(self, SystemDiskType):  # String
		self.add_query_param('SystemDiskType', SystemDiskType)
	def get_Cores(self): # Integer
		return self.get_query_params().get('Cores')

	def set_Cores(self, Cores):  # Integer
		self.add_query_param('Cores', Cores)
	def get_SystemDiskSize(self): # Integer
		return self.get_query_params().get('SystemDiskSize')

	def set_SystemDiskSize(self, SystemDiskSize):  # Integer
		self.add_query_param('SystemDiskSize', SystemDiskSize)
	def get_ZoneInfoss(self): # RepeatList
		return self.get_query_params().get('ZoneInfos')

	def set_ZoneInfoss(self, ZoneInfos):  # RepeatList
		for depth1 in range(len(ZoneInfos)):
			if ZoneInfos[depth1].get('VSwitchId') is not None:
				self.add_query_param('ZoneInfos.' + str(depth1 + 1) + '.VSwitchId', ZoneInfos[depth1].get('VSwitchId'))
			if ZoneInfos[depth1].get('ZoneId') is not None:
				self.add_query_param('ZoneInfos.' + str(depth1 + 1) + '.ZoneId', ZoneInfos[depth1].get('ZoneId'))
	def get_HostNamePrefix(self): # String
		return self.get_query_params().get('HostNamePrefix')

	def set_HostNamePrefix(self, HostNamePrefix):  # String
		self.add_query_param('HostNamePrefix', HostNamePrefix)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_ComputeSpotPriceLimit(self): # Float
		return self.get_query_params().get('ComputeSpotPriceLimit')

	def set_ComputeSpotPriceLimit(self, ComputeSpotPriceLimit):  # Float
		self.add_query_param('ComputeSpotPriceLimit', ComputeSpotPriceLimit)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_ComputeSpotStrategy(self): # String
		return self.get_query_params().get('ComputeSpotStrategy')

	def set_ComputeSpotStrategy(self, ComputeSpotStrategy):  # String
		self.add_query_param('ComputeSpotStrategy', ComputeSpotStrategy)
	def get_HostNameSuffix(self): # String
		return self.get_query_params().get('HostNameSuffix')

	def set_HostNameSuffix(self, HostNameSuffix):  # String
		self.add_query_param('HostNameSuffix', HostNameSuffix)
	def get_PriorityStrategy(self): # String
		return self.get_query_params().get('PriorityStrategy')

	def set_PriorityStrategy(self, PriorityStrategy):  # String
		self.add_query_param('PriorityStrategy', PriorityStrategy)
	def get_InstanceFamilyLevel(self): # String
		return self.get_query_params().get('InstanceFamilyLevel')

	def set_InstanceFamilyLevel(self, InstanceFamilyLevel):  # String
		self.add_query_param('InstanceFamilyLevel', InstanceFamilyLevel)
	def get_Round(self): # Integer
		return self.get_query_params().get('Round')

	def set_Round(self, Round):  # Integer
		self.add_query_param('Round', Round)
	def get_InternetChargeType(self): # String
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self, InternetChargeType):  # String
		self.add_query_param('InternetChargeType', InternetChargeType)
	def get_Interval(self): # Integer
		return self.get_query_params().get('Interval')

	def set_Interval(self, Interval):  # Integer
		self.add_query_param('Interval', Interval)
	def get_InstanceTypeModels(self): # RepeatList
		return self.get_query_params().get('InstanceTypeModel')

	def set_InstanceTypeModels(self, InstanceTypeModel):  # RepeatList
		for depth1 in range(len(InstanceTypeModel)):
			if InstanceTypeModel[depth1].get('MaxPrice') is not None:
				self.add_query_param('InstanceTypeModel.' + str(depth1 + 1) + '.MaxPrice', InstanceTypeModel[depth1].get('MaxPrice'))
			if InstanceTypeModel[depth1].get('TargetImageId') is not None:
				self.add_query_param('InstanceTypeModel.' + str(depth1 + 1) + '.TargetImageId', InstanceTypeModel[depth1].get('TargetImageId'))
			if InstanceTypeModel[depth1].get('InstanceType') is not None:
				self.add_query_param('InstanceTypeModel.' + str(depth1 + 1) + '.InstanceType', InstanceTypeModel[depth1].get('InstanceType'))
	def get_InternetMaxBandWidthIn(self): # Integer
		return self.get_query_params().get('InternetMaxBandWidthIn')

	def set_InternetMaxBandWidthIn(self, InternetMaxBandWidthIn):  # Integer
		self.add_query_param('InternetMaxBandWidthIn', InternetMaxBandWidthIn)
	def get_TargetCapacity(self): # Integer
		return self.get_query_params().get('TargetCapacity')

	def set_TargetCapacity(self, TargetCapacity):  # Integer
		self.add_query_param('TargetCapacity', TargetCapacity)
	def get_StrictSatisfiedTargetCapacity(self): # Boolean
		return self.get_query_params().get('StrictSatisfiedTargetCapacity')

	def set_StrictSatisfiedTargetCapacity(self, StrictSatisfiedTargetCapacity):  # Boolean
		self.add_query_param('StrictSatisfiedTargetCapacity', StrictSatisfiedTargetCapacity)
