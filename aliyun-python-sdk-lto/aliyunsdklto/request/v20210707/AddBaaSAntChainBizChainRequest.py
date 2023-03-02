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

class AddBaaSAntChainBizChainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'lto', '2021-07-07', 'AddBaaSAntChainBizChain')
		self.set_method('POST')

	def get_CaCertPassword(self): # String
		return self.get_query_params().get('CaCertPassword')

	def set_CaCertPassword(self, CaCertPassword):  # String
		self.add_query_param('CaCertPassword', CaCertPassword)
	def get_NodeNameList(self): # String
		return self.get_query_params().get('NodeNameList')

	def set_NodeNameList(self, NodeNameList):  # String
		self.add_query_param('NodeNameList', NodeNameList)
	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_UserKey(self): # String
		return self.get_query_params().get('UserKey')

	def set_UserKey(self, UserKey):  # String
		self.add_query_param('UserKey', UserKey)
	def get_ClientCert(self): # String
		return self.get_query_params().get('ClientCert')

	def set_ClientCert(self, ClientCert):  # String
		self.add_query_param('ClientCert', ClientCert)
	def get_BaaSAntChainConsortiumId(self): # String
		return self.get_query_params().get('BaaSAntChainConsortiumId')

	def set_BaaSAntChainConsortiumId(self, BaaSAntChainConsortiumId):  # String
		self.add_query_param('BaaSAntChainConsortiumId', BaaSAntChainConsortiumId)
	def get_UserKeyPassword(self): # String
		return self.get_query_params().get('UserKeyPassword')

	def set_UserKeyPassword(self, UserKeyPassword):  # String
		self.add_query_param('UserKeyPassword', UserKeyPassword)
	def get_BaaSAntChainChainId(self): # String
		return self.get_query_params().get('BaaSAntChainChainId')

	def set_BaaSAntChainChainId(self, BaaSAntChainChainId):  # String
		self.add_query_param('BaaSAntChainChainId', BaaSAntChainChainId)
	def get_ClientKey(self): # String
		return self.get_query_params().get('ClientKey')

	def set_ClientKey(self, ClientKey):  # String
		self.add_query_param('ClientKey', ClientKey)
	def get_CaCert(self): # String
		return self.get_query_params().get('CaCert')

	def set_CaCert(self, CaCert):  # String
		self.add_query_param('CaCert', CaCert)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_ClientKeyPassword(self): # String
		return self.get_query_params().get('ClientKeyPassword')

	def set_ClientKeyPassword(self, ClientKeyPassword):  # String
		self.add_query_param('ClientKeyPassword', ClientKeyPassword)
	def get_ContractTemplateIdList(self): # String
		return self.get_query_params().get('ContractTemplateIdList')

	def set_ContractTemplateIdList(self, ContractTemplateIdList):  # String
		self.add_query_param('ContractTemplateIdList', ContractTemplateIdList)
	def get_UserName(self): # String
		return self.get_query_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_query_param('UserName', UserName)
