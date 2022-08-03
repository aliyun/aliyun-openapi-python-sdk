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
from aliyunsdkresourcemanager.endpoint import endpoint_data

class CreateResourceAccountRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceManager', '2020-03-31', 'CreateResourceAccount')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AccountNamePrefix(self): # String
		return self.get_query_params().get('AccountNamePrefix')

	def set_AccountNamePrefix(self, AccountNamePrefix):  # String
		self.add_query_param('AccountNamePrefix', AccountNamePrefix)
	def get_ParentFolderId(self): # String
		return self.get_query_params().get('ParentFolderId')

	def set_ParentFolderId(self, ParentFolderId):  # String
		self.add_query_param('ParentFolderId', ParentFolderId)
	def get_DisplayName(self): # String
		return self.get_query_params().get('DisplayName')

	def set_DisplayName(self, DisplayName):  # String
		self.add_query_param('DisplayName', DisplayName)
	def get_Tag(self): # Array
		return self.get_query_params().get('Tag')

	def set_Tag(self, Tag):  # Array
		for index1, value1 in enumerate(Tag):
			if value1.get('Value') is not None:
				self.add_query_param('Tag.' + str(index1 + 1) + '.Value', value1.get('Value'))
			if value1.get('Key') is not None:
				self.add_query_param('Tag.' + str(index1 + 1) + '.Key', value1.get('Key'))
	def get_PayerAccountId(self): # String
		return self.get_query_params().get('PayerAccountId')

	def set_PayerAccountId(self, PayerAccountId):  # String
		self.add_query_param('PayerAccountId', PayerAccountId)
