# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateNetworkQuotaRequestRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Netana', '2018-10-18', 'CreateNetworkQuotaRequest','Netana')

	def get_RequestReason(self):
		return self.get_query_params().get('RequestReason')

	def set_RequestReason(self,RequestReason):
		self.add_query_param('RequestReason',RequestReason)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Product(self):
		return self.get_query_params().get('Product')

	def set_Product(self,Product):
		self.add_query_param('Product',Product)

	def get_QuotaPublicityName(self):
		return self.get_query_params().get('QuotaPublicityName')

	def set_QuotaPublicityName(self,QuotaPublicityName):
		self.add_query_param('QuotaPublicityName',QuotaPublicityName)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_RequestQuantity(self):
		return self.get_query_params().get('RequestQuantity')

	def set_RequestQuantity(self,RequestQuantity):
		self.add_query_param('RequestQuantity',RequestQuantity)

	def get_MobilePhone(self):
		return self.get_query_params().get('MobilePhone')

	def set_MobilePhone(self,MobilePhone):
		self.add_query_param('MobilePhone',MobilePhone)

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)

	def get_Email(self):
		return self.get_query_params().get('Email')

	def set_Email(self,Email):
		self.add_query_param('Email',Email)