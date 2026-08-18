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

class ModifyFileSystemRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DFS', '2018-06-20', 'ModifyFileSystem','alidfs')
		self.set_method('POST')

	def get_ThroughputMode(self): # String
		return self.get_query_params().get('ThroughputMode')

	def set_ThroughputMode(self, ThroughputMode):  # String
		self.add_query_param('ThroughputMode', ThroughputMode)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_FileSystemName(self): # String
		return self.get_query_params().get('FileSystemName')

	def set_FileSystemName(self, FileSystemName):  # String
		self.add_query_param('FileSystemName', FileSystemName)
	def get_InputRegionId(self): # String
		return self.get_query_params().get('InputRegionId')

	def set_InputRegionId(self, InputRegionId):  # String
		self.add_query_param('InputRegionId', InputRegionId)
	def get_SpaceCapacity(self): # Long
		return self.get_query_params().get('SpaceCapacity')

	def set_SpaceCapacity(self, SpaceCapacity):  # Long
		self.add_query_param('SpaceCapacity', SpaceCapacity)
	def get_FileSystemId(self): # String
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self, FileSystemId):  # String
		self.add_query_param('FileSystemId', FileSystemId)
	def get_ProvisionedThroughputInMiBps(self): # Long
		return self.get_query_params().get('ProvisionedThroughputInMiBps')

	def set_ProvisionedThroughputInMiBps(self, ProvisionedThroughputInMiBps):  # Long
		self.add_query_param('ProvisionedThroughputInMiBps', ProvisionedThroughputInMiBps)
