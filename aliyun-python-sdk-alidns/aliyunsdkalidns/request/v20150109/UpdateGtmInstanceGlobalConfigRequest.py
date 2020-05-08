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
from aliyunsdkalidns.endpoint import endpoint_data

class UpdateGtmInstanceGlobalConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alidns', '2015-01-09', 'UpdateGtmInstanceGlobalConfig','alidns')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AlertGroup(self):
		return self.get_query_params().get('AlertGroup')

	def set_AlertGroup(self,AlertGroup):
		self.add_query_param('AlertGroup',AlertGroup)

	def get_CnameMode(self):
		return self.get_query_params().get('CnameMode')

	def set_CnameMode(self,CnameMode):
		self.add_query_param('CnameMode',CnameMode)

	def get_LbaStrategy(self):
		return self.get_query_params().get('LbaStrategy')

	def set_LbaStrategy(self,LbaStrategy):
		self.add_query_param('LbaStrategy',LbaStrategy)

	def get_Ttl(self):
		return self.get_query_params().get('Ttl')

	def set_Ttl(self,Ttl):
		self.add_query_param('Ttl',Ttl)

	def get_CnameCustomDomainName(self):
		return self.get_query_params().get('CnameCustomDomainName')

	def set_CnameCustomDomainName(self,CnameCustomDomainName):
		self.add_query_param('CnameCustomDomainName',CnameCustomDomainName)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_UserDomainName(self):
		return self.get_query_params().get('UserDomainName')

	def set_UserDomainName(self,UserDomainName):
		self.add_query_param('UserDomainName',UserDomainName)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)