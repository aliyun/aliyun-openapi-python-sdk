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

class UpdateEthereumNodeConfigurationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'UpdateEthereumNodeConfiguration')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_P2pPort(self):
		return self.get_body_params().get('P2pPort')

	def set_P2pPort(self,P2pPort):
		self.add_body_params('P2pPort', P2pPort)

	def get_WSPort(self):
		return self.get_body_params().get('WSPort')

	def set_WSPort(self,WSPort):
		self.add_body_params('WSPort', WSPort)

	def get_RaftPort(self):
		return self.get_body_params().get('RaftPort')

	def set_RaftPort(self,RaftPort):
		self.add_body_params('RaftPort', RaftPort)

	def get_TMPort(self):
		return self.get_body_params().get('TMPort')

	def set_TMPort(self,TMPort):
		self.add_body_params('TMPort', TMPort)

	def get_NodeId(self):
		return self.get_body_params().get('NodeId')

	def set_NodeId(self,NodeId):
		self.add_body_params('NodeId', NodeId)

	def get_IP(self):
		return self.get_body_params().get('IP')

	def set_IP(self,IP):
		self.add_body_params('IP', IP)

	def get_RpcPort(self):
		return self.get_body_params().get('RpcPort')

	def set_RpcPort(self,RpcPort):
		self.add_body_params('RpcPort', RpcPort)

	def get_TMPub(self):
		return self.get_body_params().get('TMPub')

	def set_TMPub(self,TMPub):
		self.add_body_params('TMPub', TMPub)

	def get_NodePub(self):
		return self.get_body_params().get('NodePub')

	def set_NodePub(self,NodePub):
		self.add_body_params('NodePub', NodePub)