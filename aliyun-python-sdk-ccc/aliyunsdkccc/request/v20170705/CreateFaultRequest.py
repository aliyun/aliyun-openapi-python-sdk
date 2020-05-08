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
from aliyunsdkccc.endpoint import endpoint_data

class CreateFaultRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'CreateFault')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AgentOssFileName(self):
		return self.get_query_params().get('AgentOssFileName')

	def set_AgentOssFileName(self,AgentOssFileName):
		self.add_query_param('AgentOssFileName',AgentOssFileName)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_OperatingSystemVersion(self):
		return self.get_query_params().get('OperatingSystemVersion')

	def set_OperatingSystemVersion(self,OperatingSystemVersion):
		self.add_query_param('OperatingSystemVersion',OperatingSystemVersion)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_MicrophoneList(self):
		return self.get_query_params().get('MicrophoneList')

	def set_MicrophoneList(self,MicrophoneList):
		self.add_query_param('MicrophoneList',MicrophoneList)

	def get_ClientPort(self):
		return self.get_query_params().get('ClientPort')

	def set_ClientPort(self,ClientPort):
		self.add_query_param('ClientPort',ClientPort)

	def get_CustomFilePath(self):
		return self.get_query_params().get('CustomFilePath')

	def set_CustomFilePath(self,CustomFilePath):
		self.add_query_param('CustomFilePath',CustomFilePath)

	def get_ClientIp(self):
		return self.get_query_params().get('ClientIp')

	def set_ClientIp(self,ClientIp):
		self.add_query_param('ClientIp',ClientIp)

	def get_SpeakerList(self):
		return self.get_query_params().get('SpeakerList')

	def set_SpeakerList(self,SpeakerList):
		self.add_query_param('SpeakerList',SpeakerList)

	def get_AgentId(self):
		return self.get_query_params().get('AgentId')

	def set_AgentId(self,AgentId):
		self.add_query_param('AgentId',AgentId)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_SpeakerEquipment(self):
		return self.get_query_params().get('SpeakerEquipment')

	def set_SpeakerEquipment(self,SpeakerEquipment):
		self.add_query_param('SpeakerEquipment',SpeakerEquipment)

	def get_ServicePort(self):
		return self.get_query_params().get('ServicePort')

	def set_ServicePort(self,ServicePort):
		self.add_query_param('ServicePort',ServicePort)

	def get_ServiceIp(self):
		return self.get_query_params().get('ServiceIp')

	def set_ServiceIp(self,ServiceIp):
		self.add_query_param('ServiceIp',ServiceIp)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_AgentFilePath(self):
		return self.get_query_params().get('AgentFilePath')

	def set_AgentFilePath(self,AgentFilePath):
		self.add_query_param('AgentFilePath',AgentFilePath)

	def get_ConnectId(self):
		return self.get_query_params().get('ConnectId')

	def set_ConnectId(self,ConnectId):
		self.add_query_param('ConnectId',ConnectId)

	def get_CustomOssFileName(self):
		return self.get_query_params().get('CustomOssFileName')

	def set_CustomOssFileName(self,CustomOssFileName):
		self.add_query_param('CustomOssFileName',CustomOssFileName)

	def get_MicrophoneEquipment(self):
		return self.get_query_params().get('MicrophoneEquipment')

	def set_MicrophoneEquipment(self,MicrophoneEquipment):
		self.add_query_param('MicrophoneEquipment',MicrophoneEquipment)

	def get_BrowserVersion(self):
		return self.get_query_params().get('BrowserVersion')

	def set_BrowserVersion(self,BrowserVersion):
		self.add_query_param('BrowserVersion',BrowserVersion)