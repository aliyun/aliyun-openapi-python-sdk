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

class ModifyTenantResourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'ModifyTenantResource','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Memory(self): # Integer
		return self.get_body_params().get('Memory')

	def set_Memory(self, Memory):  # Integer
		self.add_body_params('Memory', Memory)
	def get_LogDisk(self): # Long
		return self.get_body_params().get('LogDisk')

	def set_LogDisk(self, LogDisk):  # Long
		self.add_body_params('LogDisk', LogDisk)
	def get_Cpu(self): # Integer
		return self.get_body_params().get('Cpu')

	def set_Cpu(self, Cpu):  # Integer
		self.add_body_params('Cpu', Cpu)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_TenantId(self): # String
		return self.get_body_params().get('TenantId')

	def set_TenantId(self, TenantId):  # String
		self.add_body_params('TenantId', TenantId)
	def get_Iops(self): # String
		return self.get_body_params().get('Iops')

	def set_Iops(self, Iops):  # String
		self.add_body_params('Iops', Iops)
	def get_ReadOnlyZoneList(self): # String
		return self.get_body_params().get('ReadOnlyZoneList')

	def set_ReadOnlyZoneList(self, ReadOnlyZoneList):  # String
		self.add_body_params('ReadOnlyZoneList', ReadOnlyZoneList)
