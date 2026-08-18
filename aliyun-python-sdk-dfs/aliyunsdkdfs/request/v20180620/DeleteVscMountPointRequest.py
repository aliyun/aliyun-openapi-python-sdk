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

class DeleteVscMountPointRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DFS', '2018-06-20', 'DeleteVscMountPoint','alidfs')
		self.set_method('POST')

	def get_InputRegionId(self): # String
		return self.get_query_params().get('InputRegionId')

	def set_InputRegionId(self, InputRegionId):  # String
		self.add_query_param('InputRegionId', InputRegionId)
	def get_MountPointId(self): # String
		return self.get_query_params().get('MountPointId')

	def set_MountPointId(self, MountPointId):  # String
		self.add_query_param('MountPointId', MountPointId)
	def get_FileSystemId(self): # String
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self, FileSystemId):  # String
		self.add_query_param('FileSystemId', FileSystemId)
