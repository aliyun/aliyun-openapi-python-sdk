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
from aliyunsdkrtc.endpoint import endpoint_data

class UpdateAutoLiveStreamRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rtc', '2018-01-11', 'UpdateAutoLiveStreamRule')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_ChannelIdPrefixess(self): # RepeatList
		return self.get_query_params().get('ChannelIdPrefixes')

	def set_ChannelIdPrefixess(self, ChannelIdPrefixes):  # RepeatList
		for depth1 in range(len(ChannelIdPrefixes)):
			self.add_query_param('ChannelIdPrefixes.' + str(depth1 + 1), ChannelIdPrefixes[depth1])
	def get_PlayDomain(self): # String
		return self.get_query_params().get('PlayDomain')

	def set_PlayDomain(self, PlayDomain):  # String
		self.add_query_param('PlayDomain', PlayDomain)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_CallBack(self): # String
		return self.get_query_params().get('CallBack')

	def set_CallBack(self, CallBack):  # String
		self.add_query_param('CallBack', CallBack)
	def get_MediaEncode(self): # Integer
		return self.get_query_params().get('MediaEncode')

	def set_MediaEncode(self, MediaEncode):  # Integer
		self.add_query_param('MediaEncode', MediaEncode)
	def get_RuleId(self): # Integer
		return self.get_query_params().get('RuleId')

	def set_RuleId(self, RuleId):  # Integer
		self.add_query_param('RuleId', RuleId)
	def get_ChannelIdss(self): # RepeatList
		return self.get_query_params().get('ChannelIds')

	def set_ChannelIdss(self, ChannelIds):  # RepeatList
		for depth1 in range(len(ChannelIds)):
			self.add_query_param('ChannelIds.' + str(depth1 + 1), ChannelIds[depth1])
