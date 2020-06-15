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

class CreateEthereumRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'CreateEthereum')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Description(self):
		return self.get_body_params().get('Description')

	def set_Description(self,Description):
		self.add_body_params('Description', Description)

	def get_Gas(self):
		return self.get_body_params().get('Gas')

	def set_Gas(self,Gas):
		self.add_body_params('Gas', Gas)

	def get_Consensus(self):
		return self.get_body_params().get('Consensus')

	def set_Consensus(self,Consensus):
		self.add_body_params('Consensus', Consensus)

	def get_Difficulty(self):
		return self.get_body_params().get('Difficulty')

	def set_Difficulty(self,Difficulty):
		self.add_body_params('Difficulty', Difficulty)

	def get_Nodes(self):
		return self.get_body_params().get('Nodes')

	def set_Nodes(self, Nodes):
		for depth1 in range(len(Nodes)):
			if Nodes[depth1].get('Name') is not None:
				self.add_body_params('Node.' + str(depth1 + 1) + '.Name', Nodes[depth1].get('Name'))

	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)

	def get_NetworkId(self):
		return self.get_body_params().get('NetworkId')

	def set_NetworkId(self,NetworkId):
		self.add_body_params('NetworkId', NetworkId)

	def get_Region(self):
		return self.get_body_params().get('Region')

	def set_Region(self,Region):
		self.add_body_params('Region', Region)