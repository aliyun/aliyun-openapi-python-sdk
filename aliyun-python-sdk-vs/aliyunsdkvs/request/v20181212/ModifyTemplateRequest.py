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
from aliyunsdkvs.endpoint import endpoint_data

class ModifyTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vs', '2018-12-12', 'ModifyTemplate','vs')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_HlsTs(self):
		return self.get_query_params().get('HlsTs')

	def set_HlsTs(self,HlsTs):
		self.add_query_param('HlsTs',HlsTs)

	def get_OssEndpoint(self):
		return self.get_query_params().get('OssEndpoint')

	def set_OssEndpoint(self,OssEndpoint):
		self.add_query_param('OssEndpoint',OssEndpoint)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_OssFilePrefix(self):
		return self.get_query_params().get('OssFilePrefix')

	def set_OssFilePrefix(self,OssFilePrefix):
		self.add_query_param('OssFilePrefix',OssFilePrefix)

	def get_JpgOverwrite(self):
		return self.get_query_params().get('JpgOverwrite')

	def set_JpgOverwrite(self,JpgOverwrite):
		self.add_query_param('JpgOverwrite',JpgOverwrite)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_JpgOnDemand(self):
		return self.get_query_params().get('JpgOnDemand')

	def set_JpgOnDemand(self,JpgOnDemand):
		self.add_query_param('JpgOnDemand',JpgOnDemand)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_Retention(self):
		return self.get_query_params().get('Retention')

	def set_Retention(self,Retention):
		self.add_query_param('Retention',Retention)

	def get_HlsM3u8(self):
		return self.get_query_params().get('HlsM3u8')

	def set_HlsM3u8(self,HlsM3u8):
		self.add_query_param('HlsM3u8',HlsM3u8)

	def get_OssBucket(self):
		return self.get_query_params().get('OssBucket')

	def set_OssBucket(self,OssBucket):
		self.add_query_param('OssBucket',OssBucket)

	def get_TransConfigsJSON(self):
		return self.get_query_params().get('TransConfigsJSON')

	def set_TransConfigsJSON(self,TransConfigsJSON):
		self.add_query_param('TransConfigsJSON',TransConfigsJSON)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_Trigger(self):
		return self.get_query_params().get('Trigger')

	def set_Trigger(self,Trigger):
		self.add_query_param('Trigger',Trigger)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_JpgSequence(self):
		return self.get_query_params().get('JpgSequence')

	def set_JpgSequence(self,JpgSequence):
		self.add_query_param('JpgSequence',JpgSequence)

	def get_Mp4(self):
		return self.get_query_params().get('Mp4')

	def set_Mp4(self,Mp4):
		self.add_query_param('Mp4',Mp4)

	def get_Flv(self):
		return self.get_query_params().get('Flv')

	def set_Flv(self,Flv):
		self.add_query_param('Flv',Flv)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Callback(self):
		return self.get_query_params().get('Callback')

	def set_Callback(self,Callback):
		self.add_query_param('Callback',Callback)

	def get_Interval(self):
		return self.get_query_params().get('Interval')

	def set_Interval(self,Interval):
		self.add_query_param('Interval',Interval)

	def get_FileFormat(self):
		return self.get_query_params().get('FileFormat')

	def set_FileFormat(self,FileFormat):
		self.add_query_param('FileFormat',FileFormat)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)