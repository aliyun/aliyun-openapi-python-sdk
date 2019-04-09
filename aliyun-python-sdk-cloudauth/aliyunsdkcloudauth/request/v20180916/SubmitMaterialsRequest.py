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
class SubmitMaterialsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2018-09-16', 'SubmitMaterials','cloudauth')
		self.set_protocol_type('https');
		self.set_method('POST')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_Materials(self):
		return self.get_body_params().get('Materials')

	def set_Materials(self,Materials):
		for i in range(len(Materials)):	
			if Materials[i].get('MaterialType') is not None:
				self.add_body_params('Material.' + str(i + 1) + '.MaterialType' , Materials[i].get('MaterialType'))
			if Materials[i].get('Value') is not None:
				self.add_body_params('Material.' + str(i + 1) + '.Value' , Materials[i].get('Value'))


	def get_VerifyToken(self):
		return self.get_body_params().get('VerifyToken')

	def set_VerifyToken(self,VerifyToken):
		self.add_body_params('VerifyToken', VerifyToken)