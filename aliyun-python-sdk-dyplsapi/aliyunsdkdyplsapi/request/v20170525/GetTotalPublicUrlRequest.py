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
from aliyunsdkdyplsapi.endpoint import endpoint_data

class GetTotalPublicUrlRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyplsapi', '2017-05-25', 'GetTotalPublicUrl')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CallId(self):
		return self.get_query_params().get('CallId')

	def set_CallId(self,CallId):
		self.add_query_param('CallId',CallId)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_CheckSubs(self):
		return self.get_query_params().get('CheckSubs')

	def set_CheckSubs(self,CheckSubs):
		self.add_query_param('CheckSubs',CheckSubs)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_CallTime(self):
		return self.get_query_params().get('CallTime')

	def set_CallTime(self,CallTime):
		self.add_query_param('CallTime',CallTime)

	def get_PartnerKey(self):
		return self.get_query_params().get('PartnerKey')

	def set_PartnerKey(self,PartnerKey):
		self.add_query_param('PartnerKey',PartnerKey)