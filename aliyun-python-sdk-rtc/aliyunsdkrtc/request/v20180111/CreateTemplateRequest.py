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

class CreateTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rtc', '2018-01-11', 'CreateTemplate','rtc')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ServiceMode(self):
		return self.get_query_params().get('ServiceMode')

	def set_ServiceMode(self,ServiceMode):
		self.add_query_param('ServiceMode',ServiceMode)

	def get_LiveConfigs(self):
		return self.get_query_params().get('LiveConfigs')

	def set_LiveConfigs(self,LiveConfigs):
		for i in range(len(LiveConfigs)):	
			if LiveConfigs[i].get('DomainName') is not None:
				self.add_query_param('LiveConfig.' + str(i + 1) + '.DomainName' , LiveConfigs[i].get('DomainName'))
			if LiveConfigs[i].get('AppName') is not None:
				self.add_query_param('LiveConfig.' + str(i + 1) + '.AppName' , LiveConfigs[i].get('AppName'))


	def get_MediaConfig(self):
		return self.get_query_params().get('MediaConfig')

	def set_MediaConfig(self,MediaConfig):
		self.add_query_param('MediaConfig',MediaConfig)

	def get_MaxMixStreamCount(self):
		return self.get_query_params().get('MaxMixStreamCount')

	def set_MaxMixStreamCount(self,MaxMixStreamCount):
		self.add_query_param('MaxMixStreamCount',MaxMixStreamCount)

	def get_RecordConfigs(self):
		return self.get_query_params().get('RecordConfigs')

	def set_RecordConfigs(self,RecordConfigs):
		for i in range(len(RecordConfigs)):	
			if RecordConfigs[i].get('StorageType') is not None:
				self.add_query_param('RecordConfig.' + str(i + 1) + '.StorageType' , RecordConfigs[i].get('StorageType'))
			if RecordConfigs[i].get('FileFormat') is not None:
				self.add_query_param('RecordConfig.' + str(i + 1) + '.FileFormat' , RecordConfigs[i].get('FileFormat'))
			if RecordConfigs[i].get('OssEndPoint') is not None:
				self.add_query_param('RecordConfig.' + str(i + 1) + '.OssEndPoint' , RecordConfigs[i].get('OssEndPoint'))
			if RecordConfigs[i].get('OssBucket') is not None:
				self.add_query_param('RecordConfig.' + str(i + 1) + '.OssBucket' , RecordConfigs[i].get('OssBucket'))
			if RecordConfigs[i].get('VodTransCodeGroupId') is not None:
				self.add_query_param('RecordConfig.' + str(i + 1) + '.VodTransCodeGroupId' , RecordConfigs[i].get('VodTransCodeGroupId'))


	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_LayOuts(self):
		return self.get_query_params().get('LayOuts')

	def set_LayOuts(self,LayOuts):
		for i in range(len(LayOuts)):	
			if LayOuts[i].get('Color') is not None:
				self.add_query_param('LayOut.' + str(i + 1) + '.Color' , LayOuts[i].get('Color'))
			if LayOuts[i].get('CutMode') is not None:
				self.add_query_param('LayOut.' + str(i + 1) + '.CutMode' , LayOuts[i].get('CutMode'))
			if LayOuts[i].get('LayOutId') is not None:
				self.add_query_param('LayOut.' + str(i + 1) + '.LayOutId' , LayOuts[i].get('LayOutId'))


	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_CallBack(self):
		return self.get_query_params().get('CallBack')

	def set_CallBack(self,CallBack):
		self.add_query_param('CallBack',CallBack)

	def get_MixMode(self):
		return self.get_query_params().get('MixMode')

	def set_MixMode(self,MixMode):
		self.add_query_param('MixMode',MixMode)