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
from aliyunsdkice.endpoint import endpoint_data

class ListMediaBasicInfosRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'ListMediaBasicInfos','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_BusinessType(self): # String
		return self.get_query_params().get('BusinessType')

	def set_BusinessType(self, BusinessType):  # String
		self.add_query_param('BusinessType', BusinessType)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_IncludeFileBasicInfo(self): # Boolean
		return self.get_query_params().get('IncludeFileBasicInfo')

	def set_IncludeFileBasicInfo(self, IncludeFileBasicInfo):  # Boolean
		self.add_query_param('IncludeFileBasicInfo', IncludeFileBasicInfo)
	def get_MediaId(self): # String
		return self.get_query_params().get('MediaId')

	def set_MediaId(self, MediaId):  # String
		self.add_query_param('MediaId', MediaId)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_SortBy(self): # String
		return self.get_query_params().get('SortBy')

	def set_SortBy(self, SortBy):  # String
		self.add_query_param('SortBy', SortBy)
	def get_MediaType(self): # String
		return self.get_query_params().get('MediaType')

	def set_MediaType(self, MediaType):  # String
		self.add_query_param('MediaType', MediaType)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
