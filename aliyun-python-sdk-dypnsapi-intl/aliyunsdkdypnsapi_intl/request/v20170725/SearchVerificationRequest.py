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

class SearchVerificationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dypnsapi-intl', '2017-07-25', 'SearchVerification')
		self.set_method('POST')

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_Code(self): # String
		return self.get_query_params().get('Code')

	def set_Code(self, Code):  # String
		self.add_query_param('Code', Code)
	def get_ServiceSid(self): # String
		return self.get_query_params().get('ServiceSid')

	def set_ServiceSid(self, ServiceSid):  # String
		self.add_query_param('ServiceSid', ServiceSid)
	def get_SendDate(self): # Long
		return self.get_query_params().get('SendDate')

	def set_SendDate(self, SendDate):  # Long
		self.add_query_param('SendDate', SendDate)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_VerificationId(self): # String
		return self.get_query_params().get('VerificationId')

	def set_VerificationId(self, VerificationId):  # String
		self.add_query_param('VerificationId', VerificationId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_CurrentPage(self): # Long
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Long
		self.add_query_param('CurrentPage', CurrentPage)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_To(self): # String
		return self.get_query_params().get('To')

	def set_To(self, To):  # String
		self.add_query_param('To', To)
