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

class RefreshMediaPlayUrlsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'RefreshMediaPlayUrls','vod')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Formats(self): # String
		return self.get_query_params().get('Formats')

	def set_Formats(self, Formats):  # String
		self.add_query_param('Formats', Formats)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_MediaIds(self): # String
		return self.get_query_params().get('MediaIds')

	def set_MediaIds(self, MediaIds):  # String
		self.add_query_param('MediaIds', MediaIds)
	def get_Definitions(self): # String
		return self.get_query_params().get('Definitions')

	def set_Definitions(self, Definitions):  # String
		self.add_query_param('Definitions', Definitions)
	def get_StreamType(self): # String
		return self.get_query_params().get('StreamType')

	def set_StreamType(self, StreamType):  # String
		self.add_query_param('StreamType', StreamType)
	def get_TaskType(self): # String
		return self.get_query_params().get('TaskType')

	def set_TaskType(self, TaskType):  # String
		self.add_query_param('TaskType', TaskType)
	def get_SliceFlag(self): # Boolean
		return self.get_query_params().get('SliceFlag')

	def set_SliceFlag(self, SliceFlag):  # Boolean
		self.add_query_param('SliceFlag', SliceFlag)
	def get_ResultType(self): # String
		return self.get_query_params().get('ResultType')

	def set_ResultType(self, ResultType):  # String
		self.add_query_param('ResultType', ResultType)
	def get_SliceCount(self): # Integer
		return self.get_query_params().get('SliceCount')

	def set_SliceCount(self, SliceCount):  # Integer
		self.add_query_param('SliceCount', SliceCount)
