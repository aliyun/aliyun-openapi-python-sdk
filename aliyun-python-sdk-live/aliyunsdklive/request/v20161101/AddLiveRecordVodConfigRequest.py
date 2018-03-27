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
class AddLiveRecordVodConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'AddLiveRecordVodConfig','live')

	def get_AppName(self):
		return self.get_query_params().get('AppName')

	def set_AppName(self,AppName):
		self.add_query_param('AppName',AppName)

	def get_AutoCompose(self):
		return self.get_query_params().get('AutoCompose')

	def set_AutoCompose(self,AutoCompose):
		self.add_query_param('AutoCompose',AutoCompose)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_CycleDuration(self):
		return self.get_query_params().get('CycleDuration')

	def set_CycleDuration(self,CycleDuration):
		self.add_query_param('CycleDuration',CycleDuration)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ComposeVodTranscodeGroupId(self):
		return self.get_query_params().get('ComposeVodTranscodeGroupId')

	def set_ComposeVodTranscodeGroupId(self,ComposeVodTranscodeGroupId):
		self.add_query_param('ComposeVodTranscodeGroupId',ComposeVodTranscodeGroupId)

	def get_StreamName(self):
		return self.get_query_params().get('StreamName')

	def set_StreamName(self,StreamName):
		self.add_query_param('StreamName',StreamName)

	def get_VodTranscodeGroupId(self):
		return self.get_query_params().get('VodTranscodeGroupId')

	def set_VodTranscodeGroupId(self,VodTranscodeGroupId):
		self.add_query_param('VodTranscodeGroupId',VodTranscodeGroupId)