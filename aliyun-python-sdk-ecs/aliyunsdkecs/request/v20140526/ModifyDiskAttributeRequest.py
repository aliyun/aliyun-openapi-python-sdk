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

class ModifyDiskAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyDiskAttribute','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_DiskName(self): # String
		return self.get_query_params().get('DiskName')

	def set_DiskName(self, DiskName):  # String
		self.add_query_param('DiskName', DiskName)
	def get_DeleteAutoSnapshot(self): # Boolean
		return self.get_query_params().get('DeleteAutoSnapshot')

	def set_DeleteAutoSnapshot(self, DeleteAutoSnapshot):  # Boolean
		self.add_query_param('DeleteAutoSnapshot', DeleteAutoSnapshot)
	def get_DiskIdss(self): # RepeatList
		return self.get_query_params().get('DiskIds')

	def set_DiskIdss(self, DiskIds):  # RepeatList
		for depth1 in range(len(DiskIds)):
			self.add_query_param('DiskIds.' + str(depth1 + 1), DiskIds[depth1])
	def get_DiskId(self): # String
		return self.get_query_params().get('DiskId')

	def set_DiskId(self, DiskId):  # String
		self.add_query_param('DiskId', DiskId)
	def get_DeleteWithInstance(self): # Boolean
		return self.get_query_params().get('DeleteWithInstance')

	def set_DeleteWithInstance(self, DeleteWithInstance):  # Boolean
		self.add_query_param('DeleteWithInstance', DeleteWithInstance)
	def get_EnableAutoSnapshot(self): # Boolean
		return self.get_query_params().get('EnableAutoSnapshot')

	def set_EnableAutoSnapshot(self, EnableAutoSnapshot):  # Boolean
		self.add_query_param('EnableAutoSnapshot', EnableAutoSnapshot)
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
