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
from aliyunsdkbssopenapi.endpoint import endpoint_data

class CreateAgAccountRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'CreateAgAccount')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_FirstName(self):
		return self.get_query_params().get('FirstName')

	def set_FirstName(self,FirstName):
		self.add_query_param('FirstName',FirstName)

	def get_CityName(self):
		return self.get_query_params().get('CityName')

	def set_CityName(self,CityName):
		self.add_query_param('CityName',CityName)

	def get_Postcode(self):
		return self.get_query_params().get('Postcode')

	def set_Postcode(self,Postcode):
		self.add_query_param('Postcode',Postcode)

	def get_EnterpriseName(self):
		return self.get_query_params().get('EnterpriseName')

	def set_EnterpriseName(self,EnterpriseName):
		self.add_query_param('EnterpriseName',EnterpriseName)

	def get_NationCode(self):
		return self.get_query_params().get('NationCode')

	def set_NationCode(self,NationCode):
		self.add_query_param('NationCode',NationCode)

	def get_LastName(self):
		return self.get_query_params().get('LastName')

	def set_LastName(self,LastName):
		self.add_query_param('LastName',LastName)

	def get_LoginEmail(self):
		return self.get_query_params().get('LoginEmail')

	def set_LoginEmail(self,LoginEmail):
		self.add_query_param('LoginEmail',LoginEmail)

	def get_ProvinceName(self):
		return self.get_query_params().get('ProvinceName')

	def set_ProvinceName(self,ProvinceName):
		self.add_query_param('ProvinceName',ProvinceName)

	def get_AccountAttr(self):
		return self.get_query_params().get('AccountAttr')

	def set_AccountAttr(self,AccountAttr):
		self.add_query_param('AccountAttr',AccountAttr)