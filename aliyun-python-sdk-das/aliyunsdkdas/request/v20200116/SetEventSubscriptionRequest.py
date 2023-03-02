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
from aliyunsdkdas.endpoint import endpoint_data

class SetEventSubscriptionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'SetEventSubscription')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ContactGroupName(self): # String
		return self.get_query_params().get('ContactGroupName')

	def set_ContactGroupName(self, ContactGroupName):  # String
		self.add_query_param('ContactGroupName', ContactGroupName)
	def get_ContactName(self): # String
		return self.get_query_params().get('ContactName')

	def set_ContactName(self, ContactName):  # String
		self.add_query_param('ContactName', ContactName)
	def get_DispatchRule(self): # String
		return self.get_query_params().get('DispatchRule')

	def set_DispatchRule(self, DispatchRule):  # String
		self.add_query_param('DispatchRule', DispatchRule)
	def get_ChannelType(self): # String
		return self.get_query_params().get('ChannelType')

	def set_ChannelType(self, ChannelType):  # String
		self.add_query_param('ChannelType', ChannelType)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Severity(self): # String
		return self.get_query_params().get('Severity')

	def set_Severity(self, Severity):  # String
		self.add_query_param('Severity', Severity)
	def get_Level(self): # String
		return self.get_query_params().get('Level')

	def set_Level(self, Level):  # String
		self.add_query_param('Level', Level)
	def get_Active(self): # String
		return self.get_query_params().get('Active')

	def set_Active(self, Active):  # String
		self.add_query_param('Active', Active)
	def get_MinInterval(self): # String
		return self.get_query_params().get('MinInterval')

	def set_MinInterval(self, MinInterval):  # String
		self.add_query_param('MinInterval', MinInterval)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_EventContext(self): # String
		return self.get_query_params().get('EventContext')

	def set_EventContext(self, EventContext):  # String
		self.add_query_param('EventContext', EventContext)
