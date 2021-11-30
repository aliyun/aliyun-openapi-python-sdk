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
from aliyunsdkalb.endpoint import endpoint_data

class CreateListenerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'CreateListener','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_GzipEnabled(self): # Boolean
		return self.get_query_params().get('GzipEnabled')

	def set_GzipEnabled(self, GzipEnabled):  # Boolean
		self.add_query_param('GzipEnabled', GzipEnabled)
	def get_QuicConfig(self): # Struct
		return self.get_query_params().get('QuicConfig')

	def set_QuicConfig(self, QuicConfig):  # Struct
		if QuicConfig.get('QuicUpgradeEnabled') is not None:
			self.add_query_param('QuicConfig.QuicUpgradeEnabled', QuicConfig.get('QuicUpgradeEnabled'))
		if QuicConfig.get('QuicListenerId') is not None:
			self.add_query_param('QuicConfig.QuicListenerId', QuicConfig.get('QuicListenerId'))
	def get_Http2Enabled(self): # Boolean
		return self.get_query_params().get('Http2Enabled')

	def set_Http2Enabled(self, Http2Enabled):  # Boolean
		self.add_query_param('Http2Enabled', Http2Enabled)
	def get_DefaultActions(self): # Array
		return self.get_query_params().get('DefaultActions')

	def set_DefaultActions(self, DefaultActions):  # Array
		for index1, value1 in enumerate(DefaultActions):
			if value1.get('ForwardGroupConfig') is not None:
				if value1.get('ForwardGroupConfig').get('ServerGroupTuples') is not None:
					for index2, value2 in enumerate(value1.get('ForwardGroupConfig').get('ServerGroupTuples')):
						if value2.get('ServerGroupId') is not None:
							self.add_query_param('DefaultActions.' + str(index1 + 1) + '.ForwardGroupConfig.ServerGroupTuples' + str(index2 + 1) + '.ServerGroupId', value2.get('ServerGroupId'))
			if value1.get('Type') is not None:
				self.add_query_param('DefaultActions.' + str(index1 + 1) + '.Type', value1.get('Type'))
	def get_ListenerPort(self): # Integer
		return self.get_query_params().get('ListenerPort')

	def set_ListenerPort(self, ListenerPort):  # Integer
		self.add_query_param('ListenerPort', ListenerPort)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_RequestTimeout(self): # Integer
		return self.get_query_params().get('RequestTimeout')

	def set_RequestTimeout(self, RequestTimeout):  # Integer
		self.add_query_param('RequestTimeout', RequestTimeout)
	def get_CaCertificates(self): # Array
		return self.get_query_params().get('CaCertificates')

	def set_CaCertificates(self, CaCertificates):  # Array
		for index1, value1 in enumerate(CaCertificates):
			if value1.get('CertificateId') is not None:
				self.add_query_param('CaCertificates.' + str(index1 + 1) + '.CertificateId', value1.get('CertificateId'))
	def get_XForwardedForConfig(self): # Struct
		return self.get_query_params().get('XForwardedForConfig')

	def set_XForwardedForConfig(self, XForwardedForConfig):  # Struct
		if XForwardedForConfig.get('XForwardedForClientCertSubjectDNAlias') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForClientCertSubjectDNAlias', XForwardedForConfig.get('XForwardedForClientCertSubjectDNAlias'))
		if XForwardedForConfig.get('XForwardedForClientCertIssuerDNEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForClientCertIssuerDNEnabled', XForwardedForConfig.get('XForwardedForClientCertIssuerDNEnabled'))
		if XForwardedForConfig.get('XForwardedForClientCertFingerprintEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForClientCertFingerprintEnabled', XForwardedForConfig.get('XForwardedForClientCertFingerprintEnabled'))
		if XForwardedForConfig.get('XForwardedForClientCertIssuerDNAlias') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForClientCertIssuerDNAlias', XForwardedForConfig.get('XForwardedForClientCertIssuerDNAlias'))
		if XForwardedForConfig.get('XForwardedForProtoEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForProtoEnabled', XForwardedForConfig.get('XForwardedForProtoEnabled'))
		if XForwardedForConfig.get('XForwardedForClientCertFingerprintAlias') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForClientCertFingerprintAlias', XForwardedForConfig.get('XForwardedForClientCertFingerprintAlias'))
		if XForwardedForConfig.get('XForwardedForClientCertClientVerifyEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForClientCertClientVerifyEnabled', XForwardedForConfig.get('XForwardedForClientCertClientVerifyEnabled'))
		if XForwardedForConfig.get('XForwardedForSLBPortEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForSLBPortEnabled', XForwardedForConfig.get('XForwardedForSLBPortEnabled'))
		if XForwardedForConfig.get('XForwardedForClientCertSubjectDNEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForClientCertSubjectDNEnabled', XForwardedForConfig.get('XForwardedForClientCertSubjectDNEnabled'))
		if XForwardedForConfig.get('XForwardedForClientCertClientVerifyAlias') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForClientCertClientVerifyAlias', XForwardedForConfig.get('XForwardedForClientCertClientVerifyAlias'))
		if XForwardedForConfig.get('XForwardedForClientSrcPortEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForClientSrcPortEnabled', XForwardedForConfig.get('XForwardedForClientSrcPortEnabled'))
		if XForwardedForConfig.get('XForwardedForEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForEnabled', XForwardedForConfig.get('XForwardedForEnabled'))
		if XForwardedForConfig.get('XForwardedForSLBIdEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForSLBIdEnabled', XForwardedForConfig.get('XForwardedForSLBIdEnabled'))
	def get_ListenerProtocol(self): # String
		return self.get_query_params().get('ListenerProtocol')

	def set_ListenerProtocol(self, ListenerProtocol):  # String
		self.add_query_param('ListenerProtocol', ListenerProtocol)
	def get_SecurityPolicyId(self): # String
		return self.get_query_params().get('SecurityPolicyId')

	def set_SecurityPolicyId(self, SecurityPolicyId):  # String
		self.add_query_param('SecurityPolicyId', SecurityPolicyId)
	def get_IdleTimeout(self): # Integer
		return self.get_query_params().get('IdleTimeout')

	def set_IdleTimeout(self, IdleTimeout):  # Integer
		self.add_query_param('IdleTimeout', IdleTimeout)
	def get_LoadBalancerId(self): # String
		return self.get_query_params().get('LoadBalancerId')

	def set_LoadBalancerId(self, LoadBalancerId):  # String
		self.add_query_param('LoadBalancerId', LoadBalancerId)
	def get_Certificates(self): # Array
		return self.get_query_params().get('Certificates')

	def set_Certificates(self, Certificates):  # Array
		for index1, value1 in enumerate(Certificates):
			if value1.get('CertificateId') is not None:
				self.add_query_param('Certificates.' + str(index1 + 1) + '.CertificateId', value1.get('CertificateId'))
	def get_ListenerDescription(self): # String
		return self.get_query_params().get('ListenerDescription')

	def set_ListenerDescription(self, ListenerDescription):  # String
		self.add_query_param('ListenerDescription', ListenerDescription)
	def get_CaEnabled(self): # Boolean
		return self.get_query_params().get('CaEnabled')

	def set_CaEnabled(self, CaEnabled):  # Boolean
		self.add_query_param('CaEnabled', CaEnabled)
