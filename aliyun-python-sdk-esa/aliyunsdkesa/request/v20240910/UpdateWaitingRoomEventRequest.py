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

class UpdateWaitingRoomEventRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ESA', '2024-09-10', 'UpdateWaitingRoomEvent')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_SessionDuration(self): # String
		return self.get_query_params().get('SessionDuration')

	def set_SessionDuration(self, SessionDuration):  # String
		self.add_query_param('SessionDuration', SessionDuration)
	def get_WaitingRoomType(self): # String
		return self.get_query_params().get('WaitingRoomType')

	def set_WaitingRoomType(self, WaitingRoomType):  # String
		self.add_query_param('WaitingRoomType', WaitingRoomType)
	def get_TotalActiveUsers(self): # String
		return self.get_query_params().get('TotalActiveUsers')

	def set_TotalActiveUsers(self, TotalActiveUsers):  # String
		self.add_query_param('TotalActiveUsers', TotalActiveUsers)
	def get_QueuingMethod(self): # String
		return self.get_query_params().get('QueuingMethod')

	def set_QueuingMethod(self, QueuingMethod):  # String
		self.add_query_param('QueuingMethod', QueuingMethod)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_Language(self): # String
		return self.get_query_params().get('Language')

	def set_Language(self, Language):  # String
		self.add_query_param('Language', Language)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_DisableSessionRenewalEnable(self): # String
		return self.get_query_params().get('DisableSessionRenewalEnable')

	def set_DisableSessionRenewalEnable(self, DisableSessionRenewalEnable):  # String
		self.add_query_param('DisableSessionRenewalEnable', DisableSessionRenewalEnable)
	def get_RandomPreQueueEnable(self): # String
		return self.get_query_params().get('RandomPreQueueEnable')

	def set_RandomPreQueueEnable(self, RandomPreQueueEnable):  # String
		self.add_query_param('RandomPreQueueEnable', RandomPreQueueEnable)
	def get_JsonResponseEnable(self): # String
		return self.get_query_params().get('JsonResponseEnable')

	def set_JsonResponseEnable(self, JsonResponseEnable):  # String
		self.add_query_param('JsonResponseEnable', JsonResponseEnable)
	def get_QueuingStatusCode(self): # String
		return self.get_query_params().get('QueuingStatusCode')

	def set_QueuingStatusCode(self, QueuingStatusCode):  # String
		self.add_query_param('QueuingStatusCode', QueuingStatusCode)
	def get_WaitingRoomEventId(self): # Long
		return self.get_query_params().get('WaitingRoomEventId')

	def set_WaitingRoomEventId(self, WaitingRoomEventId):  # Long
		self.add_query_param('WaitingRoomEventId', WaitingRoomEventId)
	def get_Enable(self): # String
		return self.get_query_params().get('Enable')

	def set_Enable(self, Enable):  # String
		self.add_query_param('Enable', Enable)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_SiteId(self): # Long
		return self.get_query_params().get('SiteId')

	def set_SiteId(self, SiteId):  # Long
		self.add_query_param('SiteId', SiteId)
	def get_PreQueueStartTime(self): # String
		return self.get_query_params().get('PreQueueStartTime')

	def set_PreQueueStartTime(self, PreQueueStartTime):  # String
		self.add_query_param('PreQueueStartTime', PreQueueStartTime)
	def get_NewUsersPerMinute(self): # String
		return self.get_query_params().get('NewUsersPerMinute')

	def set_NewUsersPerMinute(self, NewUsersPerMinute):  # String
		self.add_query_param('NewUsersPerMinute', NewUsersPerMinute)
	def get_CustomPageHtml(self): # String
		return self.get_query_params().get('CustomPageHtml')

	def set_CustomPageHtml(self, CustomPageHtml):  # String
		self.add_query_param('CustomPageHtml', CustomPageHtml)
	def get_PreQueueEnable(self): # String
		return self.get_query_params().get('PreQueueEnable')

	def set_PreQueueEnable(self, PreQueueEnable):  # String
		self.add_query_param('PreQueueEnable', PreQueueEnable)
