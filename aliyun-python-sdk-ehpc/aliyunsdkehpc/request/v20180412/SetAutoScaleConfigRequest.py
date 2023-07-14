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

class SetAutoScaleConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'SetAutoScaleConfig')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_DnsConfig(self): # String
		return self.get_query_params().get('DnsConfig')

	def set_DnsConfig(self, DnsConfig):  # String
		self.add_query_param('DnsConfig', DnsConfig)
	def get_SpotPriceLimit(self): # Float
		return self.get_query_params().get('SpotPriceLimit')

	def set_SpotPriceLimit(self, SpotPriceLimit):  # Float
		self.add_query_param('SpotPriceLimit', SpotPriceLimit)
	def get_ExcludeNodes(self): # String
		return self.get_query_params().get('ExcludeNodes')

	def set_ExcludeNodes(self, ExcludeNodes):  # String
		self.add_query_param('ExcludeNodes', ExcludeNodes)
	def get_ExtraNodesGrowRatio(self): # Integer
		return self.get_query_params().get('ExtraNodesGrowRatio')

	def set_ExtraNodesGrowRatio(self, ExtraNodesGrowRatio):  # Integer
		self.add_query_param('ExtraNodesGrowRatio', ExtraNodesGrowRatio)
	def get_ShrinkIdleTimes(self): # Integer
		return self.get_query_params().get('ShrinkIdleTimes')

	def set_ShrinkIdleTimes(self, ShrinkIdleTimes):  # Integer
		self.add_query_param('ShrinkIdleTimes', ShrinkIdleTimes)
	def get_GrowTimeoutInMinutes(self): # Integer
		return self.get_query_params().get('GrowTimeoutInMinutes')

	def set_GrowTimeoutInMinutes(self, GrowTimeoutInMinutes):  # Integer
		self.add_query_param('GrowTimeoutInMinutes', GrowTimeoutInMinutes)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_EnableAutoGrow(self): # Boolean
		return self.get_query_params().get('EnableAutoGrow')

	def set_EnableAutoGrow(self, EnableAutoGrow):  # Boolean
		self.add_query_param('EnableAutoGrow', EnableAutoGrow)
	def get_EnableAutoShrink(self): # Boolean
		return self.get_query_params().get('EnableAutoShrink')

	def set_EnableAutoShrink(self, EnableAutoShrink):  # Boolean
		self.add_query_param('EnableAutoShrink', EnableAutoShrink)
	def get_SpotStrategy(self): # String
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self, SpotStrategy):  # String
		self.add_query_param('SpotStrategy', SpotStrategy)
	def get_MaxNodesInCluster(self): # Integer
		return self.get_query_params().get('MaxNodesInCluster')

	def set_MaxNodesInCluster(self, MaxNodesInCluster):  # Integer
		self.add_query_param('MaxNodesInCluster', MaxNodesInCluster)
	def get_ComputeEnableHt(self): # Boolean
		return self.get_query_params().get('ComputeEnableHt')

	def set_ComputeEnableHt(self, ComputeEnableHt):  # Boolean
		self.add_query_param('ComputeEnableHt', ComputeEnableHt)
	def get_ShrinkIntervalInMinutes(self): # Integer
		return self.get_query_params().get('ShrinkIntervalInMinutes')

	def set_ShrinkIntervalInMinutes(self, ShrinkIntervalInMinutes):  # Integer
		self.add_query_param('ShrinkIntervalInMinutes', ShrinkIntervalInMinutes)
	def get_Queuess(self): # RepeatList
		return self.get_query_params().get('Queues')

	def set_Queuess(self, Queues):  # RepeatList
		for depth1 in range(len(Queues)):
			if Queues[depth1].get('QueueName') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.QueueName', Queues[depth1].get('QueueName'))
			if Queues[depth1].get('SystemDiskLevel') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.SystemDiskLevel', Queues[depth1].get('SystemDiskLevel'))
			if Queues[depth1].get('SortedByInventory') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.SortedByInventory', Queues[depth1].get('SortedByInventory'))
			if Queues[depth1].get('InstanceTypes') is not None:
				for depth2 in range(len(Queues[depth1].get('InstanceTypes'))):
					if Queues[depth1].get('InstanceTypes')[depth2].get('VSwitchId') is not None:
						self.add_query_param('Queues.' + str(depth1 + 1) + '.InstanceTypes.'  + str(depth2 + 1) + '.VSwitchId', Queues[depth1].get('InstanceTypes')[depth2].get('VSwitchId'))
					if Queues[depth1].get('InstanceTypes')[depth2].get('SpotStrategy') is not None:
						self.add_query_param('Queues.' + str(depth1 + 1) + '.InstanceTypes.'  + str(depth2 + 1) + '.SpotStrategy', Queues[depth1].get('InstanceTypes')[depth2].get('SpotStrategy'))
					if Queues[depth1].get('InstanceTypes')[depth2].get('SpotInterruptionBehavior') is not None:
						self.add_query_param('Queues.' + str(depth1 + 1) + '.InstanceTypes.'  + str(depth2 + 1) + '.SpotInterruptionBehavior', Queues[depth1].get('InstanceTypes')[depth2].get('SpotInterruptionBehavior'))
					if Queues[depth1].get('InstanceTypes')[depth2].get('ZoneId') is not None:
						self.add_query_param('Queues.' + str(depth1 + 1) + '.InstanceTypes.'  + str(depth2 + 1) + '.ZoneId', Queues[depth1].get('InstanceTypes')[depth2].get('ZoneId'))
					if Queues[depth1].get('InstanceTypes')[depth2].get('InstanceType') is not None:
						self.add_query_param('Queues.' + str(depth1 + 1) + '.InstanceTypes.'  + str(depth2 + 1) + '.InstanceType', Queues[depth1].get('InstanceTypes')[depth2].get('InstanceType'))
					if Queues[depth1].get('InstanceTypes')[depth2].get('SpotPriceLimit') is not None:
						self.add_query_param('Queues.' + str(depth1 + 1) + '.InstanceTypes.'  + str(depth2 + 1) + '.SpotPriceLimit', Queues[depth1].get('InstanceTypes')[depth2].get('SpotPriceLimit'))
					if Queues[depth1].get('InstanceTypes')[depth2].get('SpotDuration') is not None:
						self.add_query_param('Queues.' + str(depth1 + 1) + '.InstanceTypes.'  + str(depth2 + 1) + '.SpotDuration', Queues[depth1].get('InstanceTypes')[depth2].get('SpotDuration'))
			if Queues[depth1].get('EnableAutoGrow') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.EnableAutoGrow', Queues[depth1].get('EnableAutoGrow'))
			if Queues[depth1].get('HostNameSuffix') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.HostNameSuffix', Queues[depth1].get('HostNameSuffix'))
			if Queues[depth1].get('SpotPriceLimit') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.SpotPriceLimit', Queues[depth1].get('SpotPriceLimit'))
			if Queues[depth1].get('EnableAutoShrink') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.EnableAutoShrink', Queues[depth1].get('EnableAutoShrink'))
			if Queues[depth1].get('SpotStrategy') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.SpotStrategy', Queues[depth1].get('SpotStrategy'))
			if Queues[depth1].get('DataDisks') is not None:
				for depth2 in range(len(Queues[depth1].get('DataDisks'))):
					if Queues[depth1].get('DataDisks')[depth2].get('DataDiskDeleteWithInstance') is not None:
						self.add_query_param('Queues.' + str(depth1 + 1) + '.DataDisks.'  + str(depth2 + 1) + '.DataDiskDeleteWithInstance', Queues[depth1].get('DataDisks')[depth2].get('DataDiskDeleteWithInstance'))
					if Queues[depth1].get('DataDisks')[depth2].get('DataDiskEncrypted') is not None:
						self.add_query_param('Queues.' + str(depth1 + 1) + '.DataDisks.'  + str(depth2 + 1) + '.DataDiskEncrypted', Queues[depth1].get('DataDisks')[depth2].get('DataDiskEncrypted'))
					if Queues[depth1].get('DataDisks')[depth2].get('DataDiskKMSKeyId') is not None:
						self.add_query_param('Queues.' + str(depth1 + 1) + '.DataDisks.'  + str(depth2 + 1) + '.DataDiskKMSKeyId', Queues[depth1].get('DataDisks')[depth2].get('DataDiskKMSKeyId'))
					if Queues[depth1].get('DataDisks')[depth2].get('DataDiskSize') is not None:
						self.add_query_param('Queues.' + str(depth1 + 1) + '.DataDisks.'  + str(depth2 + 1) + '.DataDiskSize', Queues[depth1].get('DataDisks')[depth2].get('DataDiskSize'))
					if Queues[depth1].get('DataDisks')[depth2].get('DataDiskCategory') is not None:
						self.add_query_param('Queues.' + str(depth1 + 1) + '.DataDisks.'  + str(depth2 + 1) + '.DataDiskCategory', Queues[depth1].get('DataDisks')[depth2].get('DataDiskCategory'))
					if Queues[depth1].get('DataDisks')[depth2].get('DataDiskPerformanceLevel') is not None:
						self.add_query_param('Queues.' + str(depth1 + 1) + '.DataDisks.'  + str(depth2 + 1) + '.DataDiskPerformanceLevel', Queues[depth1].get('DataDisks')[depth2].get('DataDiskPerformanceLevel'))
			if Queues[depth1].get('MinNodesInQueue') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.MinNodesInQueue', Queues[depth1].get('MinNodesInQueue'))
			if Queues[depth1].get('MaxNodesPerCycle') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.MaxNodesPerCycle', Queues[depth1].get('MaxNodesPerCycle'))
			if Queues[depth1].get('SystemDiskCategory') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.SystemDiskCategory', Queues[depth1].get('SystemDiskCategory'))
			if Queues[depth1].get('MaxNodesInQueue') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.MaxNodesInQueue', Queues[depth1].get('MaxNodesInQueue'))
			if Queues[depth1].get('SystemDiskSize') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.SystemDiskSize', Queues[depth1].get('SystemDiskSize'))
			if Queues[depth1].get('QueueImageId') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.QueueImageId', Queues[depth1].get('QueueImageId'))
			if Queues[depth1].get('InstanceType') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.InstanceType', Queues[depth1].get('InstanceType'))
			if Queues[depth1].get('HostNamePrefix') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.HostNamePrefix', Queues[depth1].get('HostNamePrefix'))
			if Queues[depth1].get('MinNodesPerCycle') is not None:
				self.add_query_param('Queues.' + str(depth1 + 1) + '.MinNodesPerCycle', Queues[depth1].get('MinNodesPerCycle'))
	def get_GrowIntervalInMinutes(self): # Integer
		return self.get_query_params().get('GrowIntervalInMinutes')

	def set_GrowIntervalInMinutes(self, GrowIntervalInMinutes):  # Integer
		self.add_query_param('GrowIntervalInMinutes', GrowIntervalInMinutes)
	def get_GrowRatio(self): # Integer
		return self.get_query_params().get('GrowRatio')

	def set_GrowRatio(self, GrowRatio):  # Integer
		self.add_query_param('GrowRatio', GrowRatio)
