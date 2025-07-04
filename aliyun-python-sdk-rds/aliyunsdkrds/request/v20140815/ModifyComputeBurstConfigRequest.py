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
from aliyunsdkrds.endpoint import endpoint_data

class ModifyComputeBurstConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'ModifyComputeBurstConfig','rds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_CpuShrinkThreshold(self): # String
		return self.get_query_params().get('CpuShrinkThreshold')

	def set_CpuShrinkThreshold(self, CpuShrinkThreshold):  # String
		self.add_query_param('CpuShrinkThreshold', CpuShrinkThreshold)
	def get_BurstStatus(self): # String
		return self.get_query_params().get('BurstStatus')

	def set_BurstStatus(self, BurstStatus):  # String
		self.add_query_param('BurstStatus', BurstStatus)
	def get_SwitchTimeMode(self): # String
		return self.get_query_params().get('SwitchTimeMode')

	def set_SwitchTimeMode(self, SwitchTimeMode):  # String
		self.add_query_param('SwitchTimeMode', SwitchTimeMode)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_SwitchTime(self): # String
		return self.get_query_params().get('SwitchTime')

	def set_SwitchTime(self, SwitchTime):  # String
		self.add_query_param('SwitchTime', SwitchTime)
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_MemoryEnlargeThreshold(self): # String
		return self.get_query_params().get('MemoryEnlargeThreshold')

	def set_MemoryEnlargeThreshold(self, MemoryEnlargeThreshold):  # String
		self.add_query_param('MemoryEnlargeThreshold', MemoryEnlargeThreshold)
	def get_CrontabJobId(self): # String
		return self.get_query_params().get('CrontabJobId')

	def set_CrontabJobId(self, CrontabJobId):  # String
		self.add_query_param('CrontabJobId', CrontabJobId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ScaleMaxMemory(self): # String
		return self.get_query_params().get('ScaleMaxMemory')

	def set_ScaleMaxMemory(self, ScaleMaxMemory):  # String
		self.add_query_param('ScaleMaxMemory', ScaleMaxMemory)
	def get_MemoryShrinkThreshold(self): # String
		return self.get_query_params().get('MemoryShrinkThreshold')

	def set_MemoryShrinkThreshold(self, MemoryShrinkThreshold):  # String
		self.add_query_param('MemoryShrinkThreshold', MemoryShrinkThreshold)
	def get_ScaleMaxCpus(self): # String
		return self.get_query_params().get('ScaleMaxCpus')

	def set_ScaleMaxCpus(self, ScaleMaxCpus):  # String
		self.add_query_param('ScaleMaxCpus', ScaleMaxCpus)
	def get_CpuEnlargeThreshold(self): # String
		return self.get_query_params().get('CpuEnlargeThreshold')

	def set_CpuEnlargeThreshold(self, CpuEnlargeThreshold):  # String
		self.add_query_param('CpuEnlargeThreshold', CpuEnlargeThreshold)
