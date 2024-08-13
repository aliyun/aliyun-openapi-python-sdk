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
from aliyunsdklive.endpoint import endpoint_data

class CreateRtcAsrTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'CreateRtcAsrTask','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AuthKey(self): # String
		return self.get_query_params().get('AuthKey')

	def set_AuthKey(self, AuthKey):  # String
		self.add_query_param('AuthKey', AuthKey)
	def get_Language(self): # String
		return self.get_query_params().get('Language')

	def set_Language(self, Language):  # String
		self.add_query_param('Language', Language)
	def get_Mode(self): # String
		return self.get_query_params().get('Mode')

	def set_Mode(self, Mode):  # String
		self.add_query_param('Mode', Mode)
	def get_TranslateEnabled(self): # Boolean
		return self.get_query_params().get('TranslateEnabled')

	def set_TranslateEnabled(self, TranslateEnabled):  # Boolean
		self.add_query_param('TranslateEnabled', TranslateEnabled)
	def get_StreamURL(self): # String
		return self.get_query_params().get('StreamURL')

	def set_StreamURL(self, StreamURL):  # String
		self.add_query_param('StreamURL', StreamURL)
	def get_TargetLanguages(self): # String
		return self.get_query_params().get('TargetLanguages')

	def set_TargetLanguages(self, TargetLanguages):  # String
		self.add_query_param('TargetLanguages', TargetLanguages)
	def get_AutoTerminateEnabled(self): # Boolean
		return self.get_query_params().get('AutoTerminateEnabled')

	def set_AutoTerminateEnabled(self, AutoTerminateEnabled):  # Boolean
		self.add_query_param('AutoTerminateEnabled', AutoTerminateEnabled)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_RtcUserId(self): # String
		return self.get_query_params().get('RtcUserId')

	def set_RtcUserId(self, RtcUserId):  # String
		self.add_query_param('RtcUserId', RtcUserId)
	def get_ReportInterval(self): # Long
		return self.get_query_params().get('ReportInterval')

	def set_ReportInterval(self, ReportInterval):  # Long
		self.add_query_param('ReportInterval', ReportInterval)
	def get_AutoTerminateDelay(self): # Long
		return self.get_query_params().get('AutoTerminateDelay')

	def set_AutoTerminateDelay(self, AutoTerminateDelay):  # Long
		self.add_query_param('AutoTerminateDelay', AutoTerminateDelay)
	def get_SDKAppID(self): # String
		return self.get_query_params().get('SDKAppID')

	def set_SDKAppID(self, SDKAppID):  # String
		self.add_query_param('SDKAppID', SDKAppID)
	def get_CallbackURL(self): # String
		return self.get_query_params().get('CallbackURL')

	def set_CallbackURL(self, CallbackURL):  # String
		self.add_query_param('CallbackURL', CallbackURL)
	def get_ChannelID(self): # String
		return self.get_query_params().get('ChannelID')

	def set_ChannelID(self, ChannelID):  # String
		self.add_query_param('ChannelID', ChannelID)
