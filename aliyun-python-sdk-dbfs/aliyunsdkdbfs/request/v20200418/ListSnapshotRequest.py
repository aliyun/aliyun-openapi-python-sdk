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
from aliyunsdkdbfs.endpoint import endpoint_data

class ListSnapshotRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DBFS', '2020-04-18', 'ListSnapshot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SortType(self):
		return self.get_query_params().get('SortType')

	def set_SortType(self,SortType):
		self.add_query_param('SortType',SortType)

	def get_SnapshotIds(self):
		return self.get_query_params().get('SnapshotIds')

	def set_SnapshotIds(self,SnapshotIds):
		self.add_query_param('SnapshotIds',SnapshotIds)

	def get_FilterValue(self):
		return self.get_query_params().get('FilterValue')

	def set_FilterValue(self,FilterValue):
		self.add_query_param('FilterValue',FilterValue)

	def get_SnapshotName(self):
		return self.get_query_params().get('SnapshotName')

	def set_SnapshotName(self,SnapshotName):
		self.add_query_param('SnapshotName',SnapshotName)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_FilterKey(self):
		return self.get_query_params().get('FilterKey')

	def set_FilterKey(self,FilterKey):
		self.add_query_param('FilterKey',FilterKey)

	def get_SortKey(self):
		return self.get_query_params().get('SortKey')

	def set_SortKey(self,SortKey):
		self.add_query_param('SortKey',SortKey)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_FsId(self):
		return self.get_query_params().get('FsId')

	def set_FsId(self,FsId):
		self.add_query_param('FsId',FsId)

	def get_SnapshotType(self):
		return self.get_query_params().get('SnapshotType')

	def set_SnapshotType(self,SnapshotType):
		self.add_query_param('SnapshotType',SnapshotType)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)