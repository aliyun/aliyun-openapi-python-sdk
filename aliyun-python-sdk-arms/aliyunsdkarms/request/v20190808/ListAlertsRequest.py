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

class ListAlertsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'ListAlerts','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Severity(self): # String
		return self.get_query_params().get('Severity')

	def set_Severity(self, Severity):  # String
		self.add_query_param('Severity', Severity)
	def get_IntegrationType(self): # String
		return self.get_query_params().get('IntegrationType')

	def set_IntegrationType(self, IntegrationType):  # String
		self.add_query_param('IntegrationType', IntegrationType)
	def get_AlertName(self): # String
		return self.get_query_params().get('AlertName')

	def set_AlertName(self, AlertName):  # String
		self.add_query_param('AlertName', AlertName)
	def get_ShowActivities(self): # Boolean
		return self.get_query_params().get('ShowActivities')

	def set_ShowActivities(self, ShowActivities):  # Boolean
		self.add_query_param('ShowActivities', ShowActivities)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_DispatchRuleId(self): # Long
		return self.get_query_params().get('DispatchRuleId')

	def set_DispatchRuleId(self, DispatchRuleId):  # Long
		self.add_query_param('DispatchRuleId', DispatchRuleId)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_ShowEvents(self): # Boolean
		return self.get_query_params().get('ShowEvents')

	def set_ShowEvents(self, ShowEvents):  # Boolean
		self.add_query_param('ShowEvents', ShowEvents)
	def get_Size(self): # Long
		return self.get_query_params().get('Size')

	def set_Size(self, Size):  # Long
		self.add_query_param('Size', Size)
	def get_State(self): # Long
		return self.get_query_params().get('State')

	def set_State(self, State):  # Long
		self.add_query_param('State', State)
	def get_Page(self): # Long
		return self.get_query_params().get('Page')

	def set_Page(self, Page):  # Long
		self.add_query_param('Page', Page)
