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

class ModifyCasterVideoResourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'ModifyCasterVideoResource','live')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_EndOffset(self):
		return self.get_query_params().get('EndOffset')

	def set_EndOffset(self,EndOffset):
		self.add_query_param('EndOffset',EndOffset)

	def get_MaterialId(self):
		return self.get_query_params().get('MaterialId')

	def set_MaterialId(self,MaterialId):
		self.add_query_param('MaterialId',MaterialId)

	def get_ResourceId(self):
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self,ResourceId):
		self.add_query_param('ResourceId',ResourceId)

	def get_VodUrl(self):
		return self.get_query_params().get('VodUrl')

	def set_VodUrl(self,VodUrl):
		self.add_query_param('VodUrl',VodUrl)

	def get_CasterId(self):
		return self.get_query_params().get('CasterId')

	def set_CasterId(self,CasterId):
		self.add_query_param('CasterId',CasterId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_BeginOffset(self):
		return self.get_query_params().get('BeginOffset')

	def set_BeginOffset(self,BeginOffset):
		self.add_query_param('BeginOffset',BeginOffset)

	def get_LiveStreamUrl(self):
		return self.get_query_params().get('LiveStreamUrl')

	def set_LiveStreamUrl(self,LiveStreamUrl):
		self.add_query_param('LiveStreamUrl',LiveStreamUrl)

	def get_PtsCallbackInterval(self):
		return self.get_query_params().get('PtsCallbackInterval')

	def set_PtsCallbackInterval(self,PtsCallbackInterval):
		self.add_query_param('PtsCallbackInterval',PtsCallbackInterval)

	def get_ResourceName(self):
		return self.get_query_params().get('ResourceName')

	def set_ResourceName(self,ResourceName):
		self.add_query_param('ResourceName',ResourceName)

	def get_RepeatNum(self):
		return self.get_query_params().get('RepeatNum')

	def set_RepeatNum(self,RepeatNum):
		self.add_query_param('RepeatNum',RepeatNum)