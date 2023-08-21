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

class LoginInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecs-workbench', '2022-02-20', 'LoginInstance','ecs-workbench')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_PartnerInfo(self): # Struct
		return self.get_query_params().get('PartnerInfo')

	def set_PartnerInfo(self, PartnerInfo):  # Struct
		if PartnerInfo.get('PartnerName') is not None:
			self.add_query_param('PartnerInfo.PartnerName', PartnerInfo.get('PartnerName'))
		if PartnerInfo.get('PartnerId') is not None:
			self.add_query_param('PartnerInfo.PartnerId', PartnerInfo.get('PartnerId'))
	def get_InstanceLoginInfo(self): # Struct
		return self.get_query_params().get('InstanceLoginInfo')

	def set_InstanceLoginInfo(self, InstanceLoginInfo):  # Struct
		if InstanceLoginInfo.get('ExpireTime') is not None:
			self.add_query_param('InstanceLoginInfo.ExpireTime', InstanceLoginInfo.get('ExpireTime'))
		if InstanceLoginInfo.get('Certificate') is not None:
			self.add_query_param('InstanceLoginInfo.Certificate', InstanceLoginInfo.get('Certificate'))
		if InstanceLoginInfo.get('AuthenticationType') is not None:
			self.add_query_param('InstanceLoginInfo.AuthenticationType', InstanceLoginInfo.get('AuthenticationType'))
		if InstanceLoginInfo.get('Protocol') is not None:
			self.add_query_param('InstanceLoginInfo.Protocol', InstanceLoginInfo.get('Protocol'))
		if InstanceLoginInfo.get('Password') is not None:
			self.add_query_param('InstanceLoginInfo.Password', InstanceLoginInfo.get('Password'))
		if InstanceLoginInfo.get('InstanceId') is not None:
			self.add_query_param('InstanceLoginInfo.InstanceId', InstanceLoginInfo.get('InstanceId'))
		if InstanceLoginInfo.get('RegionId') is not None:
			self.add_query_param('InstanceLoginInfo.RegionId', InstanceLoginInfo.get('RegionId'))
		if InstanceLoginInfo.get('Port') is not None:
			self.add_query_param('InstanceLoginInfo.Port', InstanceLoginInfo.get('Port'))
		if InstanceLoginInfo.get('VpcId') is not None:
			self.add_query_param('InstanceLoginInfo.VpcId', InstanceLoginInfo.get('VpcId'))
		if InstanceLoginInfo.get('Host') is not None:
			self.add_query_param('InstanceLoginInfo.Host', InstanceLoginInfo.get('Host'))
		if InstanceLoginInfo.get('Options') is not None:
			if InstanceLoginInfo.get('Options').get('OperationDisableSeconds') is not None:
				self.add_query_param('InstanceLoginInfo.Options.OperationDisableSeconds', InstanceLoginInfo.get('Options').get('OperationDisableSeconds'))
			if InstanceLoginInfo.get('Options').get('NotificationRecipientUrl') is not None:
				self.add_query_param('InstanceLoginInfo.Options.NotificationRecipientUrl', InstanceLoginInfo.get('Options').get('NotificationRecipientUrl'))
			if InstanceLoginInfo.get('Options').get('SessionControl') is not None:
				self.add_query_param('InstanceLoginInfo.Options.SessionControl', InstanceLoginInfo.get('Options').get('SessionControl'))
			if InstanceLoginInfo.get('Options').get('VideoFreezeSeconds') is not None:
				self.add_query_param('InstanceLoginInfo.Options.VideoFreezeSeconds', InstanceLoginInfo.get('Options').get('VideoFreezeSeconds'))
			if InstanceLoginInfo.get('Options').get('ContainerInfo') is not None:
				if InstanceLoginInfo.get('Options').get('ContainerInfo').get('Headers') is not None:
					for key1, value1 in InstanceLoginInfo.get('Options').get('ContainerInfo').get('Headers').items():
						self.add_query_param('InstanceLoginInfo.Options.ContainerInfo.#' + str(len(key1)) + '#' + key1, value1)
				if InstanceLoginInfo.get('Options').get('ContainerInfo').get('Endpoint') is not None:
					self.add_query_param('InstanceLoginInfo.Options.ContainerInfo.Endpoint', InstanceLoginInfo.get('Options').get('ContainerInfo').get('Endpoint'))
				if InstanceLoginInfo.get('Options').get('ContainerInfo').get('ContainerName') is not None:
					self.add_query_param('InstanceLoginInfo.Options.ContainerInfo.ContainerName', InstanceLoginInfo.get('Options').get('ContainerInfo').get('ContainerName'))
				if InstanceLoginInfo.get('Options').get('ContainerInfo').get('ClusterName') is not None:
					self.add_query_param('InstanceLoginInfo.Options.ContainerInfo.ClusterName', InstanceLoginInfo.get('Options').get('ContainerInfo').get('ClusterName'))
				if InstanceLoginInfo.get('Options').get('ContainerInfo').get('Namespace') is not None:
					self.add_query_param('InstanceLoginInfo.Options.ContainerInfo.Namespace', InstanceLoginInfo.get('Options').get('ContainerInfo').get('Namespace'))
				if InstanceLoginInfo.get('Options').get('ContainerInfo').get('PodName') is not None:
					self.add_query_param('InstanceLoginInfo.Options.ContainerInfo.PodName', InstanceLoginInfo.get('Options').get('ContainerInfo').get('PodName'))
				if InstanceLoginInfo.get('Options').get('ContainerInfo').get('ClusterId') is not None:
					self.add_query_param('InstanceLoginInfo.Options.ContainerInfo.ClusterId', InstanceLoginInfo.get('Options').get('ContainerInfo').get('ClusterId'))
				if InstanceLoginInfo.get('Options').get('ContainerInfo').get('Deployment') is not None:
					self.add_query_param('InstanceLoginInfo.Options.ContainerInfo.Deployment', InstanceLoginInfo.get('Options').get('ContainerInfo').get('Deployment'))
			if InstanceLoginInfo.get('Options').get('NotificationRetryIntervalSeconds') is not None:
				self.add_query_param('InstanceLoginInfo.Options.NotificationRetryIntervalSeconds', InstanceLoginInfo.get('Options').get('NotificationRetryIntervalSeconds'))
			if InstanceLoginInfo.get('Options').get('AudioMuteSeconds') is not None:
				self.add_query_param('InstanceLoginInfo.Options.AudioMuteSeconds', InstanceLoginInfo.get('Options').get('AudioMuteSeconds'))
			if InstanceLoginInfo.get('Options').get('FixedHeight') is not None:
				self.add_query_param('InstanceLoginInfo.Options.FixedHeight', InstanceLoginInfo.get('Options').get('FixedHeight'))
			if InstanceLoginInfo.get('Options').get('FixedWidth') is not None:
				self.add_query_param('InstanceLoginInfo.Options.FixedWidth', InstanceLoginInfo.get('Options').get('FixedWidth'))
			if InstanceLoginInfo.get('Options').get('NotificationEventTypes') is not None:
				self.add_query_param('InstanceLoginInfo.Options.NotificationEventTypes', InstanceLoginInfo.get('Options').get('NotificationEventTypes'))
			if InstanceLoginInfo.get('Options').get('NotificationRetryLimit') is not None:
				self.add_query_param('InstanceLoginInfo.Options.NotificationRetryLimit', InstanceLoginInfo.get('Options').get('NotificationRetryLimit'))
		if InstanceLoginInfo.get('InstanceType') is not None:
			self.add_query_param('InstanceLoginInfo.InstanceType', InstanceLoginInfo.get('InstanceType'))
		if InstanceLoginInfo.get('PassPhrase') is not None:
			self.add_query_param('InstanceLoginInfo.PassPhrase', InstanceLoginInfo.get('PassPhrase'))
		if InstanceLoginInfo.get('DurationSeconds') is not None:
			self.add_query_param('InstanceLoginInfo.DurationSeconds', InstanceLoginInfo.get('DurationSeconds'))
		if InstanceLoginInfo.get('NetworkAccessMode') is not None:
			self.add_query_param('InstanceLoginInfo.NetworkAccessMode', InstanceLoginInfo.get('NetworkAccessMode'))
		if InstanceLoginInfo.get('Username') is not None:
			self.add_query_param('InstanceLoginInfo.Username', InstanceLoginInfo.get('Username'))
	def get_UserAccount(self): # Struct
		return self.get_query_params().get('UserAccount')

	def set_UserAccount(self, UserAccount):  # Struct
		if UserAccount.get('AccountId') is not None:
			self.add_query_param('UserAccount.AccountId', UserAccount.get('AccountId'))
		if UserAccount.get('EmpId') is not None:
			self.add_query_param('UserAccount.EmpId', UserAccount.get('EmpId'))
		if UserAccount.get('ExpireTime') is not None:
			self.add_query_param('UserAccount.ExpireTime', UserAccount.get('ExpireTime'))
		if UserAccount.get('LoginName') is not None:
			self.add_query_param('UserAccount.LoginName', UserAccount.get('LoginName'))
		if UserAccount.get('Options') is not None:
			if UserAccount.get('Options').get('LoginLimit') is not None:
				self.add_query_param('UserAccount.Options.LoginLimit', UserAccount.get('Options').get('LoginLimit'))
		if UserAccount.get('AccountStructure') is not None:
			self.add_query_param('UserAccount.AccountStructure', UserAccount.get('AccountStructure'))
		if UserAccount.get('DurationSeconds') is not None:
			self.add_query_param('UserAccount.DurationSeconds', UserAccount.get('DurationSeconds'))
		if UserAccount.get('ParentId') is not None:
			self.add_query_param('UserAccount.ParentId', UserAccount.get('ParentId'))
		if UserAccount.get('AccountPlatform') is not None:
			self.add_query_param('UserAccount.AccountPlatform', UserAccount.get('AccountPlatform'))
