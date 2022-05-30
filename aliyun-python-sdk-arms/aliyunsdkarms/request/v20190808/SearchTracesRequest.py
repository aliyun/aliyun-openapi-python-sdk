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
from aliyunsdkarms.endpoint import endpoint_data

class SearchTracesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'SearchTraces','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_Pid(self): # String
		return self.get_query_params().get('Pid')

	def set_Pid(self, Pid):  # String
		self.add_query_param('Pid', Pid)
	def get_StartTime(self): # Long
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_query_param('StartTime', StartTime)
	def get_Reverse(self): # Boolean
		return self.get_query_params().get('Reverse')

	def set_Reverse(self, Reverse):  # Boolean
		self.add_query_param('Reverse', Reverse)
	def get_MinDuration(self): # Long
		return self.get_query_params().get('MinDuration')

	def set_MinDuration(self, MinDuration):  # Long
		self.add_query_param('MinDuration', MinDuration)
	def get_ServiceIp(self): # String
		return self.get_query_params().get('ServiceIp')

	def set_ServiceIp(self, ServiceIp):  # String
		self.add_query_param('ServiceIp', ServiceIp)
	def get_ExclusionFilterss(self): # RepeatList
		return self.get_query_params().get('ExclusionFilters')

	def set_ExclusionFilterss(self, ExclusionFilters):  # RepeatList
		for depth1 in range(len(ExclusionFilters)):
			if ExclusionFilters[depth1].get('Value') is not None:
				self.add_query_param('ExclusionFilters.' + str(depth1 + 1) + '.Value', ExclusionFilters[depth1].get('Value'))
			if ExclusionFilters[depth1].get('Key') is not None:
				self.add_query_param('ExclusionFilters.' + str(depth1 + 1) + '.Key', ExclusionFilters[depth1].get('Key'))
	def get_OperationName(self): # String
		return self.get_query_params().get('OperationName')

	def set_OperationName(self, OperationName):  # String
		self.add_query_param('OperationName', OperationName)
	def get_ServiceName(self): # String
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self, ServiceName):  # String
		self.add_query_param('ServiceName', ServiceName)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
