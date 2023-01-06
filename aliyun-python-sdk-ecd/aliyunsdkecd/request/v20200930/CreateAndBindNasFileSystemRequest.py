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
from aliyunsdkecd.endpoint import endpoint_data

class CreateAndBindNasFileSystemRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'CreateAndBindNasFileSystem')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OfficeSiteId(self): # String
		return self.get_query_params().get('OfficeSiteId')

	def set_OfficeSiteId(self, OfficeSiteId):  # String
		self.add_query_param('OfficeSiteId', OfficeSiteId)
	def get_EndUserIdss(self): # RepeatList
		return self.get_query_params().get('EndUserIds')

	def set_EndUserIdss(self, EndUserIds):  # RepeatList
		for depth1 in range(len(EndUserIds)):
			self.add_query_param('EndUserIds.' + str(depth1 + 1), EndUserIds[depth1])
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_StorageType(self): # String
		return self.get_query_params().get('StorageType')

	def set_StorageType(self, StorageType):  # String
		self.add_query_param('StorageType', StorageType)
	def get_EncryptType(self): # Integer
		return self.get_query_params().get('EncryptType')

	def set_EncryptType(self, EncryptType):  # Integer
		self.add_query_param('EncryptType', EncryptType)
	def get_DesktopGroupId(self): # String
		return self.get_query_params().get('DesktopGroupId')

	def set_DesktopGroupId(self, DesktopGroupId):  # String
		self.add_query_param('DesktopGroupId', DesktopGroupId)
	def get_FileSystemName(self): # String
		return self.get_query_params().get('FileSystemName')

	def set_FileSystemName(self, FileSystemName):  # String
		self.add_query_param('FileSystemName', FileSystemName)
