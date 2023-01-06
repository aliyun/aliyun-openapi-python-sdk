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

class DescribeUserConnectionRecordsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'DescribeUserConnectionRecords')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ConnectEndTimeFrom(self): # Long
		return self.get_query_params().get('ConnectEndTimeFrom')

	def set_ConnectEndTimeFrom(self, ConnectEndTimeFrom):  # Long
		self.add_query_param('ConnectEndTimeFrom', ConnectEndTimeFrom)
	def get_ConnectDurationFrom(self): # Long
		return self.get_query_params().get('ConnectDurationFrom')

	def set_ConnectDurationFrom(self, ConnectDurationFrom):  # Long
		self.add_query_param('ConnectDurationFrom', ConnectDurationFrom)
	def get_ConnectDurationTo(self): # Long
		return self.get_query_params().get('ConnectDurationTo')

	def set_ConnectDurationTo(self, ConnectDurationTo):  # Long
		self.add_query_param('ConnectDurationTo', ConnectDurationTo)
	def get_EndUserType(self): # String
		return self.get_query_params().get('EndUserType')

	def set_EndUserType(self, EndUserType):  # String
		self.add_query_param('EndUserType', EndUserType)
	def get_DesktopGroupId(self): # String
		return self.get_query_params().get('DesktopGroupId')

	def set_DesktopGroupId(self, DesktopGroupId):  # String
		self.add_query_param('DesktopGroupId', DesktopGroupId)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_ConnectStartTimeFrom(self): # Long
		return self.get_query_params().get('ConnectStartTimeFrom')

	def set_ConnectStartTimeFrom(self, ConnectStartTimeFrom):  # Long
		self.add_query_param('ConnectStartTimeFrom', ConnectStartTimeFrom)
	def get_EndUserId(self): # String
		return self.get_query_params().get('EndUserId')

	def set_EndUserId(self, EndUserId):  # String
		self.add_query_param('EndUserId', EndUserId)
	def get_DesktopId(self): # String
		return self.get_query_params().get('DesktopId')

	def set_DesktopId(self, DesktopId):  # String
		self.add_query_param('DesktopId', DesktopId)
	def get_ConnectEndTimeTo(self): # Long
		return self.get_query_params().get('ConnectEndTimeTo')

	def set_ConnectEndTimeTo(self, ConnectEndTimeTo):  # Long
		self.add_query_param('ConnectEndTimeTo', ConnectEndTimeTo)
	def get_ConnectStartTimeTo(self): # Long
		return self.get_query_params().get('ConnectStartTimeTo')

	def set_ConnectStartTimeTo(self, ConnectStartTimeTo):  # Long
		self.add_query_param('ConnectStartTimeTo', ConnectStartTimeTo)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
