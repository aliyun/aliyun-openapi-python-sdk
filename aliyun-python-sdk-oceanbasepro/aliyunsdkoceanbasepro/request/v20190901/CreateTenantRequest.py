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
from aliyunsdkoceanbasepro.endpoint import endpoint_data
import json

class CreateTenantRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'CreateTenant','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Charset(self): # String
		return self.get_body_params().get('Charset')

	def set_Charset(self, Charset):  # String
		self.add_body_params('Charset', Charset)
	def get_TenantMode(self): # String
		return self.get_body_params().get('TenantMode')

	def set_TenantMode(self, TenantMode):  # String
		self.add_body_params('TenantMode', TenantMode)
	def get_Memory(self): # Integer
		return self.get_body_params().get('Memory')

	def set_Memory(self, Memory):  # Integer
		self.add_body_params('Memory', Memory)
	def get_LogDisk(self): # Long
		return self.get_body_params().get('LogDisk')

	def set_LogDisk(self, LogDisk):  # Long
		self.add_body_params('LogDisk', LogDisk)
	def get_TimeZone(self): # String
		return self.get_body_params().get('TimeZone')

	def set_TimeZone(self, TimeZone):  # String
		self.add_body_params('TimeZone', TimeZone)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_UserVSwitchId(self): # String
		return self.get_body_params().get('UserVSwitchId')

	def set_UserVSwitchId(self, UserVSwitchId):  # String
		self.add_body_params('UserVSwitchId', UserVSwitchId)
	def get_UserVpcId(self): # String
		return self.get_body_params().get('UserVpcId')

	def set_UserVpcId(self, UserVpcId):  # String
		self.add_body_params('UserVpcId', UserVpcId)
	def get_Cpu(self): # Integer
		return self.get_body_params().get('Cpu')

	def set_Cpu(self, Cpu):  # Integer
		self.add_body_params('Cpu', Cpu)
	def get_UnitNum(self): # Integer
		return self.get_body_params().get('UnitNum')

	def set_UnitNum(self, UnitNum):  # Integer
		self.add_body_params('UnitNum', UnitNum)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_PrimaryZone(self): # String
		return self.get_body_params().get('PrimaryZone')

	def set_PrimaryZone(self, PrimaryZone):  # String
		self.add_body_params('PrimaryZone', PrimaryZone)
	def get_UserVpcOwnerId(self): # String
		return self.get_body_params().get('UserVpcOwnerId')

	def set_UserVpcOwnerId(self, UserVpcOwnerId):  # String
		self.add_body_params('UserVpcOwnerId', UserVpcOwnerId)
	def get_CreateParams(self): # Map
		return self.get_body_params().get('CreateParams')

	def set_CreateParams(self, CreateParams):  # Map
		self.add_body_params("CreateParams", json.dumps(CreateParams))
	def get_TenantName(self): # String
		return self.get_body_params().get('TenantName')

	def set_TenantName(self, TenantName):  # String
		self.add_body_params('TenantName', TenantName)
	def get_ReadOnlyZoneList(self): # String
		return self.get_body_params().get('ReadOnlyZoneList')

	def set_ReadOnlyZoneList(self, ReadOnlyZoneList):  # String
		self.add_body_params('ReadOnlyZoneList', ReadOnlyZoneList)
