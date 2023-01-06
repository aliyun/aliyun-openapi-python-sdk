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
from aliyunsdkecd.endpoint import endpoint_data

class ModifyPolicyGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'ModifyPolicyGroup')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RecordingExpires(self): # Long
		return self.get_query_params().get('RecordingExpires')

	def set_RecordingExpires(self, RecordingExpires):  # Long
		self.add_query_param('RecordingExpires', RecordingExpires)
	def get_RevokeSecurityPolicyRules(self): # RepeatList
		return self.get_query_params().get('RevokeSecurityPolicyRule')

	def set_RevokeSecurityPolicyRules(self, RevokeSecurityPolicyRule):  # RepeatList
		for depth1 in range(len(RevokeSecurityPolicyRule)):
			if RevokeSecurityPolicyRule[depth1].get('PortRange') is not None:
				self.add_query_param('RevokeSecurityPolicyRule.' + str(depth1 + 1) + '.PortRange', RevokeSecurityPolicyRule[depth1].get('PortRange'))
			if RevokeSecurityPolicyRule[depth1].get('IpProtocol') is not None:
				self.add_query_param('RevokeSecurityPolicyRule.' + str(depth1 + 1) + '.IpProtocol', RevokeSecurityPolicyRule[depth1].get('IpProtocol'))
			if RevokeSecurityPolicyRule[depth1].get('Description') is not None:
				self.add_query_param('RevokeSecurityPolicyRule.' + str(depth1 + 1) + '.Description', RevokeSecurityPolicyRule[depth1].get('Description'))
			if RevokeSecurityPolicyRule[depth1].get('Type') is not None:
				self.add_query_param('RevokeSecurityPolicyRule.' + str(depth1 + 1) + '.Type', RevokeSecurityPolicyRule[depth1].get('Type'))
			if RevokeSecurityPolicyRule[depth1].get('Priority') is not None:
				self.add_query_param('RevokeSecurityPolicyRule.' + str(depth1 + 1) + '.Priority', RevokeSecurityPolicyRule[depth1].get('Priority'))
			if RevokeSecurityPolicyRule[depth1].get('CidrIp') is not None:
				self.add_query_param('RevokeSecurityPolicyRule.' + str(depth1 + 1) + '.CidrIp', RevokeSecurityPolicyRule[depth1].get('CidrIp'))
			if RevokeSecurityPolicyRule[depth1].get('Policy') is not None:
				self.add_query_param('RevokeSecurityPolicyRule.' + str(depth1 + 1) + '.Policy', RevokeSecurityPolicyRule[depth1].get('Policy'))
	def get_PrinterRedirection(self): # String
		return self.get_query_params().get('PrinterRedirection')

	def set_PrinterRedirection(self, PrinterRedirection):  # String
		self.add_query_param('PrinterRedirection', PrinterRedirection)
	def get_PreemptLoginUsers(self): # RepeatList
		return self.get_query_params().get('PreemptLoginUser')

	def set_PreemptLoginUsers(self, PreemptLoginUser):  # RepeatList
		for depth1 in range(len(PreemptLoginUser)):
			self.add_query_param('PreemptLoginUser.' + str(depth1 + 1), PreemptLoginUser[depth1])
	def get_DomainList(self): # String
		return self.get_query_params().get('DomainList')

	def set_DomainList(self, DomainList):  # String
		self.add_query_param('DomainList', DomainList)
	def get_NetRedirect(self): # String
		return self.get_query_params().get('NetRedirect')

	def set_NetRedirect(self, NetRedirect):  # String
		self.add_query_param('NetRedirect', NetRedirect)
	def get_LocalDrive(self): # String
		return self.get_query_params().get('LocalDrive')

	def set_LocalDrive(self, LocalDrive):  # String
		self.add_query_param('LocalDrive', LocalDrive)
	def get_AuthorizeSecurityPolicyRules(self): # RepeatList
		return self.get_query_params().get('AuthorizeSecurityPolicyRule')

	def set_AuthorizeSecurityPolicyRules(self, AuthorizeSecurityPolicyRule):  # RepeatList
		for depth1 in range(len(AuthorizeSecurityPolicyRule)):
			if AuthorizeSecurityPolicyRule[depth1].get('PortRange') is not None:
				self.add_query_param('AuthorizeSecurityPolicyRule.' + str(depth1 + 1) + '.PortRange', AuthorizeSecurityPolicyRule[depth1].get('PortRange'))
			if AuthorizeSecurityPolicyRule[depth1].get('IpProtocol') is not None:
				self.add_query_param('AuthorizeSecurityPolicyRule.' + str(depth1 + 1) + '.IpProtocol', AuthorizeSecurityPolicyRule[depth1].get('IpProtocol'))
			if AuthorizeSecurityPolicyRule[depth1].get('Description') is not None:
				self.add_query_param('AuthorizeSecurityPolicyRule.' + str(depth1 + 1) + '.Description', AuthorizeSecurityPolicyRule[depth1].get('Description'))
			if AuthorizeSecurityPolicyRule[depth1].get('Type') is not None:
				self.add_query_param('AuthorizeSecurityPolicyRule.' + str(depth1 + 1) + '.Type', AuthorizeSecurityPolicyRule[depth1].get('Type'))
			if AuthorizeSecurityPolicyRule[depth1].get('Priority') is not None:
				self.add_query_param('AuthorizeSecurityPolicyRule.' + str(depth1 + 1) + '.Priority', AuthorizeSecurityPolicyRule[depth1].get('Priority'))
			if AuthorizeSecurityPolicyRule[depth1].get('CidrIp') is not None:
				self.add_query_param('AuthorizeSecurityPolicyRule.' + str(depth1 + 1) + '.CidrIp', AuthorizeSecurityPolicyRule[depth1].get('CidrIp'))
			if AuthorizeSecurityPolicyRule[depth1].get('Policy') is not None:
				self.add_query_param('AuthorizeSecurityPolicyRule.' + str(depth1 + 1) + '.Policy', AuthorizeSecurityPolicyRule[depth1].get('Policy'))
	def get_Clipboard(self): # String
		return self.get_query_params().get('Clipboard')

	def set_Clipboard(self, Clipboard):  # String
		self.add_query_param('Clipboard', Clipboard)
	def get_UsbRedirect(self): # String
		return self.get_query_params().get('UsbRedirect')

	def set_UsbRedirect(self, UsbRedirect):  # String
		self.add_query_param('UsbRedirect', UsbRedirect)
	def get_WatermarkType(self): # String
		return self.get_query_params().get('WatermarkType')

	def set_WatermarkType(self, WatermarkType):  # String
		self.add_query_param('WatermarkType', WatermarkType)
	def get_RecordingStartTime(self): # String
		return self.get_query_params().get('RecordingStartTime')

	def set_RecordingStartTime(self, RecordingStartTime):  # String
		self.add_query_param('RecordingStartTime', RecordingStartTime)
	def get_RecordingDuration(self): # Integer
		return self.get_query_params().get('RecordingDuration')

	def set_RecordingDuration(self, RecordingDuration):  # Integer
		self.add_query_param('RecordingDuration', RecordingDuration)
	def get_RevokeAccessPolicyRules(self): # RepeatList
		return self.get_query_params().get('RevokeAccessPolicyRule')

	def set_RevokeAccessPolicyRules(self, RevokeAccessPolicyRule):  # RepeatList
		for depth1 in range(len(RevokeAccessPolicyRule)):
			if RevokeAccessPolicyRule[depth1].get('Description') is not None:
				self.add_query_param('RevokeAccessPolicyRule.' + str(depth1 + 1) + '.Description', RevokeAccessPolicyRule[depth1].get('Description'))
			if RevokeAccessPolicyRule[depth1].get('CidrIp') is not None:
				self.add_query_param('RevokeAccessPolicyRule.' + str(depth1 + 1) + '.CidrIp', RevokeAccessPolicyRule[depth1].get('CidrIp'))
	def get_Watermark(self): # String
		return self.get_query_params().get('Watermark')

	def set_Watermark(self, Watermark):  # String
		self.add_query_param('Watermark', Watermark)
	def get_CameraRedirect(self): # String
		return self.get_query_params().get('CameraRedirect')

	def set_CameraRedirect(self, CameraRedirect):  # String
		self.add_query_param('CameraRedirect', CameraRedirect)
	def get_AppContentProtection(self): # String
		return self.get_query_params().get('AppContentProtection')

	def set_AppContentProtection(self, AppContentProtection):  # String
		self.add_query_param('AppContentProtection', AppContentProtection)
	def get_AuthorizeAccessPolicyRules(self): # RepeatList
		return self.get_query_params().get('AuthorizeAccessPolicyRule')

	def set_AuthorizeAccessPolicyRules(self, AuthorizeAccessPolicyRule):  # RepeatList
		for depth1 in range(len(AuthorizeAccessPolicyRule)):
			if AuthorizeAccessPolicyRule[depth1].get('Description') is not None:
				self.add_query_param('AuthorizeAccessPolicyRule.' + str(depth1 + 1) + '.Description', AuthorizeAccessPolicyRule[depth1].get('Description'))
			if AuthorizeAccessPolicyRule[depth1].get('CidrIp') is not None:
				self.add_query_param('AuthorizeAccessPolicyRule.' + str(depth1 + 1) + '.CidrIp', AuthorizeAccessPolicyRule[depth1].get('CidrIp'))
	def get_WatermarkTransparency(self): # String
		return self.get_query_params().get('WatermarkTransparency')

	def set_WatermarkTransparency(self, WatermarkTransparency):  # String
		self.add_query_param('WatermarkTransparency', WatermarkTransparency)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_PolicyGroupId(self): # String
		return self.get_query_params().get('PolicyGroupId')

	def set_PolicyGroupId(self, PolicyGroupId):  # String
		self.add_query_param('PolicyGroupId', PolicyGroupId)
	def get_PreemptLogin(self): # String
		return self.get_query_params().get('PreemptLogin')

	def set_PreemptLogin(self, PreemptLogin):  # String
		self.add_query_param('PreemptLogin', PreemptLogin)
	def get_ClientTypes(self): # RepeatList
		return self.get_query_params().get('ClientType')

	def set_ClientTypes(self, ClientType):  # RepeatList
		for depth1 in range(len(ClientType)):
			if ClientType[depth1].get('ClientType') is not None:
				self.add_query_param('ClientType.' + str(depth1 + 1) + '.ClientType', ClientType[depth1].get('ClientType'))
			if ClientType[depth1].get('Status') is not None:
				self.add_query_param('ClientType.' + str(depth1 + 1) + '.Status', ClientType[depth1].get('Status'))
	def get_UsbSupplyRedirectRules(self): # RepeatList
		return self.get_query_params().get('UsbSupplyRedirectRule')

	def set_UsbSupplyRedirectRules(self, UsbSupplyRedirectRule):  # RepeatList
		for depth1 in range(len(UsbSupplyRedirectRule)):
			if UsbSupplyRedirectRule[depth1].get('ProductId') is not None:
				self.add_query_param('UsbSupplyRedirectRule.' + str(depth1 + 1) + '.ProductId', UsbSupplyRedirectRule[depth1].get('ProductId'))
			if UsbSupplyRedirectRule[depth1].get('DeviceSubclass') is not None:
				self.add_query_param('UsbSupplyRedirectRule.' + str(depth1 + 1) + '.DeviceSubclass', UsbSupplyRedirectRule[depth1].get('DeviceSubclass'))
			if UsbSupplyRedirectRule[depth1].get('UsbRedirectType') is not None:
				self.add_query_param('UsbSupplyRedirectRule.' + str(depth1 + 1) + '.UsbRedirectType', UsbSupplyRedirectRule[depth1].get('UsbRedirectType'))
			if UsbSupplyRedirectRule[depth1].get('VendorId') is not None:
				self.add_query_param('UsbSupplyRedirectRule.' + str(depth1 + 1) + '.VendorId', UsbSupplyRedirectRule[depth1].get('VendorId'))
			if UsbSupplyRedirectRule[depth1].get('Description') is not None:
				self.add_query_param('UsbSupplyRedirectRule.' + str(depth1 + 1) + '.Description', UsbSupplyRedirectRule[depth1].get('Description'))
			if UsbSupplyRedirectRule[depth1].get('DeviceClass') is not None:
				self.add_query_param('UsbSupplyRedirectRule.' + str(depth1 + 1) + '.DeviceClass', UsbSupplyRedirectRule[depth1].get('DeviceClass'))
			if UsbSupplyRedirectRule[depth1].get('UsbRuleType') is not None:
				self.add_query_param('UsbSupplyRedirectRule.' + str(depth1 + 1) + '.UsbRuleType', UsbSupplyRedirectRule[depth1].get('UsbRuleType'))
	def get_Recording(self): # String
		return self.get_query_params().get('Recording')

	def set_Recording(self, Recording):  # String
		self.add_query_param('Recording', Recording)
	def get_ScopeValues(self): # RepeatList
		return self.get_query_params().get('ScopeValue')

	def set_ScopeValues(self, ScopeValue):  # RepeatList
		for depth1 in range(len(ScopeValue)):
			self.add_query_param('ScopeValue.' + str(depth1 + 1), ScopeValue[depth1])
	def get_RecordingFps(self): # Long
		return self.get_query_params().get('RecordingFps')

	def set_RecordingFps(self, RecordingFps):  # Long
		self.add_query_param('RecordingFps', RecordingFps)
	def get_RecordContent(self): # String
		return self.get_query_params().get('RecordContent')

	def set_RecordContent(self, RecordContent):  # String
		self.add_query_param('RecordContent', RecordContent)
	def get_Scope(self): # String
		return self.get_query_params().get('Scope')

	def set_Scope(self, Scope):  # String
		self.add_query_param('Scope', Scope)
	def get_RecordContentExpires(self): # Long
		return self.get_query_params().get('RecordContentExpires')

	def set_RecordContentExpires(self, RecordContentExpires):  # Long
		self.add_query_param('RecordContentExpires', RecordContentExpires)
	def get_RecordingAudio(self): # String
		return self.get_query_params().get('RecordingAudio')

	def set_RecordingAudio(self, RecordingAudio):  # String
		self.add_query_param('RecordingAudio', RecordingAudio)
	def get_RemoteCoordinate(self): # String
		return self.get_query_params().get('RemoteCoordinate')

	def set_RemoteCoordinate(self, RemoteCoordinate):  # String
		self.add_query_param('RemoteCoordinate', RemoteCoordinate)
	def get_Html5Access(self): # String
		return self.get_query_params().get('Html5Access')

	def set_Html5Access(self, Html5Access):  # String
		self.add_query_param('Html5Access', Html5Access)
	def get_GpuAcceleration(self): # String
		return self.get_query_params().get('GpuAcceleration')

	def set_GpuAcceleration(self, GpuAcceleration):  # String
		self.add_query_param('GpuAcceleration', GpuAcceleration)
	def get_Html5FileTransfer(self): # String
		return self.get_query_params().get('Html5FileTransfer')

	def set_Html5FileTransfer(self, Html5FileTransfer):  # String
		self.add_query_param('Html5FileTransfer', Html5FileTransfer)
	def get_VisualQuality(self): # String
		return self.get_query_params().get('VisualQuality')

	def set_VisualQuality(self, VisualQuality):  # String
		self.add_query_param('VisualQuality', VisualQuality)
	def get_RecordingEndTime(self): # String
		return self.get_query_params().get('RecordingEndTime')

	def set_RecordingEndTime(self, RecordingEndTime):  # String
		self.add_query_param('RecordingEndTime', RecordingEndTime)
	def get_InternetCommunicationProtocol(self): # String
		return self.get_query_params().get('InternetCommunicationProtocol')

	def set_InternetCommunicationProtocol(self, InternetCommunicationProtocol):  # String
		self.add_query_param('InternetCommunicationProtocol', InternetCommunicationProtocol)
