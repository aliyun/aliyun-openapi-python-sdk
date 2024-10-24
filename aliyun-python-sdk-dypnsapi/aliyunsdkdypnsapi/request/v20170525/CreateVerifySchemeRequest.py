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

class CreateVerifySchemeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dypnsapi', '2017-05-25', 'CreateVerifyScheme','dypnsapi')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_Origin(self): # String
		return self.get_query_params().get('Origin')

	def set_Origin(self, Origin):  # String
		self.add_query_param('Origin', Origin)
	def get_BundleId(self): # String
		return self.get_query_params().get('BundleId')

	def set_BundleId(self, BundleId):  # String
		self.add_query_param('BundleId', BundleId)
	def get_AuthType(self): # String
		return self.get_query_params().get('AuthType')

	def set_AuthType(self, AuthType):  # String
		self.add_query_param('AuthType', AuthType)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_IpWhiteList(self): # String
		return self.get_query_params().get('IpWhiteList')

	def set_IpWhiteList(self, IpWhiteList):  # String
		self.add_query_param('IpWhiteList', IpWhiteList)
	def get_Email(self): # String
		return self.get_query_params().get('Email')

	def set_Email(self, Email):  # String
		self.add_query_param('Email', Email)
	def get_HmSignName(self): # String
		return self.get_query_params().get('HmSignName')

	def set_HmSignName(self, HmSignName):  # String
		self.add_query_param('HmSignName', HmSignName)
	def get_PackSign(self): # String
		return self.get_query_params().get('PackSign')

	def set_PackSign(self, PackSign):  # String
		self.add_query_param('PackSign', PackSign)
	def get_PackName(self): # String
		return self.get_query_params().get('PackName')

	def set_PackName(self, PackName):  # String
		self.add_query_param('PackName', PackName)
	def get_HmAppIdentifier(self): # String
		return self.get_query_params().get('HmAppIdentifier')

	def set_HmAppIdentifier(self, HmAppIdentifier):  # String
		self.add_query_param('HmAppIdentifier', HmAppIdentifier)
	def get_CuApiCode(self): # Long
		return self.get_query_params().get('CuApiCode')

	def set_CuApiCode(self, CuApiCode):  # Long
		self.add_query_param('CuApiCode', CuApiCode)
	def get_SceneType(self): # String
		return self.get_query_params().get('SceneType')

	def set_SceneType(self, SceneType):  # String
		self.add_query_param('SceneType', SceneType)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_CtApiCode(self): # Long
		return self.get_query_params().get('CtApiCode')

	def set_CtApiCode(self, CtApiCode):  # Long
		self.add_query_param('CtApiCode', CtApiCode)
	def get_OsType(self): # String
		return self.get_query_params().get('OsType')

	def set_OsType(self, OsType):  # String
		self.add_query_param('OsType', OsType)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Url(self): # String
		return self.get_query_params().get('Url')

	def set_Url(self, Url):  # String
		self.add_query_param('Url', Url)
	def get_CmApiCode(self): # Long
		return self.get_query_params().get('CmApiCode')

	def set_CmApiCode(self, CmApiCode):  # Long
		self.add_query_param('CmApiCode', CmApiCode)
	def get_SchemeName(self): # String
		return self.get_query_params().get('SchemeName')

	def set_SchemeName(self, SchemeName):  # String
		self.add_query_param('SchemeName', SchemeName)
	def get_SmsSignName(self): # String
		return self.get_query_params().get('SmsSignName')

	def set_SmsSignName(self, SmsSignName):  # String
		self.add_query_param('SmsSignName', SmsSignName)
	def get_HmPackageName(self): # String
		return self.get_query_params().get('HmPackageName')

	def set_HmPackageName(self, HmPackageName):  # String
		self.add_query_param('HmPackageName', HmPackageName)
