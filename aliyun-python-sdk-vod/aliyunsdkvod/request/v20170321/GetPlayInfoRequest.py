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
from aliyunsdkvod.endpoint import endpoint_data

class GetPlayInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'GetPlayInfo','vod')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Formats(self):
		return self.get_query_params().get('Formats')

	def set_Formats(self,Formats):
		self.add_query_param('Formats',Formats)

	def get_ReAuthInfo(self):
		return self.get_query_params().get('ReAuthInfo')

	def set_ReAuthInfo(self,ReAuthInfo):
		self.add_query_param('ReAuthInfo',ReAuthInfo)

	def get_PlayConfig(self):
		return self.get_query_params().get('PlayConfig')

	def set_PlayConfig(self,PlayConfig):
		self.add_query_param('PlayConfig',PlayConfig)

	def get_OutputType(self):
		return self.get_query_params().get('OutputType')

	def set_OutputType(self,OutputType):
		self.add_query_param('OutputType',OutputType)

	def get_Definition(self):
		return self.get_query_params().get('Definition')

	def set_Definition(self,Definition):
		self.add_query_param('Definition',Definition)

	def get_AuthTimeout(self):
		return self.get_query_params().get('AuthTimeout')

	def set_AuthTimeout(self,AuthTimeout):
		self.add_query_param('AuthTimeout',AuthTimeout)

	def get_StreamType(self):
		return self.get_query_params().get('StreamType')

	def set_StreamType(self,StreamType):
		self.add_query_param('StreamType',StreamType)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_VideoId(self):
		return self.get_query_params().get('VideoId')

	def set_VideoId(self,VideoId):
		self.add_query_param('VideoId',VideoId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResultType(self):
		return self.get_query_params().get('ResultType')

	def set_ResultType(self,ResultType):
		self.add_query_param('ResultType',ResultType)