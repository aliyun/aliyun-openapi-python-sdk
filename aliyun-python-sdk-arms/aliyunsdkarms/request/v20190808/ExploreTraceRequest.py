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

class ExploreTraceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'ExploreTrace','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TraceId(self): # String
		return self.get_query_params().get('TraceId')

	def set_TraceId(self, TraceId):  # String
		self.add_query_param('TraceId', TraceId)
	def get_Kind(self): # String
		return self.get_query_params().get('Kind')

	def set_Kind(self, Kind):  # String
		self.add_query_param('Kind', Kind)
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_StartTime(self): # Long
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_query_param('StartTime', StartTime)
	def get_MinDuration(self): # Long
		return self.get_query_params().get('MinDuration')

	def set_MinDuration(self, MinDuration):  # Long
		self.add_query_param('MinDuration', MinDuration)
	def get_SelectedField(self): # String
		return self.get_query_params().get('SelectedField')

	def set_SelectedField(self, SelectedField):  # String
		self.add_query_param('SelectedField', SelectedField)
	def get_ServiceIp(self): # String
		return self.get_query_params().get('ServiceIp')

	def set_ServiceIp(self, ServiceIp):  # String
		self.add_query_param('ServiceIp', ServiceIp)
	def get_StatusCode(self): # String
		return self.get_query_params().get('StatusCode')

	def set_StatusCode(self, StatusCode):  # String
		self.add_query_param('StatusCode', StatusCode)
	def get_MaxDuration(self): # Long
		return self.get_query_params().get('MaxDuration')

	def set_MaxDuration(self, MaxDuration):  # Long
		self.add_query_param('MaxDuration', MaxDuration)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_ServiceName(self): # String
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self, ServiceName):  # String
		self.add_query_param('ServiceName', ServiceName)
	def get_Attributess(self): # RepeatList
		return self.get_query_params().get('Attributes')

	def set_Attributess(self, Attributes):  # RepeatList
		for depth1 in range(len(Attributes)):
			if Attributes[depth1].get('Value') is not None:
				self.add_query_param('Attributes.' + str(depth1 + 1) + '.Value', Attributes[depth1].get('Value'))
			if Attributes[depth1].get('Key') is not None:
				self.add_query_param('Attributes.' + str(depth1 + 1) + '.Key', Attributes[depth1].get('Key'))
			if Attributes[depth1].get('Operator') is not None:
				self.add_query_param('Attributes.' + str(depth1 + 1) + '.Operator', Attributes[depth1].get('Operator'))
	def get_Page(self): # Integer
		return self.get_query_params().get('Page')

	def set_Page(self, Page):  # Integer
		self.add_query_param('Page', Page)
	def get_SpanName(self): # String
		return self.get_query_params().get('SpanName')

	def set_SpanName(self, SpanName):  # String
		self.add_query_param('SpanName', SpanName)
