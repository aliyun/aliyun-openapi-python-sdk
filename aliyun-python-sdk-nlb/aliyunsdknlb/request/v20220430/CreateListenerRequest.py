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
from aliyunsdknlb.endpoint import endpoint_data

class CreateListenerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Nlb', '2022-04-30', 'CreateListener','nlb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CaCertificateIdss(self): # RepeatList
		return self.get_body_params().get('CaCertificateIds')

	def set_CaCertificateIdss(self, CaCertificateIds):  # RepeatList
		for depth1 in range(len(CaCertificateIds)):
			self.add_body_params('CaCertificateIds.' + str(depth1 + 1), CaCertificateIds[depth1])
	def get_StartPort(self): # Integer
		return self.get_body_params().get('StartPort')

	def set_StartPort(self, StartPort):  # Integer
		self.add_body_params('StartPort', StartPort)
	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_SecSensorEnabled(self): # Boolean
		return self.get_body_params().get('SecSensorEnabled')

	def set_SecSensorEnabled(self, SecSensorEnabled):  # Boolean
		self.add_body_params('SecSensorEnabled', SecSensorEnabled)
	def get_AlpnPolicy(self): # String
		return self.get_body_params().get('AlpnPolicy')

	def set_AlpnPolicy(self, AlpnPolicy):  # String
		self.add_body_params('AlpnPolicy', AlpnPolicy)
	def get_Mss(self): # Integer
		return self.get_body_params().get('Mss')

	def set_Mss(self, Mss):  # Integer
		self.add_body_params('Mss', Mss)
	def get_ServerGroupId(self): # String
		return self.get_body_params().get('ServerGroupId')

	def set_ServerGroupId(self, ServerGroupId):  # String
		self.add_body_params('ServerGroupId', ServerGroupId)
	def get_CertificateIdss(self): # RepeatList
		return self.get_body_params().get('CertificateIds')

	def set_CertificateIdss(self, CertificateIds):  # RepeatList
		for depth1 in range(len(CertificateIds)):
			self.add_body_params('CertificateIds.' + str(depth1 + 1), CertificateIds[depth1])
	def get_AlpnEnabled(self): # Boolean
		return self.get_body_params().get('AlpnEnabled')

	def set_AlpnEnabled(self, AlpnEnabled):  # Boolean
		self.add_body_params('AlpnEnabled', AlpnEnabled)
	def get_EndPort(self): # Integer
		return self.get_body_params().get('EndPort')

	def set_EndPort(self, EndPort):  # Integer
		self.add_body_params('EndPort', EndPort)
	def get_ListenerPort(self): # Integer
		return self.get_body_params().get('ListenerPort')

	def set_ListenerPort(self, ListenerPort):  # Integer
		self.add_body_params('ListenerPort', ListenerPort)
	def get_DryRun(self): # Boolean
		return self.get_body_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_body_params('DryRun', DryRun)
	def get_ProxyProtocolEnabled(self): # Boolean
		return self.get_body_params().get('ProxyProtocolEnabled')

	def set_ProxyProtocolEnabled(self, ProxyProtocolEnabled):  # Boolean
		self.add_body_params('ProxyProtocolEnabled', ProxyProtocolEnabled)
	def get_Cps(self): # Integer
		return self.get_body_params().get('Cps')

	def set_Cps(self, Cps):  # Integer
		self.add_body_params('Cps', Cps)
	def get_ListenerProtocol(self): # String
		return self.get_body_params().get('ListenerProtocol')

	def set_ListenerProtocol(self, ListenerProtocol):  # String
		self.add_body_params('ListenerProtocol', ListenerProtocol)
	def get_SecurityPolicyId(self): # String
		return self.get_body_params().get('SecurityPolicyId')

	def set_SecurityPolicyId(self, SecurityPolicyId):  # String
		self.add_body_params('SecurityPolicyId', SecurityPolicyId)
	def get_IdleTimeout(self): # Integer
		return self.get_body_params().get('IdleTimeout')

	def set_IdleTimeout(self, IdleTimeout):  # Integer
		self.add_body_params('IdleTimeout', IdleTimeout)
	def get_LoadBalancerId(self): # String
		return self.get_body_params().get('LoadBalancerId')

	def set_LoadBalancerId(self, LoadBalancerId):  # String
		self.add_body_params('LoadBalancerId', LoadBalancerId)
	def get_ListenerDescription(self): # String
		return self.get_body_params().get('ListenerDescription')

	def set_ListenerDescription(self, ListenerDescription):  # String
		self.add_body_params('ListenerDescription', ListenerDescription)
	def get_CaEnabled(self): # Boolean
		return self.get_body_params().get('CaEnabled')

	def set_CaEnabled(self, CaEnabled):  # Boolean
		self.add_body_params('CaEnabled', CaEnabled)
