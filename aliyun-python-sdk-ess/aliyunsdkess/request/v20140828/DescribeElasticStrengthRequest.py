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

	def get_ScalingGroupId(self): # String
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self, ScalingGroupId):  # String
		self.add_query_param('ScalingGroupId', ScalingGroupId)
	def get_InstanceTypess(self): # RepeatList
		return self.get_query_params().get('InstanceTypes')

	def set_InstanceTypess(self, InstanceTypes):  # RepeatList
		for depth1 in range(len(InstanceTypes)):
			self.add_query_param('InstanceTypes.' + str(depth1 + 1), InstanceTypes[depth1])
	def get_ScalingGroupIdss(self): # RepeatList
		return self.get_query_params().get('ScalingGroupIds')

	def set_ScalingGroupIdss(self, ScalingGroupIds):  # RepeatList
		for depth1 in range(len(ScalingGroupIds)):
			self.add_query_param('ScalingGroupIds.' + str(depth1 + 1), ScalingGroupIds[depth1])
	def get_SystemDiskCategoriess(self): # RepeatList
		return self.get_query_params().get('SystemDiskCategories')

	def set_SystemDiskCategoriess(self, SystemDiskCategories):  # RepeatList
		for depth1 in range(len(SystemDiskCategories)):
			self.add_query_param('SystemDiskCategories.' + str(depth1 + 1), SystemDiskCategories[depth1])
	def get_PriorityStrategy(self): # String
		return self.get_query_params().get('PriorityStrategy')

	def set_PriorityStrategy(self, PriorityStrategy):  # String
		self.add_query_param('PriorityStrategy', PriorityStrategy)
