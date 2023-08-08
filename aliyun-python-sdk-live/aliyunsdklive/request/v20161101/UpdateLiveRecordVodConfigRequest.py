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

class UpdateLiveRecordVodConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'UpdateLiveRecordVodConfig','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AutoCompose(self): # String
		return self.get_query_params().get('AutoCompose')

	def set_AutoCompose(self, AutoCompose):  # String
		self.add_query_param('AutoCompose', AutoCompose)
	def get_ComposeVodTranscodeGroupId(self): # String
		return self.get_query_params().get('ComposeVodTranscodeGroupId')

	def set_ComposeVodTranscodeGroupId(self, ComposeVodTranscodeGroupId):  # String
		self.add_query_param('ComposeVodTranscodeGroupId', ComposeVodTranscodeGroupId)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_OnDemand(self): # Integer
		return self.get_query_params().get('OnDemand')

	def set_OnDemand(self, OnDemand):  # Integer
		self.add_query_param('OnDemand', OnDemand)
	def get_StreamName(self): # String
		return self.get_query_params().get('StreamName')

	def set_StreamName(self, StreamName):  # String
		self.add_query_param('StreamName', StreamName)
	def get_VodTranscodeGroupId(self): # String
		return self.get_query_params().get('VodTranscodeGroupId')

	def set_VodTranscodeGroupId(self, VodTranscodeGroupId):  # String
		self.add_query_param('VodTranscodeGroupId', VodTranscodeGroupId)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_CycleDuration(self): # Integer
		return self.get_query_params().get('CycleDuration')

	def set_CycleDuration(self, CycleDuration):  # Integer
		self.add_query_param('CycleDuration', CycleDuration)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
