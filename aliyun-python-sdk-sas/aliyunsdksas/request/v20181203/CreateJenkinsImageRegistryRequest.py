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
from aliyunsdksas.endpoint import endpoint_data

class CreateJenkinsImageRegistryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'CreateJenkinsImageRegistry','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ExtraParam(self): # String
		return self.get_body_params().get('ExtraParam')

	def set_ExtraParam(self, ExtraParam):  # String
		self.add_body_params('ExtraParam', ExtraParam)
	def get_RegistryVersion(self): # String
		return self.get_body_params().get('RegistryVersion')

	def set_RegistryVersion(self, RegistryVersion):  # String
		self.add_body_params('RegistryVersion', RegistryVersion)
	def get_RegistryHostIp(self): # String
		return self.get_body_params().get('RegistryHostIp')

	def set_RegistryHostIp(self, RegistryHostIp):  # String
		self.add_body_params('RegistryHostIp', RegistryHostIp)
	def get_Password(self): # String
		return self.get_body_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_body_params('Password', Password)
	def get_SourceIp(self): # String
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self, SourceIp):  # String
		self.add_query_param('SourceIp', SourceIp)
	def get_RegistryName(self): # String
		return self.get_body_params().get('RegistryName')

	def set_RegistryName(self, RegistryName):  # String
		self.add_body_params('RegistryName', RegistryName)
	def get_TransPerHour(self): # Integer
		return self.get_body_params().get('TransPerHour')

	def set_TransPerHour(self, TransPerHour):  # Integer
		self.add_body_params('TransPerHour', TransPerHour)
	def get_RegistryType(self): # String
		return self.get_body_params().get('RegistryType')

	def set_RegistryType(self, RegistryType):  # String
		self.add_body_params('RegistryType', RegistryType)
	def get_DomainName(self): # String
		return self.get_body_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_body_params('DomainName', DomainName)
	def get_WhiteList(self): # String
		return self.get_body_params().get('WhiteList')

	def set_WhiteList(self, WhiteList):  # String
		self.add_body_params('WhiteList', WhiteList)
	def get_NetType(self): # Integer
		return self.get_body_params().get('NetType')

	def set_NetType(self, NetType):  # Integer
		self.add_body_params('NetType', NetType)
	def get_VpcId(self): # String
		return self.get_body_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_body_params('VpcId', VpcId)
	def get_PersistenceDay(self): # Integer
		return self.get_body_params().get('PersistenceDay')

	def set_PersistenceDay(self, PersistenceDay):  # Integer
		self.add_body_params('PersistenceDay', PersistenceDay)
	def get_ProtocolType(self): # Integer
		return self.get_body_params().get('ProtocolType')

	def set_ProtocolType(self, ProtocolType):  # Integer
		self.add_body_params('ProtocolType', ProtocolType)
	def get_UserName(self): # String
		return self.get_body_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_body_params('UserName', UserName)
