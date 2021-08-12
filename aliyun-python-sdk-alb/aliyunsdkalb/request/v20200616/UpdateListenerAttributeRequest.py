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

class UpdateListenerAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'UpdateListenerAttribute','alb')
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
	def get_ListenerId(self): # String
		return self.get_query_params().get('ListenerId')

	def set_ListenerId(self, ListenerId):  # String
		self.add_query_param('ListenerId', ListenerId)
	def get_QuicConfig(self): # Struct
		return self.get_query_params().get('QuicConfig')

	def set_QuicConfig(self, QuicConfig):  # Struct
		for key1, value1 in QuicConfig.items():
			self.add_query_param('QuicConfig.' + key1 + '.QuicUpgradeEnabled', value1)
			self.add_query_param('QuicConfig.' + key1 + '.QuicListenerId', value1)
	def get_Http2Enabled(self): # Boolean
		return self.get_query_params().get('Http2Enabled')

	def set_Http2Enabled(self, Http2Enabled):  # Boolean
		self.add_query_param('Http2Enabled', Http2Enabled)
	def get_DefaultActions(self): # Array
		return self.get_query_params().get('DefaultActions')

	def set_DefaultActions(self, DefaultActions):  # Array
		for index1, value1 in enumerate(DefaultActions):
			for key2, value2 in value1.items():
				for key3, value3 in value2.items():
					for index4, value4 in enumerate(value3):
						for key5, value5 in value4.items():
							self.add_query_param('DefaultActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.' + str(index4 + 1) + '.' + key5 + '.ServerGroupId', value5)
				self.add_query_param('DefaultActions.' + str(index1 + 1) + '.' + key2 + '.Type', value2)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_RequestTimeout(self): # Integer
		return self.get_query_params().get('RequestTimeout')

	def set_RequestTimeout(self, RequestTimeout):  # Integer
		self.add_query_param('RequestTimeout', RequestTimeout)
	def get_XForwardedForConfig(self): # Struct
		return self.get_query_params().get('XForwardedForConfig')

	def set_XForwardedForConfig(self, XForwardedForConfig):  # Struct
		for key1, value1 in XForwardedForConfig.items():
			self.add_query_param('XForwardedForConfig.' + key1 + '.XForwardedForClientCertSubjectDNAlias', value1)
			self.add_query_param('XForwardedForConfig.' + key1 + '.XForwardedForClientCertIssuerDNEnabled', value1)
			self.add_query_param('XForwardedForConfig.' + key1 + '.XForwardedForClientCertFingerprintEnabled', value1)
			self.add_query_param('XForwardedForConfig.' + key1 + '.XForwardedForClientCertIssuerDNAlias', value1)
			self.add_query_param('XForwardedForConfig.' + key1 + '.XForwardedForProtoEnabled', value1)
			self.add_query_param('XForwardedForConfig.' + key1 + '.XForwardedForClientCertFingerprintAlias', value1)
			self.add_query_param('XForwardedForConfig.' + key1 + '.XForwardedForClientCertClientVerifyEnabled', value1)
			self.add_query_param('XForwardedForConfig.' + key1 + '.XForwardedForSLBPortEnabled', value1)
			self.add_query_param('XForwardedForConfig.' + key1 + '.XForwardedForClientCertSubjectDNEnabled', value1)
			self.add_query_param('XForwardedForConfig.' + key1 + '.XForwardedForClientCertClientVerifyAlias', value1)
			self.add_query_param('XForwardedForConfig.' + key1 + '.XForwardedForClientSrcPortEnabled', value1)
			self.add_query_param('XForwardedForConfig.' + key1 + '.XForwardedForEnabled', value1)
			self.add_query_param('XForwardedForConfig.' + key1 + '.XForwardedForSLBIdEnabled', value1)
	def get_SecurityPolicyId(self): # String
		return self.get_query_params().get('SecurityPolicyId')

	def set_SecurityPolicyId(self, SecurityPolicyId):  # String
		self.add_query_param('SecurityPolicyId', SecurityPolicyId)
	def get_IdleTimeout(self): # Integer
		return self.get_query_params().get('IdleTimeout')

	def set_IdleTimeout(self, IdleTimeout):  # Integer
		self.add_query_param('IdleTimeout', IdleTimeout)
	def get_Certificates(self): # Array
		return self.get_query_params().get('Certificates')

	def set_Certificates(self, Certificates):  # Array
		for index1, value1 in enumerate(Certificates):
			for key2, value2 in value1.items():
				self.add_query_param('Certificates.' + str(index1 + 1) + '.' + key2 + '.CertificateId', value2)
	def get_ListenerDescription(self): # String
		return self.get_query_params().get('ListenerDescription')

	def set_ListenerDescription(self, ListenerDescription):  # String
		self.add_query_param('ListenerDescription', ListenerDescription)
