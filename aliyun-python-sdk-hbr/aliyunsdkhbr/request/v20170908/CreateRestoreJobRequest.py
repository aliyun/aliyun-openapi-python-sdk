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

class CreateRestoreJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateRestoreJob')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TargetPrefix(self): # String
		return self.get_query_params().get('TargetPrefix')

	def set_TargetPrefix(self, TargetPrefix):  # String
		self.add_query_param('TargetPrefix', TargetPrefix)
	def get_SnapshotId(self): # String
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self, SnapshotId):  # String
		self.add_query_param('SnapshotId', SnapshotId)
	def get_TargetCreateTime(self): # Long
		return self.get_query_params().get('TargetCreateTime')

	def set_TargetCreateTime(self, TargetCreateTime):  # Long
		self.add_query_param('TargetCreateTime', TargetCreateTime)
	def get_VaultId(self): # String
		return self.get_query_params().get('VaultId')

	def set_VaultId(self, VaultId):  # String
		self.add_query_param('VaultId', VaultId)
	def get_CrossAccountType(self): # String
		return self.get_query_params().get('CrossAccountType')

	def set_CrossAccountType(self, CrossAccountType):  # String
		self.add_query_param('CrossAccountType', CrossAccountType)
	def get_CrossAccountRoleName(self): # String
		return self.get_query_params().get('CrossAccountRoleName')

	def set_CrossAccountRoleName(self, CrossAccountRoleName):  # String
		self.add_query_param('CrossAccountRoleName', CrossAccountRoleName)
	def get_SnapshotHash(self): # String
		return self.get_query_params().get('SnapshotHash')

	def set_SnapshotHash(self, SnapshotHash):  # String
		self.add_query_param('SnapshotHash', SnapshotHash)
	def get_TargetTime(self): # Long
		return self.get_query_params().get('TargetTime')

	def set_TargetTime(self, TargetTime):  # Long
		self.add_query_param('TargetTime', TargetTime)
	def get_TargetInstanceName(self): # String
		return self.get_query_params().get('TargetInstanceName')

	def set_TargetInstanceName(self, TargetInstanceName):  # String
		self.add_query_param('TargetInstanceName', TargetInstanceName)
	def get_SourceType(self): # String
		return self.get_query_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_query_param('SourceType', SourceType)
	def get_Exclude(self): # String
		return self.get_body_params().get('Exclude')

	def set_Exclude(self, Exclude):  # String
		self.add_body_params('Exclude', Exclude)
	def get_TargetContainer(self): # String
		return self.get_query_params().get('TargetContainer')

	def set_TargetContainer(self, TargetContainer):  # String
		self.add_query_param('TargetContainer', TargetContainer)
	def get_TargetBucket(self): # String
		return self.get_query_params().get('TargetBucket')

	def set_TargetBucket(self, TargetBucket):  # String
		self.add_query_param('TargetBucket', TargetBucket)
	def get_TargetContainerClusterId(self): # String
		return self.get_query_params().get('TargetContainerClusterId')

	def set_TargetContainerClusterId(self, TargetContainerClusterId):  # String
		self.add_query_param('TargetContainerClusterId', TargetContainerClusterId)
	def get_Include(self): # String
		return self.get_body_params().get('Include')

	def set_Include(self, Include):  # String
		self.add_body_params('Include', Include)
	def get_UdmDetail(self): # String
		return self.get_query_params().get('UdmDetail')

	def set_UdmDetail(self, UdmDetail):  # String
		self.add_query_param('UdmDetail', UdmDetail)
	def get_TargetTableName(self): # String
		return self.get_query_params().get('TargetTableName')

	def set_TargetTableName(self, TargetTableName):  # String
		self.add_query_param('TargetTableName', TargetTableName)
	def get_InitiatedByAck(self): # Boolean
		return self.get_query_params().get('InitiatedByAck')

	def set_InitiatedByAck(self, InitiatedByAck):  # Boolean
		self.add_query_param('InitiatedByAck', InitiatedByAck)
	def get_RestoreType(self): # String
		return self.get_query_params().get('RestoreType')

	def set_RestoreType(self, RestoreType):  # String
		self.add_query_param('RestoreType', RestoreType)
	def get_TargetInstanceId(self): # String
		return self.get_body_params().get('TargetInstanceId')

	def set_TargetInstanceId(self, TargetInstanceId):  # String
		self.add_body_params('TargetInstanceId', TargetInstanceId)
	def get_OtsDetail(self): # Struct
		return self.get_body_params().get('OtsDetail')

	def set_OtsDetail(self, OtsDetail):  # Struct
		self.add_body_params("OtsDetail", json.dumps(OtsDetail))
	def get_TargetFileSystemId(self): # String
		return self.get_query_params().get('TargetFileSystemId')

	def set_TargetFileSystemId(self, TargetFileSystemId):  # String
		self.add_query_param('TargetFileSystemId', TargetFileSystemId)
	def get_TargetPath(self): # String
		return self.get_body_params().get('TargetPath')

	def set_TargetPath(self, TargetPath):  # String
		self.add_body_params('TargetPath', TargetPath)
	def get_CrossAccountUserId(self): # Long
		return self.get_query_params().get('CrossAccountUserId')

	def set_CrossAccountUserId(self, CrossAccountUserId):  # Long
		self.add_query_param('CrossAccountUserId', CrossAccountUserId)
	def get_UdmRegionId(self): # String
		return self.get_query_params().get('UdmRegionId')

	def set_UdmRegionId(self, UdmRegionId):  # String
		self.add_query_param('UdmRegionId', UdmRegionId)
