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
from aliyunsdkretailcloud.endpoint import endpoint_data

class DeployAppRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'DeployApp')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DeployPacketUrl(self): # String
		return self.get_query_params().get('DeployPacketUrl')

	def set_DeployPacketUrl(self, DeployPacketUrl):  # String
		self.add_query_param('DeployPacketUrl', DeployPacketUrl)
	def get_TotalPartitions(self): # Integer
		return self.get_query_params().get('TotalPartitions')

	def set_TotalPartitions(self, TotalPartitions):  # Integer
		self.add_query_param('TotalPartitions', TotalPartitions)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_EnvId(self): # Long
		return self.get_query_params().get('EnvId')

	def set_EnvId(self, EnvId):  # Long
		self.add_query_param('EnvId', EnvId)
	def get_UpdateStrategyType(self): # String
		return self.get_query_params().get('UpdateStrategyType')

	def set_UpdateStrategyType(self, UpdateStrategyType):  # String
		self.add_query_param('UpdateStrategyType', UpdateStrategyType)
	def get_PauseType(self): # String
		return self.get_query_params().get('PauseType')

	def set_PauseType(self, PauseType):  # String
		self.add_query_param('PauseType', PauseType)
	def get_DeployPacketId(self): # Long
		return self.get_query_params().get('DeployPacketId')

	def set_DeployPacketId(self, DeployPacketId):  # Long
		self.add_query_param('DeployPacketId', DeployPacketId)
	def get_ContainerImageLists(self): # RepeatList
		return self.get_query_params().get('ContainerImageList')

	def set_ContainerImageLists(self, ContainerImageList):  # RepeatList
		for depth1 in range(len(ContainerImageList)):
			self.add_query_param('ContainerImageList.' + str(depth1 + 1), ContainerImageList[depth1])
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_InitContainerImageLists(self): # RepeatList
		return self.get_query_params().get('InitContainerImageList')

	def set_InitContainerImageLists(self, InitContainerImageList):  # RepeatList
		for depth1 in range(len(InitContainerImageList)):
			self.add_query_param('InitContainerImageList.' + str(depth1 + 1), InitContainerImageList[depth1])
	def get_DefaultPacketOfAppGroup(self): # String
		return self.get_query_params().get('DefaultPacketOfAppGroup')

	def set_DefaultPacketOfAppGroup(self, DefaultPacketOfAppGroup):  # String
		self.add_query_param('DefaultPacketOfAppGroup', DefaultPacketOfAppGroup)
	def get_ArmsFlag(self): # Boolean
		return self.get_query_params().get('ArmsFlag')

	def set_ArmsFlag(self, ArmsFlag):  # Boolean
		self.add_query_param('ArmsFlag', ArmsFlag)
