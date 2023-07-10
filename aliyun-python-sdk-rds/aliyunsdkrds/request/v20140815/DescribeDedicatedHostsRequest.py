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

class DescribeDedicatedHostsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'DescribeDedicatedHosts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_HostType(self): # String
		return self.get_query_params().get('HostType')

	def set_HostType(self, HostType):  # String
		self.add_query_param('HostType', HostType)
	def get_HostStatus(self): # String
		return self.get_query_params().get('HostStatus')

	def set_HostStatus(self, HostStatus):  # String
		self.add_query_param('HostStatus', HostStatus)
	def get_AllocationStatus(self): # String
		return self.get_query_params().get('AllocationStatus')

	def set_AllocationStatus(self, AllocationStatus):  # String
		self.add_query_param('AllocationStatus', AllocationStatus)
	def get_DedicatedHostGroupId(self): # String
		return self.get_query_params().get('DedicatedHostGroupId')

	def set_DedicatedHostGroupId(self, DedicatedHostGroupId):  # String
		self.add_query_param('DedicatedHostGroupId', DedicatedHostGroupId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OrderId(self): # Long
		return self.get_query_params().get('OrderId')

	def set_OrderId(self, OrderId):  # Long
		self.add_query_param('OrderId', OrderId)
	def get_DedicatedHostId(self): # String
		return self.get_query_params().get('DedicatedHostId')

	def set_DedicatedHostId(self, DedicatedHostId):  # String
		self.add_query_param('DedicatedHostId', DedicatedHostId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
