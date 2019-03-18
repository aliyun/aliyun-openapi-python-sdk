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
class CreateSignaturePeopleCertificateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cas', '2018-08-13', 'CreateSignaturePeopleCertificate','cas_esign_fdd')

	def get_PeopleName(self):
		return self.get_query_params().get('PeopleName')

	def set_PeopleName(self,PeopleName):
		self.add_query_param('PeopleName',PeopleName)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_Mobile(self):
		return self.get_query_params().get('Mobile')

	def set_Mobile(self,Mobile):
		self.add_query_param('Mobile',Mobile)

	def get_IdentityNumber(self):
		return self.get_query_params().get('IdentityNumber')

	def set_IdentityNumber(self,IdentityNumber):
		self.add_query_param('IdentityNumber',IdentityNumber)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Email(self):
		return self.get_query_params().get('Email')

	def set_Email(self,Email):
		self.add_query_param('Email',Email)