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
from aliyunsdknas.endpoint import endpoint_data

class CreateDirRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'CreateDir','nas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Recursion(self): # Boolean
		return self.get_query_params().get('Recursion')

	def set_Recursion(self, Recursion):  # Boolean
		self.add_query_param('Recursion', Recursion)
	def get_FileSystemId(self): # String
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self, FileSystemId):  # String
		self.add_query_param('FileSystemId', FileSystemId)
	def get_OwnerGroupId(self): # Integer
		return self.get_query_params().get('OwnerGroupId')

	def set_OwnerGroupId(self, OwnerGroupId):  # Integer
		self.add_query_param('OwnerGroupId', OwnerGroupId)
	def get_OwnerUserId(self): # Integer
		return self.get_query_params().get('OwnerUserId')

	def set_OwnerUserId(self, OwnerUserId):  # Integer
		self.add_query_param('OwnerUserId', OwnerUserId)
	def get_Permission(self): # String
		return self.get_query_params().get('Permission')

	def set_Permission(self, Permission):  # String
		self.add_query_param('Permission', Permission)
	def get_RootDirectory(self): # String
		return self.get_query_params().get('RootDirectory')

	def set_RootDirectory(self, RootDirectory):  # String
		self.add_query_param('RootDirectory', RootDirectory)
