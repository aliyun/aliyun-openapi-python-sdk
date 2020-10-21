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

class CreateBackupPlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateBackupPlan','hbr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientId(self):
		return self.get_body_params().get('ClientId')

	def set_ClientId(self,ClientId):
		self.add_body_params('ClientId', ClientId)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_Prefix(self):
		return self.get_query_params().get('Prefix')

	def set_Prefix(self,Prefix):
		self.add_query_param('Prefix',Prefix)

	def get_Paths(self):
		return self.get_body_params().get('Path')

	def set_Paths(self, Paths):
		for depth1 in range(len(Paths)):
			if Paths[depth1] is not None:
				self.add_body_params('Path.' + str(depth1 + 1) , Paths[depth1])

	def get_PlanName(self):
		return self.get_query_params().get('PlanName')

	def set_PlanName(self,PlanName):
		self.add_query_param('PlanName',PlanName)

	def get_Options(self):
		return self.get_body_params().get('Options')

	def set_Options(self,Options):
		self.add_body_params('Options', Options)

	def get_SourceType(self):
		return self.get_query_params().get('SourceType')

	def set_SourceType(self,SourceType):
		self.add_query_param('SourceType',SourceType)

	def get_Exclude(self):
		return self.get_body_params().get('Exclude')

	def set_Exclude(self,Exclude):
		self.add_body_params('Exclude', Exclude)

	def get_BackupType(self):
		return self.get_query_params().get('BackupType')

	def set_BackupType(self,BackupType):
		self.add_query_param('BackupType',BackupType)

	def get_Retention(self):
		return self.get_query_params().get('Retention')

	def set_Retention(self,Retention):
		self.add_query_param('Retention',Retention)

	def get_FileSystemId(self):
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self,FileSystemId):
		self.add_query_param('FileSystemId',FileSystemId)

	def get_Include(self):
		return self.get_body_params().get('Include')

	def set_Include(self,Include):
		self.add_body_params('Include', Include)

	def get_CreateTime(self):
		return self.get_query_params().get('CreateTime')

	def set_CreateTime(self,CreateTime):
		self.add_query_param('CreateTime',CreateTime)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_Bucket(self):
		return self.get_query_params().get('Bucket')

	def set_Bucket(self,Bucket):
		self.add_query_param('Bucket',Bucket)

	def get_Schedule(self):
		return self.get_query_params().get('Schedule')

	def set_Schedule(self,Schedule):
		self.add_query_param('Schedule',Schedule)

	def get_InstanceId(self):
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_body_params('InstanceId', InstanceId)

	def get_SpeedLimit(self):
		return self.get_body_params().get('SpeedLimit')

	def set_SpeedLimit(self,SpeedLimit):
		self.add_body_params('SpeedLimit', SpeedLimit)

	def get_Detail(self):
		return self.get_query_params().get('Detail')

	def set_Detail(self,Detail):
		self.add_query_param('Detail',Detail)

	def get_BackupSourceGroupId(self):
		return self.get_query_params().get('BackupSourceGroupId')

	def set_BackupSourceGroupId(self,BackupSourceGroupId):
		self.add_query_param('BackupSourceGroupId',BackupSourceGroupId)

	def get_UdmRegionId(self):
		return self.get_query_params().get('UdmRegionId')

	def set_UdmRegionId(self,UdmRegionId):
		self.add_query_param('UdmRegionId',UdmRegionId)