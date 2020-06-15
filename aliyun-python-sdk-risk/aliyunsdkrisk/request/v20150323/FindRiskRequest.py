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

class FindRiskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Risk', '2015-03-23', 'FindRisk')
		self.set_method('POST')

	def get_IdType(self):
		return self.get_query_params().get('IdType')

	def set_IdType(self,IdType):
		self.add_query_param('IdType',IdType)

	def get_CodeType(self):
		return self.get_query_params().get('CodeType')

	def set_CodeType(self,CodeType):
		self.add_query_param('CodeType',CodeType)

	def get_Phone(self):
		return self.get_query_params().get('Phone')

	def set_Phone(self,Phone):
		self.add_query_param('Phone',Phone)

	def get_UmidToken(self):
		return self.get_query_params().get('UmidToken')

	def set_UmidToken(self,UmidToken):
		self.add_query_param('UmidToken',UmidToken)

	def get_Collina(self):
		return self.get_query_params().get('Collina')

	def set_Collina(self,Collina):
		self.add_query_param('Collina',Collina)

	def get_Ip(self):
		return self.get_query_params().get('Ip')

	def set_Ip(self,Ip):
		self.add_query_param('Ip',Ip)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_MteeCode(self):
		return self.get_query_params().get('MteeCode')

	def set_MteeCode(self,MteeCode):
		self.add_query_param('MteeCode',MteeCode)

	def get_Email(self):
		return self.get_query_params().get('Email')

	def set_Email(self,Email):
		self.add_query_param('Email',Email)