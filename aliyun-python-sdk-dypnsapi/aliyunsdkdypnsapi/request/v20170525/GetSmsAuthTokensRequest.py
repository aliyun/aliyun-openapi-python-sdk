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
from aliyunsdkdypnsapi.endpoint import endpoint_data

class GetSmsAuthTokensRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dypnsapi', '2017-05-25', 'GetSmsAuthTokens')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_BundleId(self): # String
		return self.get_query_params().get('BundleId')

	def set_BundleId(self, BundleId):  # String
		self.add_query_param('BundleId', BundleId)
	def get_SignName(self): # String
		return self.get_query_params().get('SignName')

	def set_SignName(self, SignName):  # String
		self.add_query_param('SignName', SignName)
	def get_SceneCode(self): # String
		return self.get_query_params().get('SceneCode')

	def set_SceneCode(self, SceneCode):  # String
		self.add_query_param('SceneCode', SceneCode)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_SmsCodeExpire(self): # Integer
		return self.get_query_params().get('SmsCodeExpire')

	def set_SmsCodeExpire(self, SmsCodeExpire):  # Integer
		self.add_query_param('SmsCodeExpire', SmsCodeExpire)
	def get_PackageName(self): # String
		return self.get_query_params().get('PackageName')

	def set_PackageName(self, PackageName):  # String
		self.add_query_param('PackageName', PackageName)
	def get_OsType(self): # String
		return self.get_query_params().get('OsType')

	def set_OsType(self, OsType):  # String
		self.add_query_param('OsType', OsType)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SmsTemplateCode(self): # String
		return self.get_query_params().get('SmsTemplateCode')

	def set_SmsTemplateCode(self, SmsTemplateCode):  # String
		self.add_query_param('SmsTemplateCode', SmsTemplateCode)
	def get_Expire(self): # Long
		return self.get_query_params().get('Expire')

	def set_Expire(self, Expire):  # Long
		self.add_query_param('Expire', Expire)
