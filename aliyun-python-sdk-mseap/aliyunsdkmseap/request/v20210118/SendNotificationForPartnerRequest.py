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
import json

class SendNotificationForPartnerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mseap', '2021-01-18', 'SendNotificationForPartner')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_TrackId(self): # String
		return self.get_query_params().get('TrackId')

	def set_TrackId(self, TrackId):  # String
		self.add_query_param('TrackId', TrackId)
	def get_SmartSubChannels(self): # Array
		return self.get_query_params().get('SmartSubChannels')

	def set_SmartSubChannels(self, SmartSubChannels):  # Array
		self.add_query_param("SmartSubChannels", json.dumps(SmartSubChannels))
	def get_ChannelType(self): # String
		return self.get_query_params().get('ChannelType')

	def set_ChannelType(self, ChannelType):  # String
		self.add_query_param('ChannelType', ChannelType)
	def get_NotifyType(self): # String
		return self.get_query_params().get('NotifyType')

	def set_NotifyType(self, NotifyType):  # String
		self.add_query_param('NotifyType', NotifyType)
	def get_NotifycationEventType(self): # String
		return self.get_query_params().get('NotifycationEventType')

	def set_NotifycationEventType(self, NotifycationEventType):  # String
		self.add_query_param('NotifycationEventType', NotifycationEventType)
	def get_SendTarget(self): # String
		return self.get_query_params().get('SendTarget')

	def set_SendTarget(self, SendTarget):  # String
		self.add_query_param('SendTarget', SendTarget)
	def get_BizId(self): # String
		return self.get_query_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_query_param('BizId', BizId)
	def get_ParamMap(self): # Map
		return self.get_query_params().get('ParamMap')

	def set_ParamMap(self, ParamMap):  # Map
		self.add_query_param("ParamMap", json.dumps(ParamMap))
