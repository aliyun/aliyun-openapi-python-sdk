# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class LookupEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Actiontrail', '2017-12-04', 'LookupEvents','actiontrail')

	def get_Request(self):
		return self.get_query_params().get('Request')

	def set_Request(self,Request):
		self.add_query_param('Request',Request)

	def get_Format(self):
		return self.get_query_params().get('Format')

	def set_Format(self,Format):
		self.add_query_param('Format',Format)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_Version(self):
		return self.get_query_params().get('Version')

	def set_Version(self,Version):
		self.add_query_param('Version',Version)

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)

	def get_EventName(self):
		return self.get_query_params().get('EventName')

	def set_EventName(self,EventName):
		self.add_query_param('EventName',EventName)

	def get_Help(self):
		return self.get_query_params().get('Help')

	def set_Help(self,Help):
		self.add_query_param('Help',Help)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)

	def get_EventType(self):
		return self.get_query_params().get('EventType')

	def set_EventType(self,EventType):
		self.add_query_param('EventType',EventType)

	def get_ServiceName(self):
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self,ServiceName):
		self.add_query_param('ServiceName',ServiceName)

	def get_ResourceName(self):
		return self.get_query_params().get('ResourceName')

	def set_ResourceName(self,ResourceName):
		self.add_query_param('ResourceName',ResourceName)

	def get_Event(self):
		return self.get_query_params().get('Event')

	def set_Event(self,Event):
		self.add_query_param('Event',Event)

	def get_User(self):
		return self.get_query_params().get('User')

	def set_User(self,User):
		self.add_query_param('User',User)