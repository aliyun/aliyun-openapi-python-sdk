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

class DescribeAutoSnapshotTasksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'DescribeAutoSnapshotTasks','nas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FileSystemType(self): # String
		return self.get_query_params().get('FileSystemType')

	def set_FileSystemType(self, FileSystemType):  # String
		self.add_query_param('FileSystemType', FileSystemType)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_FileSystemIds(self): # String
		return self.get_query_params().get('FileSystemIds')

	def set_FileSystemIds(self, FileSystemIds):  # String
		self.add_query_param('FileSystemIds', FileSystemIds)
	def get_AutoSnapshotPolicyIds(self): # String
		return self.get_query_params().get('AutoSnapshotPolicyIds')

	def set_AutoSnapshotPolicyIds(self, AutoSnapshotPolicyIds):  # String
		self.add_query_param('AutoSnapshotPolicyIds', AutoSnapshotPolicyIds)
