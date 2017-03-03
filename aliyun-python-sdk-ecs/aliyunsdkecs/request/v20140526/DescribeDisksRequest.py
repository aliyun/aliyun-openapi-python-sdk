# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeDisksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeDisks')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_DiskIds(self):
		return self.get_query_params().get('DiskIds')

	def set_DiskIds(self,DiskIds):
		self.add_query_param('DiskIds',DiskIds)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_DiskType(self):
		return self.get_query_params().get('DiskType')

	def set_DiskType(self,DiskType):
		self.add_query_param('DiskType',DiskType)

	def get_Category(self):
		return self.get_query_params().get('Category')

	def set_Category(self,Category):
		self.add_query_param('Category',Category)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)

	def get_SnapshotId(self):
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self,SnapshotId):
		self.add_query_param('SnapshotId',SnapshotId)

	def get_Portable(self):
		return self.get_query_params().get('Portable')

	def set_Portable(self,Portable):
		self.add_query_param('Portable',Portable)

	def get_DeleteWithInstance(self):
		return self.get_query_params().get('DeleteWithInstance')

	def set_DeleteWithInstance(self,DeleteWithInstance):
		self.add_query_param('DeleteWithInstance',DeleteWithInstance)

	def get_DeleteAutoSnapshot(self):
		return self.get_query_params().get('DeleteAutoSnapshot')

	def set_DeleteAutoSnapshot(self,DeleteAutoSnapshot):
		self.add_query_param('DeleteAutoSnapshot',DeleteAutoSnapshot)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_DiskName(self):
		return self.get_query_params().get('DiskName')

	def set_DiskName(self,DiskName):
		self.add_query_param('DiskName',DiskName)

	def get_AutoSnapshotPolicyId(self):
		return self.get_query_params().get('AutoSnapshotPolicyId')

	def set_AutoSnapshotPolicyId(self,AutoSnapshotPolicyId):
		self.add_query_param('AutoSnapshotPolicyId',AutoSnapshotPolicyId)

	def get_EnableAutoSnapshot(self):
		return self.get_query_params().get('EnableAutoSnapshot')

	def set_EnableAutoSnapshot(self,EnableAutoSnapshot):
		self.add_query_param('EnableAutoSnapshot',EnableAutoSnapshot)

	def get_EnableAutomatedSnapshotPolicy(self):
		return self.get_query_params().get('EnableAutomatedSnapshotPolicy')

	def set_EnableAutomatedSnapshotPolicy(self,EnableAutomatedSnapshotPolicy):
		self.add_query_param('EnableAutomatedSnapshotPolicy',EnableAutomatedSnapshotPolicy)

	def get_DiskChargeType(self):
		return self.get_query_params().get('DiskChargeType')

	def set_DiskChargeType(self,DiskChargeType):
		self.add_query_param('DiskChargeType',DiskChargeType)

	def get_LockReason(self):
		return self.get_query_params().get('LockReason')

	def set_LockReason(self,LockReason):
		self.add_query_param('LockReason',LockReason)

	def get_Filter1Key(self):
		return self.get_query_params().get('Filter.1.Key')

	def set_Filter1Key(self,Filter1Key):
		self.add_query_param('Filter.1.Key',Filter1Key)

	def get_Filter2Key(self):
		return self.get_query_params().get('Filter.2.Key')

	def set_Filter2Key(self,Filter2Key):
		self.add_query_param('Filter.2.Key',Filter2Key)

	def get_Filter1Value(self):
		return self.get_query_params().get('Filter.1.Value')

	def set_Filter1Value(self,Filter1Value):
		self.add_query_param('Filter.1.Value',Filter1Value)

	def get_Filter2Value(self):
		return self.get_query_params().get('Filter.2.Value')

	def set_Filter2Value(self,Filter2Value):
		self.add_query_param('Filter.2.Value',Filter2Value)

	def get_Tag1Key(self):
		return self.get_query_params().get('Tag.1.Key')

	def set_Tag1Key(self,Tag1Key):
		self.add_query_param('Tag.1.Key',Tag1Key)

	def get_Tag2Key(self):
		return self.get_query_params().get('Tag.2.Key')

	def set_Tag2Key(self,Tag2Key):
		self.add_query_param('Tag.2.Key',Tag2Key)

	def get_Tag3Key(self):
		return self.get_query_params().get('Tag.3.Key')

	def set_Tag3Key(self,Tag3Key):
		self.add_query_param('Tag.3.Key',Tag3Key)

	def get_Tag4Key(self):
		return self.get_query_params().get('Tag.4.Key')

	def set_Tag4Key(self,Tag4Key):
		self.add_query_param('Tag.4.Key',Tag4Key)

	def get_Tag5Key(self):
		return self.get_query_params().get('Tag.5.Key')

	def set_Tag5Key(self,Tag5Key):
		self.add_query_param('Tag.5.Key',Tag5Key)

	def get_Tag1Value(self):
		return self.get_query_params().get('Tag.1.Value')

	def set_Tag1Value(self,Tag1Value):
		self.add_query_param('Tag.1.Value',Tag1Value)

	def get_Tag2Value(self):
		return self.get_query_params().get('Tag.2.Value')

	def set_Tag2Value(self,Tag2Value):
		self.add_query_param('Tag.2.Value',Tag2Value)

	def get_Tag3Value(self):
		return self.get_query_params().get('Tag.3.Value')

	def set_Tag3Value(self,Tag3Value):
		self.add_query_param('Tag.3.Value',Tag3Value)

	def get_Tag4Value(self):
		return self.get_query_params().get('Tag.4.Value')

	def set_Tag4Value(self,Tag4Value):
		self.add_query_param('Tag.4.Value',Tag4Value)

	def get_Tag5Value(self):
		return self.get_query_params().get('Tag.5.Value')

	def set_Tag5Value(self,Tag5Value):
		self.add_query_param('Tag.5.Value',Tag5Value)