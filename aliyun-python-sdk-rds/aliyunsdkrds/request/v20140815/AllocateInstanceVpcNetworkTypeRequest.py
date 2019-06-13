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
class AllocateInstanceVpcNetworkTypeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'AllocateInstanceVpcNetworkType','rds')

	def get_TargetVpcId(self):
		return self.get_query_params().get('TargetVpcId')

	def set_TargetVpcId(self,TargetVpcId):
		self.add_query_param('TargetVpcId',TargetVpcId)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_TargetZoneId(self):
		return self.get_query_params().get('TargetZoneId')

	def set_TargetZoneId(self,TargetZoneId):
		self.add_query_param('TargetZoneId',TargetZoneId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)

	def get_TargetRegionId(self):
		return self.get_query_params().get('TargetRegionId')

	def set_TargetRegionId(self,TargetRegionId):
		self.add_query_param('TargetRegionId',TargetRegionId)

	def get_TargetVSwitchId(self):
		return self.get_query_params().get('TargetVSwitchId')

	def set_TargetVSwitchId(self,TargetVSwitchId):
		self.add_query_param('TargetVSwitchId',TargetVSwitchId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)