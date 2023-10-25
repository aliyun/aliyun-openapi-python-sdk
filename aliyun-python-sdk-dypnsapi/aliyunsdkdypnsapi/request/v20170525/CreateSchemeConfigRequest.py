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

class CreateSchemeConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dypnsapi', '2017-05-25', 'CreateSchemeConfig','dypnsapi')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_AndroidPackageSign(self): # String
		return self.get_query_params().get('AndroidPackageSign')

	def set_AndroidPackageSign(self, AndroidPackageSign):  # String
		self.add_query_param('AndroidPackageSign', AndroidPackageSign)
	def get_Platform(self): # String
		return self.get_query_params().get('Platform')

	def set_Platform(self, Platform):  # String
		self.add_query_param('Platform', Platform)
	def get_H5Url(self): # String
		return self.get_query_params().get('H5Url')

	def set_H5Url(self, H5Url):  # String
		self.add_query_param('H5Url', H5Url)
	def get_IosBundleId(self): # String
		return self.get_query_params().get('IosBundleId')

	def set_IosBundleId(self, IosBundleId):  # String
		self.add_query_param('IosBundleId', IosBundleId)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_H5Origin(self): # String
		return self.get_query_params().get('H5Origin')

	def set_H5Origin(self, H5Origin):  # String
		self.add_query_param('H5Origin', H5Origin)
	def get_SchemeName(self): # String
		return self.get_query_params().get('SchemeName')

	def set_SchemeName(self, SchemeName):  # String
		self.add_query_param('SchemeName', SchemeName)
	def get_AndroidPackageName(self): # String
		return self.get_query_params().get('AndroidPackageName')

	def set_AndroidPackageName(self, AndroidPackageName):  # String
		self.add_query_param('AndroidPackageName', AndroidPackageName)
