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
from aliyunsdkcomputenestsupplier.endpoint import endpoint_data
import json

class UpdateServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ComputeNestSupplier', '2021-05-21', 'UpdateService')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AlarmMetadata(self): # String
		return self.get_query_params().get('AlarmMetadata')

	def set_AlarmMetadata(self, AlarmMetadata):  # String
		self.add_query_param('AlarmMetadata', AlarmMetadata)
	def get_Resellable(self): # Boolean
		return self.get_query_params().get('Resellable')

	def set_Resellable(self, Resellable):  # Boolean
		self.add_query_param('Resellable', Resellable)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_PolicyNames(self): # String
		return self.get_query_params().get('PolicyNames')

	def set_PolicyNames(self, PolicyNames):  # String
		self.add_query_param('PolicyNames', PolicyNames)
	def get_LicenseMetadata(self): # String
		return self.get_query_params().get('LicenseMetadata')

	def set_LicenseMetadata(self, LicenseMetadata):  # String
		self.add_query_param('LicenseMetadata', LicenseMetadata)
	def get_Duration(self): # Long
		return self.get_query_params().get('Duration')

	def set_Duration(self, Duration):  # Long
		self.add_query_param('Duration', Duration)
	def get_TrialDuration(self): # Integer
		return self.get_query_params().get('TrialDuration')

	def set_TrialDuration(self, TrialDuration):  # Integer
		self.add_query_param('TrialDuration', TrialDuration)
	def get_UpgradeMetadata(self): # String
		return self.get_query_params().get('UpgradeMetadata')

	def set_UpgradeMetadata(self, UpgradeMetadata):  # String
		self.add_query_param('UpgradeMetadata', UpgradeMetadata)
	def get_DeployMetadata(self): # String
		return self.get_query_params().get('DeployMetadata')

	def set_DeployMetadata(self, DeployMetadata):  # String
		self.add_query_param('DeployMetadata', DeployMetadata)
	def get_ServiceType(self): # String
		return self.get_query_params().get('ServiceType')

	def set_ServiceType(self, ServiceType):  # String
		self.add_query_param('ServiceType', ServiceType)
	def get_IsSupportOperated(self): # Boolean
		return self.get_query_params().get('IsSupportOperated')

	def set_IsSupportOperated(self, IsSupportOperated):  # Boolean
		self.add_query_param('IsSupportOperated', IsSupportOperated)
	def get_TenantType(self): # String
		return self.get_query_params().get('TenantType')

	def set_TenantType(self, TenantType):  # String
		self.add_query_param('TenantType', TenantType)
	def get_ServiceVersion(self): # String
		return self.get_query_params().get('ServiceVersion')

	def set_ServiceVersion(self, ServiceVersion):  # String
		self.add_query_param('ServiceVersion', ServiceVersion)
	def get_LogMetadata(self): # String
		return self.get_query_params().get('LogMetadata')

	def set_LogMetadata(self, LogMetadata):  # String
		self.add_query_param('LogMetadata', LogMetadata)
	def get_ServiceInfos(self): # RepeatList
		return self.get_query_params().get('ServiceInfo')

	def set_ServiceInfos(self, ServiceInfo):  # RepeatList
		for depth1 in range(len(ServiceInfo)):
			if ServiceInfo[depth1].get('ShortDescription') is not None:
				self.add_query_param('ServiceInfo.' + str(depth1 + 1) + '.ShortDescription', ServiceInfo[depth1].get('ShortDescription'))
			if ServiceInfo[depth1].get('Image') is not None:
				self.add_query_param('ServiceInfo.' + str(depth1 + 1) + '.Image', ServiceInfo[depth1].get('Image'))
			if ServiceInfo[depth1].get('Name') is not None:
				self.add_query_param('ServiceInfo.' + str(depth1 + 1) + '.Name', ServiceInfo[depth1].get('Name'))
			if ServiceInfo[depth1].get('Agreements') is not None:
				for depth2 in range(len(ServiceInfo[depth1].get('Agreements'))):
					if ServiceInfo[depth1].get('Agreements')[depth2].get('Name') is not None:
						self.add_query_param('ServiceInfo.' + str(depth1 + 1) + '.Agreements.'  + str(depth2 + 1) + '.Name', ServiceInfo[depth1].get('Agreements')[depth2].get('Name'))
					if ServiceInfo[depth1].get('Agreements')[depth2].get('Url') is not None:
						self.add_query_param('ServiceInfo.' + str(depth1 + 1) + '.Agreements.'  + str(depth2 + 1) + '.Url', ServiceInfo[depth1].get('Agreements')[depth2].get('Url'))
			if ServiceInfo[depth1].get('Locale') is not None:
				self.add_query_param('ServiceInfo.' + str(depth1 + 1) + '.Locale', ServiceInfo[depth1].get('Locale'))
			if ServiceInfo[depth1].get('LongDescriptionUrl') is not None:
				self.add_query_param('ServiceInfo.' + str(depth1 + 1) + '.LongDescriptionUrl', ServiceInfo[depth1].get('LongDescriptionUrl'))
	def get_UpdateOption(self): # Struct
		return self.get_query_params().get('UpdateOption')

	def set_UpdateOption(self, UpdateOption):  # Struct
		self.add_query_param("UpdateOption", json.dumps(UpdateOption))
	def get_ServiceId(self): # String
		return self.get_query_params().get('ServiceId')

	def set_ServiceId(self, ServiceId):  # String
		self.add_query_param('ServiceId', ServiceId)
	def get_VersionName(self): # String
		return self.get_query_params().get('VersionName')

	def set_VersionName(self, VersionName):  # String
		self.add_query_param('VersionName', VersionName)
	def get_OperationMetadata(self): # String
		return self.get_query_params().get('OperationMetadata')

	def set_OperationMetadata(self, OperationMetadata):  # String
		self.add_query_param('OperationMetadata', OperationMetadata)
	def get_DeployType(self): # String
		return self.get_query_params().get('DeployType')

	def set_DeployType(self, DeployType):  # String
		self.add_query_param('DeployType', DeployType)
