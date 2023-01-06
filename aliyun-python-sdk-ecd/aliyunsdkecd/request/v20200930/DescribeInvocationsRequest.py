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

class DescribeInvocationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'DescribeInvocations')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_InvokeStatus(self): # String
		return self.get_query_params().get('InvokeStatus')

	def set_InvokeStatus(self, InvokeStatus):  # String
		self.add_query_param('InvokeStatus', InvokeStatus)
	def get_DesktopIdss(self): # RepeatList
		return self.get_query_params().get('DesktopIds')

	def set_DesktopIdss(self, DesktopIds):  # RepeatList
		for depth1 in range(len(DesktopIds)):
			self.add_query_param('DesktopIds.' + str(depth1 + 1), DesktopIds[depth1])
	def get_IncludeOutput(self): # Boolean
		return self.get_query_params().get('IncludeOutput')

	def set_IncludeOutput(self, IncludeOutput):  # Boolean
		self.add_query_param('IncludeOutput', IncludeOutput)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_ContentEncoding(self): # String
		return self.get_query_params().get('ContentEncoding')

	def set_ContentEncoding(self, ContentEncoding):  # String
		self.add_query_param('ContentEncoding', ContentEncoding)
	def get_EndUserId(self): # String
		return self.get_query_params().get('EndUserId')

	def set_EndUserId(self, EndUserId):  # String
		self.add_query_param('EndUserId', EndUserId)
	def get_DesktopId(self): # String
		return self.get_query_params().get('DesktopId')

	def set_DesktopId(self, DesktopId):  # String
		self.add_query_param('DesktopId', DesktopId)
	def get_InvokeId(self): # String
		return self.get_query_params().get('InvokeId')

	def set_InvokeId(self, InvokeId):  # String
		self.add_query_param('InvokeId', InvokeId)
	def get_CommandType(self): # String
		return self.get_query_params().get('CommandType')

	def set_CommandType(self, CommandType):  # String
		self.add_query_param('CommandType', CommandType)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
