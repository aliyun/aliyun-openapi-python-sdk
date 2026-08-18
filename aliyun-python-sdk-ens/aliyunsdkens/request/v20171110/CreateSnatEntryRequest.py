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

class CreateSnatEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'CreateSnatEntry','ens')
		self.set_method('POST')

	def get_SnatIp(self): # String
		return self.get_query_params().get('SnatIp')

	def set_SnatIp(self, SnatIp):  # String
		self.add_query_param('SnatIp', SnatIp)
	def get_SourceVSwitchId(self): # String
		return self.get_query_params().get('SourceVSwitchId')

	def set_SourceVSwitchId(self, SourceVSwitchId):  # String
		self.add_query_param('SourceVSwitchId', SourceVSwitchId)
	def get_EipAffinity(self): # Boolean
		return self.get_query_params().get('EipAffinity')

	def set_EipAffinity(self, EipAffinity):  # Boolean
		self.add_query_param('EipAffinity', EipAffinity)
	def get_SourceNetworkId(self): # String
		return self.get_query_params().get('SourceNetworkId')

	def set_SourceNetworkId(self, SourceNetworkId):  # String
		self.add_query_param('SourceNetworkId', SourceNetworkId)
	def get_StandbySnatIp(self): # String
		return self.get_query_params().get('StandbySnatIp')

	def set_StandbySnatIp(self, StandbySnatIp):  # String
		self.add_query_param('StandbySnatIp', StandbySnatIp)
	def get_SourceCIDR(self): # String
		return self.get_query_params().get('SourceCIDR')

	def set_SourceCIDR(self, SourceCIDR):  # String
		self.add_query_param('SourceCIDR', SourceCIDR)
	def get_NatGatewayId(self): # String
		return self.get_query_params().get('NatGatewayId')

	def set_NatGatewayId(self, NatGatewayId):  # String
		self.add_query_param('NatGatewayId', NatGatewayId)
	def get_IdleTimeout(self): # Integer
		return self.get_query_params().get('IdleTimeout')

	def set_IdleTimeout(self, IdleTimeout):  # Integer
		self.add_query_param('IdleTimeout', IdleTimeout)
	def get_SnatEntryName(self): # String
		return self.get_query_params().get('SnatEntryName')

	def set_SnatEntryName(self, SnatEntryName):  # String
		self.add_query_param('SnatEntryName', SnatEntryName)
	def get_IspAffinity(self): # Boolean
		return self.get_query_params().get('IspAffinity')

	def set_IspAffinity(self, IspAffinity):  # Boolean
		self.add_query_param('IspAffinity', IspAffinity)
