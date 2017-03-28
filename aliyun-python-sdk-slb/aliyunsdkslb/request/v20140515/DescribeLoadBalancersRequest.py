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
class DescribeLoadBalancersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Slb', '2014-05-15', 'DescribeLoadBalancers')

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

	def get_ServerId(self):
		return self.get_query_params().get('ServerId')

	def set_ServerId(self,ServerId):
		self.add_query_param('ServerId',ServerId)

	def get_LoadBalancerId(self):
		return self.get_query_params().get('LoadBalancerId')

	def set_LoadBalancerId(self,LoadBalancerId):
		self.add_query_param('LoadBalancerId',LoadBalancerId)

	def get_AddressType(self):
		return self.get_query_params().get('AddressType')

	def set_AddressType(self,AddressType):
		self.add_query_param('AddressType',AddressType)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_NetworkType(self):
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self,NetworkType):
		self.add_query_param('NetworkType',NetworkType)

	def get_Address(self):
		return self.get_query_params().get('Address')

	def set_Address(self,Address):
		self.add_query_param('Address',Address)

	def get_MasterZoneId(self):
		return self.get_query_params().get('MasterZoneId')

	def set_MasterZoneId(self,MasterZoneId):
		self.add_query_param('MasterZoneId',MasterZoneId)

	def get_SlaveZoneId(self):
		return self.get_query_params().get('SlaveZoneId')

	def set_SlaveZoneId(self,SlaveZoneId):
		self.add_query_param('SlaveZoneId',SlaveZoneId)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_access_key_id(self):
		return self.get_query_params().get('access_key_id')

	def set_access_key_id(self,access_key_id):
		self.add_query_param('access_key_id',access_key_id)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_query_param('Tags',Tags)