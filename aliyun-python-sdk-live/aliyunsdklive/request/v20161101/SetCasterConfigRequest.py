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

class SetCasterConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'SetCasterConfig','live')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ChannelEnable(self):
		return self.get_query_params().get('ChannelEnable')

	def set_ChannelEnable(self,ChannelEnable):
		self.add_query_param('ChannelEnable',ChannelEnable)

	def get_ProgramEffect(self):
		return self.get_query_params().get('ProgramEffect')

	def set_ProgramEffect(self,ProgramEffect):
		self.add_query_param('ProgramEffect',ProgramEffect)

	def get_ProgramName(self):
		return self.get_query_params().get('ProgramName')

	def set_ProgramName(self,ProgramName):
		self.add_query_param('ProgramName',ProgramName)

	def get_RecordConfig(self):
		return self.get_query_params().get('RecordConfig')

	def set_RecordConfig(self,RecordConfig):
		self.add_query_param('RecordConfig',RecordConfig)

	def get_UrgentMaterialId(self):
		return self.get_query_params().get('UrgentMaterialId')

	def set_UrgentMaterialId(self,UrgentMaterialId):
		self.add_query_param('UrgentMaterialId',UrgentMaterialId)

	def get_TranscodeConfig(self):
		return self.get_query_params().get('TranscodeConfig')

	def set_TranscodeConfig(self,TranscodeConfig):
		self.add_query_param('TranscodeConfig',TranscodeConfig)

	def get_CasterName(self):
		return self.get_query_params().get('CasterName')

	def set_CasterName(self,CasterName):
		self.add_query_param('CasterName',CasterName)

	def get_SideOutputUrl(self):
		return self.get_query_params().get('SideOutputUrl')

	def set_SideOutputUrl(self,SideOutputUrl):
		self.add_query_param('SideOutputUrl',SideOutputUrl)

	def get_CasterId(self):
		return self.get_query_params().get('CasterId')

	def set_CasterId(self,CasterId):
		self.add_query_param('CasterId',CasterId)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Delay(self):
		return self.get_query_params().get('Delay')

	def set_Delay(self,Delay):
		self.add_query_param('Delay',Delay)

	def get_CallbackUrl(self):
		return self.get_query_params().get('CallbackUrl')

	def set_CallbackUrl(self,CallbackUrl):
		self.add_query_param('CallbackUrl',CallbackUrl)