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
from aliyunsdkecs.endpoint import endpoint_data

class DescribeDisksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeDisks','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_Filter2Value(self): # String
		return self.get_query_params().get('Filter.2.Value')

	def set_Filter2Value(self, Filter2Value):  # String
		self.add_query_param('Filter.2.Value', Filter2Value)
	def get_AutoSnapshotPolicyId(self): # String
		return self.get_query_params().get('AutoSnapshotPolicyId')

	def set_AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):  # String
		self.add_query_param('AutoSnapshotPolicyId', AutoSnapshotPolicyId)
	def get_DiskName(self): # String
		return self.get_query_params().get('DiskName')

	def set_DiskName(self, DiskName):  # String
		self.add_query_param('DiskName', DiskName)
	def get_DeleteAutoSnapshot(self): # Boolean
		return self.get_query_params().get('DeleteAutoSnapshot')

	def set_DeleteAutoSnapshot(self, DeleteAutoSnapshot):  # Boolean
		self.add_query_param('DeleteAutoSnapshot', DeleteAutoSnapshot)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_DiskChargeType(self): # String
		return self.get_query_params().get('DiskChargeType')

	def set_DiskChargeType(self, DiskChargeType):  # String
		self.add_query_param('DiskChargeType', DiskChargeType)
	def get_LockReason(self): # String
		return self.get_query_params().get('LockReason')

	def set_LockReason(self, LockReason):  # String
		self.add_query_param('LockReason', LockReason)
	def get_Filter1Key(self): # String
		return self.get_query_params().get('Filter.1.Key')

	def set_Filter1Key(self, Filter1Key):  # String
		self.add_query_param('Filter.1.Key', Filter1Key)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.value', Tag[depth1].get('value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_EnableAutoSnapshot(self): # Boolean
		return self.get_query_params().get('EnableAutoSnapshot')

	def set_EnableAutoSnapshot(self, EnableAutoSnapshot):  # Boolean
		self.add_query_param('EnableAutoSnapshot', EnableAutoSnapshot)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_Filter1Value(self): # String
		return self.get_query_params().get('Filter.1.Value')

	def set_Filter1Value(self, Filter1Value):  # String
		self.add_query_param('Filter.1.Value', Filter1Value)
	def get_Portable(self): # Boolean
		return self.get_query_params().get('Portable')

	def set_Portable(self, Portable):  # Boolean
		self.add_query_param('Portable', Portable)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_AdditionalAttributess(self): # RepeatList
		return self.get_query_params().get('AdditionalAttributes')

	def set_AdditionalAttributess(self, AdditionalAttributes):  # RepeatList
		for depth1 in range(len(AdditionalAttributes)):
			self.add_query_param('AdditionalAttributes.' + str(depth1 + 1), AdditionalAttributes[depth1])
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
	def get_SnapshotId(self): # String
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self, SnapshotId):  # String
		self.add_query_param('SnapshotId', SnapshotId)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_DiskIds(self): # String
		return self.get_query_params().get('DiskIds')

	def set_DiskIds(self, DiskIds):  # String
		self.add_query_param('DiskIds', DiskIds)
	def get_MultiAttach(self): # String
		return self.get_query_params().get('MultiAttach')

	def set_MultiAttach(self, MultiAttach):  # String
		self.add_query_param('MultiAttach', MultiAttach)
	def get_DeleteWithInstance(self): # Boolean
		return self.get_query_params().get('DeleteWithInstance')

	def set_DeleteWithInstance(self, DeleteWithInstance):  # Boolean
		self.add_query_param('DeleteWithInstance', DeleteWithInstance)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_EnableAutomatedSnapshotPolicy(self): # Boolean
		return self.get_query_params().get('EnableAutomatedSnapshotPolicy')

	def set_EnableAutomatedSnapshotPolicy(self, EnableAutomatedSnapshotPolicy):  # Boolean
		self.add_query_param('EnableAutomatedSnapshotPolicy', EnableAutomatedSnapshotPolicy)
	def get_Filter2Key(self): # String
		return self.get_query_params().get('Filter.2.Key')

	def set_Filter2Key(self, Filter2Key):  # String
		self.add_query_param('Filter.2.Key', Filter2Key)
	def get_DiskType(self): # String
		return self.get_query_params().get('DiskType')

	def set_DiskType(self, DiskType):  # String
		self.add_query_param('DiskType', DiskType)
	def get_EnableShared(self): # Boolean
		return self.get_query_params().get('EnableShared')

	def set_EnableShared(self, EnableShared):  # Boolean
		self.add_query_param('EnableShared', EnableShared)
	def get_Encrypted(self): # Boolean
		return self.get_query_params().get('Encrypted')

	def set_Encrypted(self, Encrypted):  # Boolean
		self.add_query_param('Encrypted', Encrypted)
	def get_Category(self): # String
		return self.get_query_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_query_param('Category', Category)
	def get_KMSKeyId(self): # String
		return self.get_query_params().get('KMSKeyId')

	def set_KMSKeyId(self, KMSKeyId):  # String
		self.add_query_param('KMSKeyId', KMSKeyId)
