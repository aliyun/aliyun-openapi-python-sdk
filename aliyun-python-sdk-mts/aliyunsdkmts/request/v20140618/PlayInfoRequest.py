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
from aliyunsdkmts.endpoint import endpoint_data

class PlayInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'PlayInfo')
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

	def get_Rand(self):
		return self.get_query_params().get('Rand')

	def set_Rand(self,Rand):
		self.add_query_param('Rand',Rand)

	def get_AuthTimeout(self):
		return self.get_query_params().get('AuthTimeout')

	def set_AuthTimeout(self,AuthTimeout):
		self.add_query_param('AuthTimeout',AuthTimeout)

	def get_PlayDomain(self):
		return self.get_query_params().get('PlayDomain')

	def set_PlayDomain(self,PlayDomain):
		self.add_query_param('PlayDomain',PlayDomain)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_HlsUriToken(self):
		return self.get_query_params().get('HlsUriToken')

	def set_HlsUriToken(self,HlsUriToken):
		self.add_query_param('HlsUriToken',HlsUriToken)

	def get_Terminal(self):
		return self.get_query_params().get('Terminal')

	def set_Terminal(self,Terminal):
		self.add_query_param('Terminal',Terminal)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_MediaId(self):
		return self.get_query_params().get('MediaId')

	def set_MediaId(self,MediaId):
		self.add_query_param('MediaId',MediaId)

	def get_AuthInfo(self):
		return self.get_query_params().get('AuthInfo')

	def set_AuthInfo(self,AuthInfo):
		self.add_query_param('AuthInfo',AuthInfo)