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
from aliyunsdkvod.endpoint import endpoint_data

class ListSnapshotsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'ListSnapshots','vod')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_AuthTimeout(self): # String
		return self.get_query_params().get('AuthTimeout')

	def set_AuthTimeout(self, AuthTimeout):  # String
		self.add_query_param('AuthTimeout', AuthTimeout)
	def get_VideoId(self): # String
		return self.get_query_params().get('VideoId')

	def set_VideoId(self, VideoId):  # String
		self.add_query_param('VideoId', VideoId)
	def get_SnapshotType(self): # String
		return self.get_query_params().get('SnapshotType')

	def set_SnapshotType(self, SnapshotType):  # String
		self.add_query_param('SnapshotType', SnapshotType)
	def get_PageNo(self): # String
		return self.get_query_params().get('PageNo')

	def set_PageNo(self, PageNo):  # String
		self.add_query_param('PageNo', PageNo)
