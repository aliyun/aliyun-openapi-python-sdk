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
from aliyunsdknlb.endpoint import endpoint_data

class ListSystemSecurityPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Nlb', '2022-04-30', 'ListSystemSecurityPolicy','nlb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Channel(self): # String
		return self.get_body_params().get('Channel')

	def set_Channel(self, Channel):  # String
		self.add_body_params('Channel', Channel)
	def get_OwnerIdLoginEmail(self): # String
		return self.get_body_params().get('OwnerIdLoginEmail')

	def set_OwnerIdLoginEmail(self, OwnerIdLoginEmail):  # String
		self.add_body_params('OwnerIdLoginEmail', OwnerIdLoginEmail)
	def get_CallerBidLoginEmail(self): # String
		return self.get_body_params().get('CallerBidLoginEmail')

	def set_CallerBidLoginEmail(self, CallerBidLoginEmail):  # String
		self.add_body_params('CallerBidLoginEmail', CallerBidLoginEmail)
	def get_CallerUidLoginEmail(self): # String
		return self.get_body_params().get('CallerUidLoginEmail')

	def set_CallerUidLoginEmail(self, CallerUidLoginEmail):  # String
		self.add_body_params('CallerUidLoginEmail', CallerUidLoginEmail)
	def get_RequestContent(self): # String
		return self.get_body_params().get('RequestContent')

	def set_RequestContent(self, RequestContent):  # String
		self.add_body_params('RequestContent', RequestContent)
	def get_ResourceOwnerAccount(self): # String
		return self.get_body_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_body_params('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_body_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_body_params('OwnerAccount', OwnerAccount)
