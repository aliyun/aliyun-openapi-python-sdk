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

class ModifyDBNodesClassRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'ModifyDBNodesClass','polardb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_PlannedEndTime(self): # String
		return self.get_query_params().get('PlannedEndTime')

	def set_PlannedEndTime(self, PlannedEndTime):  # String
		self.add_query_param('PlannedEndTime', PlannedEndTime)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_DBClusterId(self): # String
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self, DBClusterId):  # String
		self.add_query_param('DBClusterId', DBClusterId)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_PlannedFlashingOffTime(self): # String
		return self.get_query_params().get('PlannedFlashingOffTime')

	def set_PlannedFlashingOffTime(self, PlannedFlashingOffTime):  # String
		self.add_query_param('PlannedFlashingOffTime', PlannedFlashingOffTime)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_PlannedStartTime(self): # String
		return self.get_query_params().get('PlannedStartTime')

	def set_PlannedStartTime(self, PlannedStartTime):  # String
		self.add_query_param('PlannedStartTime', PlannedStartTime)
	def get_ModifyType(self): # String
		return self.get_query_params().get('ModifyType')

	def set_ModifyType(self, ModifyType):  # String
		self.add_query_param('ModifyType', ModifyType)
	def get_SubCategory(self): # String
		return self.get_query_params().get('SubCategory')

	def set_SubCategory(self, SubCategory):  # String
		self.add_query_param('SubCategory', SubCategory)
	def get_DBNodes(self): # RepeatList
		return self.get_query_params().get('DBNode')

	def set_DBNodes(self, DBNode):  # RepeatList
		for depth1 in range(len(DBNode)):
			if DBNode[depth1].get('DBNodeId') is not None:
				self.add_query_param('DBNode.' + str(depth1 + 1) + '.DBNodeId', DBNode[depth1].get('DBNodeId'))
			if DBNode[depth1].get('TargetClass') is not None:
				self.add_query_param('DBNode.' + str(depth1 + 1) + '.TargetClass', DBNode[depth1].get('TargetClass'))
