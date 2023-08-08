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

class UpdateLiveAppRecordConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'UpdateLiveAppRecordConfig','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OssEndpoint(self): # String
		return self.get_query_params().get('OssEndpoint')

	def set_OssEndpoint(self, OssEndpoint):  # String
		self.add_query_param('OssEndpoint', OssEndpoint)
	def get_DelayTime(self): # Integer
		return self.get_query_params().get('DelayTime')

	def set_DelayTime(self, DelayTime):  # Integer
		self.add_query_param('DelayTime', DelayTime)
	def get_TranscodeTemplatess(self): # RepeatList
		return self.get_query_params().get('TranscodeTemplates')

	def set_TranscodeTemplatess(self, TranscodeTemplates):  # RepeatList
		for depth1 in range(len(TranscodeTemplates)):
			self.add_query_param('TranscodeTemplates.' + str(depth1 + 1), TranscodeTemplates[depth1])
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_TranscodeRecordFormats(self): # RepeatList
		return self.get_query_params().get('TranscodeRecordFormat')

	def set_TranscodeRecordFormats(self, TranscodeRecordFormat):  # RepeatList
		for depth1 in range(len(TranscodeRecordFormat)):
			if TranscodeRecordFormat[depth1].get('SliceDuration') is not None:
				self.add_query_param('TranscodeRecordFormat.' + str(depth1 + 1) + '.SliceDuration', TranscodeRecordFormat[depth1].get('SliceDuration'))
			if TranscodeRecordFormat[depth1].get('Format') is not None:
				self.add_query_param('TranscodeRecordFormat.' + str(depth1 + 1) + '.Format', TranscodeRecordFormat[depth1].get('Format'))
			if TranscodeRecordFormat[depth1].get('CycleDuration') is not None:
				self.add_query_param('TranscodeRecordFormat.' + str(depth1 + 1) + '.CycleDuration', TranscodeRecordFormat[depth1].get('CycleDuration'))
	def get_OnDemand(self): # Integer
		return self.get_query_params().get('OnDemand')

	def set_OnDemand(self, OnDemand):  # Integer
		self.add_query_param('OnDemand', OnDemand)
	def get_StreamName(self): # String
		return self.get_query_params().get('StreamName')

	def set_StreamName(self, StreamName):  # String
		self.add_query_param('StreamName', StreamName)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_RecordFormats(self): # RepeatList
		return self.get_query_params().get('RecordFormat')

	def set_RecordFormats(self, RecordFormat):  # RepeatList
		for depth1 in range(len(RecordFormat)):
			if RecordFormat[depth1].get('SliceDuration') is not None:
				self.add_query_param('RecordFormat.' + str(depth1 + 1) + '.SliceDuration', RecordFormat[depth1].get('SliceDuration'))
			if RecordFormat[depth1].get('Format') is not None:
				self.add_query_param('RecordFormat.' + str(depth1 + 1) + '.Format', RecordFormat[depth1].get('Format'))
			if RecordFormat[depth1].get('CycleDuration') is not None:
				self.add_query_param('RecordFormat.' + str(depth1 + 1) + '.CycleDuration', RecordFormat[depth1].get('CycleDuration'))
