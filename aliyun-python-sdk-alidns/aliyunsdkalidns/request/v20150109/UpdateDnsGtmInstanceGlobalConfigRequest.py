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

class UpdateDnsGtmInstanceGlobalConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alidns', '2015-01-09', 'UpdateDnsGtmInstanceGlobalConfig','alidns')
		self.set_method('POST')

	def get_AlertGroup(self):
		return self.get_query_params().get('AlertGroup')

	def set_AlertGroup(self,AlertGroup):
		self.add_query_param('AlertGroup',AlertGroup)

	def get_CnameType(self):
		return self.get_query_params().get('CnameType')

	def set_CnameType(self,CnameType):
		self.add_query_param('CnameType',CnameType)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_AlertConfigs(self):
		return self.get_query_params().get('AlertConfig')

	def set_AlertConfigs(self, AlertConfigs):
		for depth1 in range(len(AlertConfigs)):
			if AlertConfigs[depth1].get('SmsNotice') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.SmsNotice', AlertConfigs[depth1].get('SmsNotice'))
			if AlertConfigs[depth1].get('NoticeType') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.NoticeType', AlertConfigs[depth1].get('NoticeType'))
			if AlertConfigs[depth1].get('EmailNotice') is not None:
				self.add_query_param('AlertConfig.' + str(depth1 + 1) + '.EmailNotice', AlertConfigs[depth1].get('EmailNotice'))

	def get_PublicCnameMode(self):
		return self.get_query_params().get('PublicCnameMode')

	def set_PublicCnameMode(self,PublicCnameMode):
		self.add_query_param('PublicCnameMode',PublicCnameMode)

	def get_PublicUserDomainName(self):
		return self.get_query_params().get('PublicUserDomainName')

	def set_PublicUserDomainName(self,PublicUserDomainName):
		self.add_query_param('PublicUserDomainName',PublicUserDomainName)

	def get_Ttl(self):
		return self.get_query_params().get('Ttl')

	def set_Ttl(self,Ttl):
		self.add_query_param('Ttl',Ttl)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_PublicZoneName(self):
		return self.get_query_params().get('PublicZoneName')

	def set_PublicZoneName(self,PublicZoneName):
		self.add_query_param('PublicZoneName',PublicZoneName)