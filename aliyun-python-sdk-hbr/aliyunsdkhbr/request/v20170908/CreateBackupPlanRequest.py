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
import json

class CreateBackupPlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateBackupPlan')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_VaultId(self): # String
		return self.get_query_params().get('VaultId')

	def set_VaultId(self, VaultId):  # String
		self.add_query_param('VaultId', VaultId)
	def get_Prefix(self): # String
		return self.get_query_params().get('Prefix')

	def set_Prefix(self, Prefix):  # String
		self.add_query_param('Prefix', Prefix)
	def get_CrossAccountType(self): # String
		return self.get_query_params().get('CrossAccountType')

	def set_CrossAccountType(self, CrossAccountType):  # String
		self.add_query_param('CrossAccountType', CrossAccountType)
	def get_Rules(self): # RepeatList
		return self.get_body_params().get('Rule')

	def set_Rules(self, Rule):  # RepeatList
		for depth1 in range(len(Rule)):
			if Rule[depth1].get('Schedule') is not None:
				self.add_body_params('Rule.' + str(depth1 + 1) + '.Schedule', Rule[depth1].get('Schedule'))
			if Rule[depth1].get('DestinationRegionId') is not None:
				self.add_body_params('Rule.' + str(depth1 + 1) + '.DestinationRegionId', Rule[depth1].get('DestinationRegionId'))
			if Rule[depth1].get('Disabled') is not None:
				self.add_body_params('Rule.' + str(depth1 + 1) + '.Disabled', Rule[depth1].get('Disabled'))
			if Rule[depth1].get('RuleName') is not None:
				self.add_body_params('Rule.' + str(depth1 + 1) + '.RuleName', Rule[depth1].get('RuleName'))
			if Rule[depth1].get('DestinationRetention') is not None:
				self.add_body_params('Rule.' + str(depth1 + 1) + '.DestinationRetention', Rule[depth1].get('DestinationRetention'))
			if Rule[depth1].get('Retention') is not None:
				self.add_body_params('Rule.' + str(depth1 + 1) + '.Retention', Rule[depth1].get('Retention'))
			if Rule[depth1].get('BackupType') is not None:
				self.add_body_params('Rule.' + str(depth1 + 1) + '.BackupType', Rule[depth1].get('BackupType'))
			if Rule[depth1].get('DoCopy') is not None:
				self.add_body_params('Rule.' + str(depth1 + 1) + '.DoCopy', Rule[depth1].get('DoCopy'))
	def get_CrossAccountRoleName(self): # String
		return self.get_query_params().get('CrossAccountRoleName')

	def set_CrossAccountRoleName(self, CrossAccountRoleName):  # String
		self.add_query_param('CrossAccountRoleName', CrossAccountRoleName)
	def get_Paths(self): # RepeatList
		return self.get_body_params().get('Path')

	def set_Paths(self, Path):  # RepeatList
		for depth1 in range(len(Path)):
			self.add_body_params('Path.' + str(depth1 + 1), Path[depth1])
	def get_PlanName(self): # String
		return self.get_query_params().get('PlanName')

	def set_PlanName(self, PlanName):  # String
		self.add_query_param('PlanName', PlanName)
	def get_Options(self): # String
		return self.get_body_params().get('Options')

	def set_Options(self, Options):  # String
		self.add_body_params('Options', Options)
	def get_SourceType(self): # String
		return self.get_query_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_query_param('SourceType', SourceType)
	def get_Exclude(self): # String
		return self.get_body_params().get('Exclude')

	def set_Exclude(self, Exclude):  # String
		self.add_body_params('Exclude', Exclude)
	def get_BackupType(self): # String
		return self.get_query_params().get('BackupType')

	def set_BackupType(self, BackupType):  # String
		self.add_query_param('BackupType', BackupType)
	def get_Retention(self): # Long
		return self.get_query_params().get('Retention')

	def set_Retention(self, Retention):  # Long
		self.add_query_param('Retention', Retention)
	def get_FileSystemId(self): # String
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self, FileSystemId):  # String
		self.add_query_param('FileSystemId', FileSystemId)
	def get_Include(self): # String
		return self.get_body_params().get('Include')

	def set_Include(self, Include):  # String
		self.add_body_params('Include', Include)
	def get_CreateTime(self): # Long
		return self.get_query_params().get('CreateTime')

	def set_CreateTime(self, CreateTime):  # Long
		self.add_query_param('CreateTime', CreateTime)
	def get_KeepLatestSnapshots(self): # Long
		return self.get_query_params().get('KeepLatestSnapshots')

	def set_KeepLatestSnapshots(self, KeepLatestSnapshots):  # Long
		self.add_query_param('KeepLatestSnapshots', KeepLatestSnapshots)
	def get_Bucket(self): # String
		return self.get_query_params().get('Bucket')

	def set_Bucket(self, Bucket):  # String
		self.add_query_param('Bucket', Bucket)
	def get_Schedule(self): # String
		return self.get_query_params().get('Schedule')

	def set_Schedule(self, Schedule):  # String
		self.add_query_param('Schedule', Schedule)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_InstanceName(self): # String
		return self.get_body_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_body_params('InstanceName', InstanceName)
	def get_OtsDetail(self): # Struct
		return self.get_body_params().get('OtsDetail')

	def set_OtsDetail(self, OtsDetail):  # Struct
		self.add_body_params("OtsDetail", json.dumps(OtsDetail))
	def get_SpeedLimit(self): # String
		return self.get_body_params().get('SpeedLimit')

	def set_SpeedLimit(self, SpeedLimit):  # String
		self.add_body_params('SpeedLimit', SpeedLimit)
	def get_Detail(self): # String
		return self.get_query_params().get('Detail')

	def set_Detail(self, Detail):  # String
		self.add_query_param('Detail', Detail)
	def get_CrossAccountUserId(self): # Long
		return self.get_query_params().get('CrossAccountUserId')

	def set_CrossAccountUserId(self, CrossAccountUserId):  # Long
		self.add_query_param('CrossAccountUserId', CrossAccountUserId)
	def get_UdmRegionId(self): # String
		return self.get_query_params().get('UdmRegionId')

	def set_UdmRegionId(self, UdmRegionId):  # String
		self.add_query_param('UdmRegionId', UdmRegionId)
