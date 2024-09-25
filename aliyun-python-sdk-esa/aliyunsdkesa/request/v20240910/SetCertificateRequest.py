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

class SetCertificateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ESA', '2024-09-10', 'SetCertificate')
		self.set_method('POST')

	def get_Certificate(self): # String
		return self.get_body_params().get('Certificate')

	def set_Certificate(self, Certificate):  # String
		self.add_body_params('Certificate', Certificate)
	def get_Update(self): # Boolean
		return self.get_body_params().get('Update')

	def set_Update(self, Update):  # Boolean
		self.add_body_params('Update', Update)
	def get_Type(self): # String
		return self.get_body_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_body_params('Type', Type)
	def get_CasId(self): # Long
		return self.get_body_params().get('CasId')

	def set_CasId(self, CasId):  # Long
		self.add_body_params('CasId', CasId)
	def get_PrivateKey(self): # String
		return self.get_body_params().get('PrivateKey')

	def set_PrivateKey(self, PrivateKey):  # String
		self.add_body_params('PrivateKey', PrivateKey)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_SiteId(self): # Long
		return self.get_body_params().get('SiteId')

	def set_SiteId(self, SiteId):  # Long
		self.add_body_params('SiteId', SiteId)
	def get_Id(self): # String
		return self.get_body_params().get('Id')

	def set_Id(self, Id):  # String
		self.add_body_params('Id', Id)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_Region(self): # String
		return self.get_body_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_body_params('Region', Region)
