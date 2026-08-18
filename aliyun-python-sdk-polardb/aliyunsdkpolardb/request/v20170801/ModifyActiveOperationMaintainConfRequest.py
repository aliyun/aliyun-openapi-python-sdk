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
from aliyunsdkpolardb.endpoint import endpoint_data

class ModifyActiveOperationMaintainConfRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'ModifyActiveOperationMaintainConf','polardb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_CycleTime(self): # String
		return self.get_query_params().get('CycleTime')

	def set_CycleTime(self, CycleTime):  # String
		self.add_query_param('CycleTime', CycleTime)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_MaintainStartTime(self): # String
		return self.get_query_params().get('MaintainStartTime')

	def set_MaintainStartTime(self, MaintainStartTime):  # String
		self.add_query_param('MaintainStartTime', MaintainStartTime)
	def get_CycleType(self): # String
		return self.get_query_params().get('CycleType')

	def set_CycleType(self, CycleType):  # String
		self.add_query_param('CycleType', CycleType)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_MaintainEndTime(self): # String
		return self.get_query_params().get('MaintainEndTime')

	def set_MaintainEndTime(self, MaintainEndTime):  # String
		self.add_query_param('MaintainEndTime', MaintainEndTime)
	def get_Comment(self): # String
		return self.get_query_params().get('Comment')

	def set_Comment(self, Comment):  # String
		self.add_query_param('Comment', Comment)
	def get_Status(self): # Long
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # Long
		self.add_query_param('Status', Status)
