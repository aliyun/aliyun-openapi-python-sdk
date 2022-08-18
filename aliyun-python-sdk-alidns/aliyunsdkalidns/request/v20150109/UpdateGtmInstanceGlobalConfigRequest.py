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
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AlertGroup(self): # String
		return self.get_query_params().get('AlertGroup')

	def set_AlertGroup(self, AlertGroup):  # String
		self.add_query_param('AlertGroup', AlertGroup)
	def get_CnameMode(self): # String
		return self.get_query_params().get('CnameMode')

	def set_CnameMode(self, CnameMode):  # String
		self.add_query_param('CnameMode', CnameMode)
	def get_LbaStrategy(self): # String
		return self.get_query_params().get('LbaStrategy')

	def set_LbaStrategy(self, LbaStrategy):  # String
		self.add_query_param('LbaStrategy', LbaStrategy)
	def get_Ttl(self): # Integer
		return self.get_query_params().get('Ttl')

	def set_Ttl(self, Ttl):  # Integer
		self.add_query_param('Ttl', Ttl)
	def get_CnameCustomDomainName(self): # String
		return self.get_query_params().get('CnameCustomDomainName')

	def set_CnameCustomDomainName(self, CnameCustomDomainName):  # String
		self.add_query_param('CnameCustomDomainName', CnameCustomDomainName)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_InstanceName(self): # String
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_query_param('InstanceName', InstanceName)
	def get_UserDomainName(self): # String
		return self.get_query_params().get('UserDomainName')

	def set_UserDomainName(self, UserDomainName):  # String
		self.add_query_param('UserDomainName', UserDomainName)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
