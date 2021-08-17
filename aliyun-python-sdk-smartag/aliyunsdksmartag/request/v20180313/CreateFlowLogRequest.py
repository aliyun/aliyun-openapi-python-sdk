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
from aliyunsdksmartag.endpoint import endpoint_data

class CreateFlowLogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'CreateFlowLog','smartag')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_NetflowVersion(self): # String
		return self.get_query_params().get('NetflowVersion')

	def set_NetflowVersion(self, NetflowVersion):  # String
		self.add_query_param('NetflowVersion', NetflowVersion)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_InactiveAging(self): # Integer
		return self.get_query_params().get('InactiveAging')

	def set_InactiveAging(self, InactiveAging):  # Integer
		self.add_query_param('InactiveAging', InactiveAging)
	def get_SlsRegionId(self): # String
		return self.get_query_params().get('SlsRegionId')

	def set_SlsRegionId(self, SlsRegionId):  # String
		self.add_query_param('SlsRegionId', SlsRegionId)
	def get_ActiveAging(self): # Integer
		return self.get_query_params().get('ActiveAging')

	def set_ActiveAging(self, ActiveAging):  # Integer
		self.add_query_param('ActiveAging', ActiveAging)
	def get_OutputType(self): # String
		return self.get_query_params().get('OutputType')

	def set_OutputType(self, OutputType):  # String
		self.add_query_param('OutputType', OutputType)
	def get_ProjectName(self): # String
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_query_param('ProjectName', ProjectName)
	def get_LogstoreName(self): # String
		return self.get_query_params().get('LogstoreName')

	def set_LogstoreName(self, LogstoreName):  # String
		self.add_query_param('LogstoreName', LogstoreName)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_NetflowServerPort(self): # Integer
		return self.get_query_params().get('NetflowServerPort')

	def set_NetflowServerPort(self, NetflowServerPort):  # Integer
		self.add_query_param('NetflowServerPort', NetflowServerPort)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_NetflowServerIp(self): # String
		return self.get_query_params().get('NetflowServerIp')

	def set_NetflowServerIp(self, NetflowServerIp):  # String
		self.add_query_param('NetflowServerIp', NetflowServerIp)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
