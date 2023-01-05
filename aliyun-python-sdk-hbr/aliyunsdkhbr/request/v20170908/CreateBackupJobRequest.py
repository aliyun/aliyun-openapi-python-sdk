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
from aliyunsdkhbr.endpoint import endpoint_data

class CreateBackupJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateBackupJob')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ContainerClusterId(self): # String
		return self.get_query_params().get('ContainerClusterId')

	def set_ContainerClusterId(self, ContainerClusterId):  # String
		self.add_query_param('ContainerClusterId', ContainerClusterId)
	def get_VaultId(self): # String
		return self.get_query_params().get('VaultId')

	def set_VaultId(self, VaultId):  # String
		self.add_query_param('VaultId', VaultId)
	def get_ContainerResources(self): # String
		return self.get_query_params().get('ContainerResources')

	def set_ContainerResources(self, ContainerResources):  # String
		self.add_query_param('ContainerResources', ContainerResources)
	def get_CrossAccountType(self): # String
		return self.get_query_params().get('CrossAccountType')

	def set_CrossAccountType(self, CrossAccountType):  # String
		self.add_query_param('CrossAccountType', CrossAccountType)
	def get_CrossAccountRoleName(self): # String
		return self.get_query_params().get('CrossAccountRoleName')

	def set_CrossAccountRoleName(self, CrossAccountRoleName):  # String
		self.add_query_param('CrossAccountRoleName', CrossAccountRoleName)
	def get_Options(self): # String
		return self.get_query_params().get('Options')

	def set_Options(self, Options):  # String
		self.add_query_param('Options', Options)
	def get_SourceType(self): # String
		return self.get_query_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_query_param('SourceType', SourceType)
	def get_Exclude(self): # String
		return self.get_query_params().get('Exclude')

	def set_Exclude(self, Exclude):  # String
		self.add_query_param('Exclude', Exclude)
	def get_JobName(self): # String
		return self.get_query_params().get('JobName')

	def set_JobName(self, JobName):  # String
		self.add_query_param('JobName', JobName)
	def get_Retention(self): # Long
		return self.get_query_params().get('Retention')

	def set_Retention(self, Retention):  # Long
		self.add_query_param('Retention', Retention)
	def get_BackupType(self): # String
		return self.get_query_params().get('BackupType')

	def set_BackupType(self, BackupType):  # String
		self.add_query_param('BackupType', BackupType)
	def get_Include(self): # String
		return self.get_query_params().get('Include')

	def set_Include(self, Include):  # String
		self.add_query_param('Include', Include)
	def get_InitiatedByAck(self): # Boolean
		return self.get_query_params().get('InitiatedByAck')

	def set_InitiatedByAck(self, InitiatedByAck):  # Boolean
		self.add_query_param('InitiatedByAck', InitiatedByAck)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_SpeedLimit(self): # String
		return self.get_query_params().get('SpeedLimit')

	def set_SpeedLimit(self, SpeedLimit):  # String
		self.add_query_param('SpeedLimit', SpeedLimit)
	def get_CrossAccountUserId(self): # Long
		return self.get_query_params().get('CrossAccountUserId')

	def set_CrossAccountUserId(self, CrossAccountUserId):  # Long
		self.add_query_param('CrossAccountUserId', CrossAccountUserId)
