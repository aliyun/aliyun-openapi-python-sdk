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
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'SetAutoScaleConfig','ehs')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_SpotPriceLimit(self):
		return self.get_query_params().get('SpotPriceLimit')

	def set_SpotPriceLimit(self,SpotPriceLimit):
		self.add_query_param('SpotPriceLimit',SpotPriceLimit)

	def get_ExcludeNodes(self):
		return self.get_query_params().get('ExcludeNodes')

	def set_ExcludeNodes(self,ExcludeNodes):
		self.add_query_param('ExcludeNodes',ExcludeNodes)

	def get_ExtraNodesGrowRatio(self):
		return self.get_query_params().get('ExtraNodesGrowRatio')

	def set_ExtraNodesGrowRatio(self,ExtraNodesGrowRatio):
		self.add_query_param('ExtraNodesGrowRatio',ExtraNodesGrowRatio)

	def get_ShrinkIdleTimes(self):
		return self.get_query_params().get('ShrinkIdleTimes')

	def set_ShrinkIdleTimes(self,ShrinkIdleTimes):
		self.add_query_param('ShrinkIdleTimes',ShrinkIdleTimes)

	def get_GrowTimeoutInMinutes(self):
		return self.get_query_params().get('GrowTimeoutInMinutes')

	def set_GrowTimeoutInMinutes(self,GrowTimeoutInMinutes):
		self.add_query_param('GrowTimeoutInMinutes',GrowTimeoutInMinutes)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_EnableAutoGrow(self):
		return self.get_query_params().get('EnableAutoGrow')

	def set_EnableAutoGrow(self,EnableAutoGrow):
		self.add_query_param('EnableAutoGrow',EnableAutoGrow)

	def get_EnableAutoShrink(self):
		return self.get_query_params().get('EnableAutoShrink')

	def set_EnableAutoShrink(self,EnableAutoShrink):
		self.add_query_param('EnableAutoShrink',EnableAutoShrink)

	def get_SpotStrategy(self):
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self,SpotStrategy):
		self.add_query_param('SpotStrategy',SpotStrategy)

	def get_MaxNodesInCluster(self):
		return self.get_query_params().get('MaxNodesInCluster')

	def set_MaxNodesInCluster(self,MaxNodesInCluster):
		self.add_query_param('MaxNodesInCluster',MaxNodesInCluster)

	def get_ShrinkIntervalInMinutes(self):
		return self.get_query_params().get('ShrinkIntervalInMinutes')

	def set_ShrinkIntervalInMinutes(self,ShrinkIntervalInMinutes):
		self.add_query_param('ShrinkIntervalInMinutes',ShrinkIntervalInMinutes)

	def get_Queuess(self):
		return self.get_query_params().get('Queuess')

	def set_Queuess(self,Queuess):
		for i in range(len(Queuess)):	
			if Queuess[i].get('SpotStrategy') is not None:
				self.add_query_param('Queues.' + str(i + 1) + '.SpotStrategy' , Queuess[i].get('SpotStrategy'))
			if Queuess[i].get('QueueName') is not None:
				self.add_query_param('Queues.' + str(i + 1) + '.QueueName' , Queuess[i].get('QueueName'))
			for j in range(len(Queuess[i].get('InstanceTypess'))):
				if Queuess[i].get('InstanceTypess')[j] is not None:
					if Queuess[i].get('InstanceTypess')[j].get('SpotStrategy') is not None:
						self.add_query_param('Queues.' + str(i + 1) + '.InstanceTypes.'+str(j + 1)+ '.SpotStrategy', Queuess[i].get('InstanceTypess')[j].get('SpotStrategy'))
					if Queuess[i].get('InstanceTypess')[j].get('VSwitchId') is not None:
						self.add_query_param('Queues.' + str(i + 1) + '.InstanceTypes.'+str(j + 1)+ '.VSwitchId', Queuess[i].get('InstanceTypess')[j].get('VSwitchId'))
					if Queuess[i].get('InstanceTypess')[j].get('InstanceType') is not None:
						self.add_query_param('Queues.' + str(i + 1) + '.InstanceTypes.'+str(j + 1)+ '.InstanceType', Queuess[i].get('InstanceTypess')[j].get('InstanceType'))
					if Queuess[i].get('InstanceTypess')[j].get('ZoneId') is not None:
						self.add_query_param('Queues.' + str(i + 1) + '.InstanceTypes.'+str(j + 1)+ '.ZoneId', Queuess[i].get('InstanceTypess')[j].get('ZoneId'))
					if Queuess[i].get('InstanceTypess')[j].get('HostNamePrefix') is not None:
						self.add_query_param('Queues.' + str(i + 1) + '.InstanceTypes.'+str(j + 1)+ '.HostNamePrefix', Queuess[i].get('InstanceTypess')[j].get('HostNamePrefix'))
					if Queuess[i].get('InstanceTypess')[j].get('SpotPriceLimit') is not None:
						self.add_query_param('Queues.' + str(i + 1) + '.InstanceTypes.'+str(j + 1)+ '.SpotPriceLimit', Queuess[i].get('InstanceTypess')[j].get('SpotPriceLimit'))
			if Queuess[i].get('MaxNodesInQueue') is not None:
				self.add_query_param('Queues.' + str(i + 1) + '.MaxNodesInQueue' , Queuess[i].get('MaxNodesInQueue'))
			if Queuess[i].get('InstanceType') is not None:
				self.add_query_param('Queues.' + str(i + 1) + '.InstanceType' , Queuess[i].get('InstanceType'))
			if Queuess[i].get('EnableAutoGrow') is not None:
				self.add_query_param('Queues.' + str(i + 1) + '.EnableAutoGrow' , Queuess[i].get('EnableAutoGrow'))
			if Queuess[i].get('SpotPriceLimit') is not None:
				self.add_query_param('Queues.' + str(i + 1) + '.SpotPriceLimit' , Queuess[i].get('SpotPriceLimit'))
			if Queuess[i].get('EnableAutoShrink') is not None:
				self.add_query_param('Queues.' + str(i + 1) + '.EnableAutoShrink' , Queuess[i].get('EnableAutoShrink'))


	def get_GrowIntervalInMinutes(self):
		return self.get_query_params().get('GrowIntervalInMinutes')

	def set_GrowIntervalInMinutes(self,GrowIntervalInMinutes):
		self.add_query_param('GrowIntervalInMinutes',GrowIntervalInMinutes)

	def get_GrowRatio(self):
		return self.get_query_params().get('GrowRatio')

	def set_GrowRatio(self,GrowRatio):
		self.add_query_param('GrowRatio',GrowRatio)