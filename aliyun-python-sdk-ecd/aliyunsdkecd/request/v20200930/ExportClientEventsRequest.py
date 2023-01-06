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

class ExportClientEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'ExportClientEvents')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OfficeSiteId(self): # String
		return self.get_query_params().get('OfficeSiteId')

	def set_OfficeSiteId(self, OfficeSiteId):  # String
		self.add_query_param('OfficeSiteId', OfficeSiteId)
	def get_EventTypess(self): # RepeatList
		return self.get_query_params().get('EventTypes')

	def set_EventTypess(self, EventTypes):  # RepeatList
		for depth1 in range(len(EventTypes)):
			self.add_query_param('EventTypes.' + str(depth1 + 1), EventTypes[depth1])
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_EndUserId(self): # String
		return self.get_query_params().get('EndUserId')

	def set_EndUserId(self, EndUserId):  # String
		self.add_query_param('EndUserId', EndUserId)
	def get_DesktopId(self): # String
		return self.get_query_params().get('DesktopId')

	def set_DesktopId(self, DesktopId):  # String
		self.add_query_param('DesktopId', DesktopId)
	def get_DesktopName(self): # String
		return self.get_query_params().get('DesktopName')

	def set_DesktopName(self, DesktopName):  # String
		self.add_query_param('DesktopName', DesktopName)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_OfficeSiteName(self): # String
		return self.get_query_params().get('OfficeSiteName')

	def set_OfficeSiteName(self, OfficeSiteName):  # String
		self.add_query_param('OfficeSiteName', OfficeSiteName)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_EventType(self): # String
		return self.get_query_params().get('EventType')

	def set_EventType(self, EventType):  # String
		self.add_query_param('EventType', EventType)
	def get_LangType(self): # String
		return self.get_query_params().get('LangType')

	def set_LangType(self, LangType):  # String
		self.add_query_param('LangType', LangType)
