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

class AddLiveAppRecordConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'AddLiveAppRecordConfig','live')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OssEndpoint(self):
		return self.get_query_params().get('OssEndpoint')

	def set_OssEndpoint(self,OssEndpoint):
		self.add_query_param('OssEndpoint',OssEndpoint)

	def get_TranscodeTemplatess(self):
		return self.get_query_params().get('TranscodeTemplates')

	def set_TranscodeTemplatess(self, TranscodeTemplatess):
		for depth1 in range(len(TranscodeTemplatess)):
			if TranscodeTemplatess[depth1] is not None:
				self.add_query_param('TranscodeTemplates.' + str(depth1 + 1) , TranscodeTemplatess[depth1])

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_AppName(self):
		return self.get_query_params().get('AppName')

	def set_AppName(self,AppName):
		self.add_query_param('AppName',AppName)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_TranscodeRecordFormats(self):
		return self.get_query_params().get('TranscodeRecordFormat')

	def set_TranscodeRecordFormats(self, TranscodeRecordFormats):
		for depth1 in range(len(TranscodeRecordFormats)):
			if TranscodeRecordFormats[depth1].get('SliceOssObjectPrefix') is not None:
				self.add_query_param('TranscodeRecordFormat.' + str(depth1 + 1) + '.SliceOssObjectPrefix', TranscodeRecordFormats[depth1].get('SliceOssObjectPrefix'))
			if TranscodeRecordFormats[depth1].get('SliceDuration') is not None:
				self.add_query_param('TranscodeRecordFormat.' + str(depth1 + 1) + '.SliceDuration', TranscodeRecordFormats[depth1].get('SliceDuration'))
			if TranscodeRecordFormats[depth1].get('Format') is not None:
				self.add_query_param('TranscodeRecordFormat.' + str(depth1 + 1) + '.Format', TranscodeRecordFormats[depth1].get('Format'))
			if TranscodeRecordFormats[depth1].get('OssObjectPrefix') is not None:
				self.add_query_param('TranscodeRecordFormat.' + str(depth1 + 1) + '.OssObjectPrefix', TranscodeRecordFormats[depth1].get('OssObjectPrefix'))
			if TranscodeRecordFormats[depth1].get('CycleDuration') is not None:
				self.add_query_param('TranscodeRecordFormat.' + str(depth1 + 1) + '.CycleDuration', TranscodeRecordFormats[depth1].get('CycleDuration'))

	def get_OnDemand(self):
		return self.get_query_params().get('OnDemand')

	def set_OnDemand(self,OnDemand):
		self.add_query_param('OnDemand',OnDemand)

	def get_StreamName(self):
		return self.get_query_params().get('StreamName')

	def set_StreamName(self,StreamName):
		self.add_query_param('StreamName',StreamName)

	def get_OssBucket(self):
		return self.get_query_params().get('OssBucket')

	def set_OssBucket(self,OssBucket):
		self.add_query_param('OssBucket',OssBucket)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_RecordFormats(self):
		return self.get_query_params().get('RecordFormat')

	def set_RecordFormats(self, RecordFormats):
		for depth1 in range(len(RecordFormats)):
			if RecordFormats[depth1].get('SliceOssObjectPrefix') is not None:
				self.add_query_param('RecordFormat.' + str(depth1 + 1) + '.SliceOssObjectPrefix', RecordFormats[depth1].get('SliceOssObjectPrefix'))
			if RecordFormats[depth1].get('SliceDuration') is not None:
				self.add_query_param('RecordFormat.' + str(depth1 + 1) + '.SliceDuration', RecordFormats[depth1].get('SliceDuration'))
			if RecordFormats[depth1].get('Format') is not None:
				self.add_query_param('RecordFormat.' + str(depth1 + 1) + '.Format', RecordFormats[depth1].get('Format'))
			if RecordFormats[depth1].get('OssObjectPrefix') is not None:
				self.add_query_param('RecordFormat.' + str(depth1 + 1) + '.OssObjectPrefix', RecordFormats[depth1].get('OssObjectPrefix'))
			if RecordFormats[depth1].get('CycleDuration') is not None:
				self.add_query_param('RecordFormat.' + str(depth1 + 1) + '.CycleDuration', RecordFormats[depth1].get('CycleDuration'))