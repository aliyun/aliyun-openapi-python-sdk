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

class SendFileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'SendFile','ecs')
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
	def get_Timeout(self): # Long
		return self.get_query_params().get('Timeout')

	def set_Timeout(self, Timeout):  # Long
		self.add_query_param('Timeout', Timeout)
	def get_Content(self): # String
		return self.get_query_params().get('Content')

	def set_Content(self, Content):  # String
		self.add_query_param('Content', Content)
	def get_FileOwner(self): # String
		return self.get_query_params().get('FileOwner')

	def set_FileOwner(self, FileOwner):  # String
		self.add_query_param('FileOwner', FileOwner)
	def get_Overwrite(self): # Boolean
		return self.get_query_params().get('Overwrite')

	def set_Overwrite(self, Overwrite):  # Boolean
		self.add_query_param('Overwrite', Overwrite)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_FileMode(self): # String
		return self.get_query_params().get('FileMode')

	def set_FileMode(self, FileMode):  # String
		self.add_query_param('FileMode', FileMode)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ContentType(self): # String
		return self.get_query_params().get('ContentType')

	def set_ContentType(self, ContentType):  # String
		self.add_query_param('ContentType', ContentType)
	def get_InstanceIds(self): # RepeatList
		return self.get_query_params().get('InstanceId')

	def set_InstanceIds(self, InstanceId):  # RepeatList
		for depth1 in range(len(InstanceId)):
			self.add_query_param('InstanceId.' + str(depth1 + 1), InstanceId[depth1])
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_FileGroup(self): # String
		return self.get_query_params().get('FileGroup')

	def set_FileGroup(self, FileGroup):  # String
		self.add_query_param('FileGroup', FileGroup)
	def get_TargetDir(self): # String
		return self.get_query_params().get('TargetDir')

	def set_TargetDir(self, TargetDir):  # String
		self.add_query_param('TargetDir', TargetDir)
