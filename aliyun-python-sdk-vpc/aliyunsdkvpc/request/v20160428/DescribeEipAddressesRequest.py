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
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'DescribeEipAddresses','Vpc')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Filter2Value(self):
		return self.get_query_params().get('Filter.2.Value')

	def set_Filter2Value(self,Filter2Value):
		self.add_query_param('Filter.2.Value',Filter2Value)

	def get_ISP(self):
		return self.get_query_params().get('ISP')

	def set_ISP(self,ISP):
		self.add_query_param('ISP',ISP)

	def get_AllocationId(self):
		return self.get_query_params().get('AllocationId')

	def set_AllocationId(self,AllocationId):
		self.add_query_param('AllocationId',AllocationId)

	def get_IncludeReservationData(self):
		return self.get_query_params().get('IncludeReservationData')

	def set_IncludeReservationData(self,IncludeReservationData):
		self.add_query_param('IncludeReservationData',IncludeReservationData)

	def get_EipAddress(self):
		return self.get_query_params().get('EipAddress')

	def set_EipAddress(self,EipAddress):
		self.add_query_param('EipAddress',EipAddress)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_LockReason(self):
		return self.get_query_params().get('LockReason')

	def set_LockReason(self,LockReason):
		self.add_query_param('LockReason',LockReason)

	def get_Filter1Key(self):
		return self.get_query_params().get('Filter.1.Key')

	def set_Filter1Key(self,Filter1Key):
		self.add_query_param('Filter.1.Key',Filter1Key)

	def get_AssociatedInstanceType(self):
		return self.get_query_params().get('AssociatedInstanceType')

	def set_AssociatedInstanceType(self,AssociatedInstanceType):
		self.add_query_param('AssociatedInstanceType',AssociatedInstanceType)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_SegmentInstanceId(self):
		return self.get_query_params().get('SegmentInstanceId')

	def set_SegmentInstanceId(self,SegmentInstanceId):
		self.add_query_param('SegmentInstanceId',SegmentInstanceId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_Filter1Value(self):
		return self.get_query_params().get('Filter.1.Value')

	def set_Filter1Value(self,Filter1Value):
		self.add_query_param('Filter.1.Value',Filter1Value)

	def get_Filter2Key(self):
		return self.get_query_params().get('Filter.2.Key')

	def set_Filter2Key(self,Filter2Key):
		self.add_query_param('Filter.2.Key',Filter2Key)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ChargeType(self):
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self,ChargeType):
		self.add_query_param('ChargeType',ChargeType)

	def get_AssociatedInstanceId(self):
		return self.get_query_params().get('AssociatedInstanceId')

	def set_AssociatedInstanceId(self,AssociatedInstanceId):
		self.add_query_param('AssociatedInstanceId',AssociatedInstanceId)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)