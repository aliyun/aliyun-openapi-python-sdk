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
from aliyunsdkvoicenavigator.endpoint import endpoint_data

class GenerateUploadUrlRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'VoiceNavigator', '2018-06-12', 'GenerateUploadUrl','voicebot')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CallerParentId(self): # Long
		return self.get_body_params().get('CallerParentId')

	def set_CallerParentId(self, CallerParentId):  # Long
		self.add_body_params('CallerParentId', CallerParentId)
	def get_SecurityTransport(self): # Boolean
		return self.get_body_params().get('SecurityTransport')

	def set_SecurityTransport(self, SecurityTransport):  # Boolean
		self.add_body_params('SecurityTransport', SecurityTransport)
	def get_ProxyOriginalSecurityTransport(self): # Boolean
		return self.get_body_params().get('ProxyOriginalSecurityTransport')

	def set_ProxyOriginalSecurityTransport(self, ProxyOriginalSecurityTransport):  # Boolean
		self.add_body_params('ProxyOriginalSecurityTransport', ProxyOriginalSecurityTransport)
	def get_UserId(self): # Long
		return self.get_body_params().get('UserId')

	def set_UserId(self, UserId):  # Long
		self.add_body_params('UserId', UserId)
	def get_CallerType(self): # String
		return self.get_body_params().get('CallerType')

	def set_CallerType(self, CallerType):  # String
		self.add_body_params('CallerType', CallerType)
	def get_CallerIp(self): # String
		return self.get_body_params().get('CallerIp')

	def set_CallerIp(self, CallerIp):  # String
		self.add_body_params('CallerIp', CallerIp)
	def get_SecurityToken(self): # String
		return self.get_body_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_body_params('SecurityToken', SecurityToken)
	def get_InstanceOwnerId(self): # Long
		return self.get_body_params().get('InstanceOwnerId')

	def set_InstanceOwnerId(self, InstanceOwnerId):  # Long
		self.add_body_params('InstanceOwnerId', InstanceOwnerId)
	def get_ClientIp(self): # String
		return self.get_body_params().get('ClientIp')

	def set_ClientIp(self, ClientIp):  # String
		self.add_body_params('ClientIp', ClientIp)
	def get_TenantId(self): # Long
		return self.get_body_params().get('TenantId')

	def set_TenantId(self, TenantId):  # Long
		self.add_body_params('TenantId', TenantId)
	def get_ProxyOriginalSourceIp(self): # String
		return self.get_body_params().get('ProxyOriginalSourceIp')

	def set_ProxyOriginalSourceIp(self, ProxyOriginalSourceIp):  # String
		self.add_body_params('ProxyOriginalSourceIp', ProxyOriginalSourceIp)
	def get_Key(self): # String
		return self.get_body_params().get('Key')

	def set_Key(self, Key):  # String
		self.add_body_params('Key', Key)
	def get_CallerUid(self): # Long
		return self.get_body_params().get('CallerUid')

	def set_CallerUid(self, CallerUid):  # Long
		self.add_body_params('CallerUid', CallerUid)
	def get_CallerBid(self): # String
		return self.get_body_params().get('CallerBid')

	def set_CallerBid(self, CallerBid):  # String
		self.add_body_params('CallerBid', CallerBid)
	def get_XspaceTenantBuId(self): # Long
		return self.get_body_params().get('XspaceTenantBuId')

	def set_XspaceTenantBuId(self, XspaceTenantBuId):  # Long
		self.add_body_params('XspaceTenantBuId', XspaceTenantBuId)
	def get_MfaPresent(self): # Boolean
		return self.get_body_params().get('MfaPresent')

	def set_MfaPresent(self, MfaPresent):  # Boolean
		self.add_body_params('MfaPresent', MfaPresent)
	def get_Environment(self): # Integer
		return self.get_body_params().get('Environment')

	def set_Environment(self, Environment):  # Integer
		self.add_body_params('Environment', Environment)
	def get_FileName(self): # String
		return self.get_body_params().get('FileName')

	def set_FileName(self, FileName):  # String
		self.add_body_params('FileName', FileName)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_RequestId(self): # String
		return self.get_body_params().get('RequestId')

	def set_RequestId(self, RequestId):  # String
		self.add_body_params('RequestId', RequestId)
	def get_XspaceServicerId(self): # Long
		return self.get_body_params().get('XspaceServicerId')

	def set_XspaceServicerId(self, XspaceServicerId):  # Long
		self.add_body_params('XspaceServicerId', XspaceServicerId)
	def get_TenantName(self): # String
		return self.get_body_params().get('TenantName')

	def set_TenantName(self, TenantName):  # String
		self.add_body_params('TenantName', TenantName)
	def get_ProxyTrustTransportInfo(self): # Boolean
		return self.get_body_params().get('ProxyTrustTransportInfo')

	def set_ProxyTrustTransportInfo(self, ProxyTrustTransportInfo):  # Boolean
		self.add_body_params('ProxyTrustTransportInfo', ProxyTrustTransportInfo)
	def get_UserName(self): # String
		return self.get_body_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_body_params('UserName', UserName)
