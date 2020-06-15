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
from aliyunsdkbaas.endpoint import endpoint_data

class CreateAntChainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'CreateAntChain')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CipherSuit(self):
		return self.get_body_params().get('CipherSuit')

	def set_CipherSuit(self,CipherSuit):
		self.add_body_params('CipherSuit', CipherSuit)

	def get_NodeNum(self):
		return self.get_body_params().get('NodeNum')

	def set_NodeNum(self,NodeNum):
		self.add_body_params('NodeNum', NodeNum)

	def get_BlockchainRegionId(self):
		return self.get_body_params().get('BlockchainRegionId')

	def set_BlockchainRegionId(self,BlockchainRegionId):
		self.add_body_params('BlockchainRegionId', BlockchainRegionId)

	def get_MerkleTreeSuit(self):
		return self.get_body_params().get('MerkleTreeSuit')

	def set_MerkleTreeSuit(self,MerkleTreeSuit):
		self.add_body_params('MerkleTreeSuit', MerkleTreeSuit)

	def get_ResourceSize(self):
		return self.get_body_params().get('ResourceSize')

	def set_ResourceSize(self,ResourceSize):
		self.add_body_params('ResourceSize', ResourceSize)

	def get_TlsAlgo(self):
		return self.get_body_params().get('TlsAlgo')

	def set_TlsAlgo(self,TlsAlgo):
		self.add_body_params('TlsAlgo', TlsAlgo)

	def get_AntChainName(self):
		return self.get_body_params().get('AntChainName')

	def set_AntChainName(self,AntChainName):
		self.add_body_params('AntChainName', AntChainName)

	def get_LiveTime(self):
		return self.get_body_params().get('LiveTime')

	def set_LiveTime(self,LiveTime):
		self.add_body_params('LiveTime', LiveTime)

	def get_ConsortiumId(self):
		return self.get_body_params().get('ConsortiumId')

	def set_ConsortiumId(self,ConsortiumId):
		self.add_body_params('ConsortiumId', ConsortiumId)