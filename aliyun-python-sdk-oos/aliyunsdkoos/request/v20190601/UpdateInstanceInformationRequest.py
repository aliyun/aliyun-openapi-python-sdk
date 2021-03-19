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
from aliyunsdkoos.endpoint import endpoint_data

class UpdateInstanceInformationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'UpdateInstanceInformation')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AgentVersion(self):
		return self.get_query_params().get('AgentVersion')

	def set_AgentVersion(self,AgentVersion):
		self.add_query_param('AgentVersion',AgentVersion)

	def get_IpAddress(self):
		return self.get_query_params().get('IpAddress')

	def set_IpAddress(self,IpAddress):
		self.add_query_param('IpAddress',IpAddress)

	def get_ComputerName(self):
		return self.get_query_params().get('ComputerName')

	def set_ComputerName(self,ComputerName):
		self.add_query_param('ComputerName',ComputerName)

	def get_PlatformName(self):
		return self.get_query_params().get('PlatformName')

	def set_PlatformName(self,PlatformName):
		self.add_query_param('PlatformName',PlatformName)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_AgentName(self):
		return self.get_query_params().get('AgentName')

	def set_AgentName(self,AgentName):
		self.add_query_param('AgentName',AgentName)

	def get_PlatformType(self):
		return self.get_query_params().get('PlatformType')

	def set_PlatformType(self,PlatformType):
		self.add_query_param('PlatformType',PlatformType)

	def get_PlatformVersion(self):
		return self.get_query_params().get('PlatformVersion')

	def set_PlatformVersion(self,PlatformVersion):
		self.add_query_param('PlatformVersion',PlatformVersion)