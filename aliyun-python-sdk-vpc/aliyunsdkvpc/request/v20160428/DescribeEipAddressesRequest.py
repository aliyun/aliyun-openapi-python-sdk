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
from aliyunsdkvpc.endpoint import endpoint_data

class DescribeEipAddressesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'DescribeEipAddresses','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_PublicIpAddressPoolId(self): # String
		return self.get_query_params().get('PublicIpAddressPoolId')

	def set_PublicIpAddressPoolId(self, PublicIpAddressPoolId):  # String
		self.add_query_param('PublicIpAddressPoolId', PublicIpAddressPoolId)
	def get_Filter2Value(self): # String
		return self.get_query_params().get('Filter.2.Value')

	def set_Filter2Value(self, Filter2Value):  # String
		self.add_query_param('Filter.2.Value', Filter2Value)
	def get_SecurityProtectionEnabled(self): # Boolean
		return self.get_query_params().get('SecurityProtectionEnabled')

	def set_SecurityProtectionEnabled(self, SecurityProtectionEnabled):  # Boolean
		self.add_query_param('SecurityProtectionEnabled', SecurityProtectionEnabled)
	def get_ISP(self): # String
		return self.get_query_params().get('ISP')

	def set_ISP(self, ISP):  # String
		self.add_query_param('ISP', ISP)
	def get_EipName(self): # String
		return self.get_query_params().get('EipName')

	def set_EipName(self, EipName):  # String
		self.add_query_param('EipName', EipName)
	def get_AllocationId(self): # String
		return self.get_query_params().get('AllocationId')

	def set_AllocationId(self, AllocationId):  # String
		self.add_query_param('AllocationId', AllocationId)
	def get_IncludeReservationData(self): # Boolean
		return self.get_query_params().get('IncludeReservationData')

	def set_IncludeReservationData(self, IncludeReservationData):  # Boolean
		self.add_query_param('IncludeReservationData', IncludeReservationData)
	def get_EipAddress(self): # String
		return self.get_query_params().get('EipAddress')

	def set_EipAddress(self, EipAddress):  # String
		self.add_query_param('EipAddress', EipAddress)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_LockReason(self): # String
		return self.get_query_params().get('LockReason')

	def set_LockReason(self, LockReason):  # String
		self.add_query_param('LockReason', LockReason)
	def get_Filter1Key(self): # String
		return self.get_query_params().get('Filter.1.Key')

	def set_Filter1Key(self, Filter1Key):  # String
		self.add_query_param('Filter.1.Key', Filter1Key)
	def get_AssociatedInstanceType(self): # String
		return self.get_query_params().get('AssociatedInstanceType')

	def set_AssociatedInstanceType(self, AssociatedInstanceType):  # String
		self.add_query_param('AssociatedInstanceType', AssociatedInstanceType)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_SegmentInstanceId(self): # String
		return self.get_query_params().get('SegmentInstanceId')

	def set_SegmentInstanceId(self, SegmentInstanceId):  # String
		self.add_query_param('SegmentInstanceId', SegmentInstanceId)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_Filter1Value(self): # String
		return self.get_query_params().get('Filter.1.Value')

	def set_Filter1Value(self, Filter1Value):  # String
		self.add_query_param('Filter.1.Value', Filter1Value)
	def get_Filter2Key(self): # String
		return self.get_query_params().get('Filter.2.Key')

	def set_Filter2Key(self, Filter2Key):  # String
		self.add_query_param('Filter.2.Key', Filter2Key)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
	def get_AssociatedInstanceId(self): # String
		return self.get_query_params().get('AssociatedInstanceId')

	def set_AssociatedInstanceId(self, AssociatedInstanceId):  # String
		self.add_query_param('AssociatedInstanceId', AssociatedInstanceId)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
