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

class SetIdentityProviderUdPullConfigurationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'SetIdentityProviderUdPullConfiguration','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_GroupSyncStatus(self): # String
		return self.get_query_params().get('GroupSyncStatus')

	def set_GroupSyncStatus(self, GroupSyncStatus):  # String
		self.add_query_param('GroupSyncStatus', GroupSyncStatus)
	def get_UdSyncScopeConfig(self): # Struct
		return self.get_query_params().get('UdSyncScopeConfig')

	def set_UdSyncScopeConfig(self, UdSyncScopeConfig):  # Struct
		if UdSyncScopeConfig.get('TargetScope') is not None:
			self.add_query_param('UdSyncScopeConfig.TargetScope', UdSyncScopeConfig.get('TargetScope'))
		if UdSyncScopeConfig.get('SourceScopes') is not None:
			for index1, value1 in enumerate(UdSyncScopeConfig.get('SourceScopes')):
				self.add_query_param('UdSyncScopeConfig.SourceScopes.' + str(index1 + 1), value1)
	def get_PeriodicSyncStatus(self): # String
		return self.get_query_params().get('PeriodicSyncStatus')

	def set_PeriodicSyncStatus(self, PeriodicSyncStatus):  # String
		self.add_query_param('PeriodicSyncStatus', PeriodicSyncStatus)
	def get_LdapUdPullConfig(self): # Struct
		return self.get_query_params().get('LdapUdPullConfig')

	def set_LdapUdPullConfig(self, LdapUdPullConfig):  # Struct
		if LdapUdPullConfig.get('GroupMemberAttributeName') is not None:
			self.add_query_param('LdapUdPullConfig.GroupMemberAttributeName', LdapUdPullConfig.get('GroupMemberAttributeName'))
		if LdapUdPullConfig.get('UserObjectClass') is not None:
			self.add_query_param('LdapUdPullConfig.UserObjectClass', LdapUdPullConfig.get('UserObjectClass'))
		if LdapUdPullConfig.get('UserObjectClassCustomFilter') is not None:
			self.add_query_param('LdapUdPullConfig.UserObjectClassCustomFilter', LdapUdPullConfig.get('UserObjectClassCustomFilter'))
		if LdapUdPullConfig.get('GroupObjectClass') is not None:
			self.add_query_param('LdapUdPullConfig.GroupObjectClass', LdapUdPullConfig.get('GroupObjectClass'))
		if LdapUdPullConfig.get('GroupObjectClassCustomFilter') is not None:
			self.add_query_param('LdapUdPullConfig.GroupObjectClassCustomFilter', LdapUdPullConfig.get('GroupObjectClassCustomFilter'))
		if LdapUdPullConfig.get('OrganizationUnitObjectClass') is not None:
			self.add_query_param('LdapUdPullConfig.OrganizationUnitObjectClass', LdapUdPullConfig.get('OrganizationUnitObjectClass'))
	def get_IdentityProviderId(self): # String
		return self.get_query_params().get('IdentityProviderId')

	def set_IdentityProviderId(self, IdentityProviderId):  # String
		self.add_query_param('IdentityProviderId', IdentityProviderId)
	def get_PeriodicSyncConfig(self): # Struct
		return self.get_query_params().get('PeriodicSyncConfig')

	def set_PeriodicSyncConfig(self, PeriodicSyncConfig):  # Struct
		if PeriodicSyncConfig.get('PeriodicSyncTimes') is not None:
			for index1, value1 in enumerate(PeriodicSyncConfig.get('PeriodicSyncTimes')):
				self.add_query_param('PeriodicSyncConfig.PeriodicSyncTimes.' + str(index1 + 1), value1)
		if PeriodicSyncConfig.get('PeriodicSyncCron') is not None:
			self.add_query_param('PeriodicSyncConfig.PeriodicSyncCron', PeriodicSyncConfig.get('PeriodicSyncCron'))
		if PeriodicSyncConfig.get('PeriodicSyncType') is not None:
			self.add_query_param('PeriodicSyncConfig.PeriodicSyncType', PeriodicSyncConfig.get('PeriodicSyncType'))
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_PullProtectedRule(self): # Struct
		return self.get_query_params().get('PullProtectedRule')

	def set_PullProtectedRule(self, PullProtectedRule):  # Struct
		if PullProtectedRule.get('UserDeletedThreshold') is not None:
			self.add_query_param('PullProtectedRule.UserDeletedThreshold', PullProtectedRule.get('UserDeletedThreshold'))
		if PullProtectedRule.get('GroupDeletedThreshold') is not None:
			self.add_query_param('PullProtectedRule.GroupDeletedThreshold', PullProtectedRule.get('GroupDeletedThreshold'))
		if PullProtectedRule.get('OrganizationalUnitDeletedThreshold') is not None:
			self.add_query_param('PullProtectedRule.OrganizationalUnitDeletedThreshold', PullProtectedRule.get('OrganizationalUnitDeletedThreshold'))
	def get_IncrementalCallbackStatus(self): # String
		return self.get_query_params().get('IncrementalCallbackStatus')

	def set_IncrementalCallbackStatus(self, IncrementalCallbackStatus):  # String
		self.add_query_param('IncrementalCallbackStatus', IncrementalCallbackStatus)
