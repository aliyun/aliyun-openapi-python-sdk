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

class DescribeElasticStrengthRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'DescribeElasticStrength','ess')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_DataDiskCategoriess(self): # RepeatList
		return self.get_query_params().get('DataDiskCategories')

	def set_DataDiskCategoriess(self, DataDiskCategories):  # RepeatList
		for depth1 in range(len(DataDiskCategories)):
			self.add_query_param('DataDiskCategories.' + str(depth1 + 1), DataDiskCategories[depth1])
	def get_ScalingGroupId(self): # String
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self, ScalingGroupId):  # String
		self.add_query_param('ScalingGroupId', ScalingGroupId)
	def get_VSwitchIdss(self): # RepeatList
		return self.get_query_params().get('VSwitchIds')

	def set_VSwitchIdss(self, VSwitchIds):  # RepeatList
		for depth1 in range(len(VSwitchIds)):
			self.add_query_param('VSwitchIds.' + str(depth1 + 1), VSwitchIds[depth1])
	def get_InstanceTypess(self): # RepeatList
		return self.get_query_params().get('InstanceTypes')

	def set_InstanceTypess(self, InstanceTypes):  # RepeatList
		for depth1 in range(len(InstanceTypes)):
			self.add_query_param('InstanceTypes.' + str(depth1 + 1), InstanceTypes[depth1])
	def get_ImageName(self): # String
		return self.get_query_params().get('ImageName')

	def set_ImageName(self, ImageName):  # String
		self.add_query_param('ImageName', ImageName)
	def get_ScalingGroupIdss(self): # RepeatList
		return self.get_query_params().get('ScalingGroupIds')

	def set_ScalingGroupIdss(self, ScalingGroupIds):  # RepeatList
		for depth1 in range(len(ScalingGroupIds)):
			self.add_query_param('ScalingGroupIds.' + str(depth1 + 1), ScalingGroupIds[depth1])
	def get_Ipv6AddressCount(self): # Integer
		return self.get_query_params().get('Ipv6AddressCount')

	def set_Ipv6AddressCount(self, Ipv6AddressCount):  # Integer
		self.add_query_param('Ipv6AddressCount', Ipv6AddressCount)
	def get_SystemDiskCategoriess(self): # RepeatList
		return self.get_query_params().get('SystemDiskCategories')

	def set_SystemDiskCategoriess(self, SystemDiskCategories):  # RepeatList
		for depth1 in range(len(SystemDiskCategories)):
			self.add_query_param('SystemDiskCategories.' + str(depth1 + 1), SystemDiskCategories[depth1])
	def get_SpotStrategy(self): # String
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self, SpotStrategy):  # String
		self.add_query_param('SpotStrategy', SpotStrategy)
	def get_PriorityStrategy(self): # String
		return self.get_query_params().get('PriorityStrategy')

	def set_PriorityStrategy(self, PriorityStrategy):  # String
		self.add_query_param('PriorityStrategy', PriorityStrategy)
	def get_ImageFamily(self): # String
		return self.get_query_params().get('ImageFamily')

	def set_ImageFamily(self, ImageFamily):  # String
		self.add_query_param('ImageFamily', ImageFamily)
