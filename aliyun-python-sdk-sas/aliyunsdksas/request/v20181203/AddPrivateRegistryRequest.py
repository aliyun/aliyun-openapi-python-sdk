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

class AddPrivateRegistryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'AddPrivateRegistry','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ExtraParam(self): # String
		return self.get_query_params().get('ExtraParam')

	def set_ExtraParam(self, ExtraParam):  # String
		self.add_query_param('ExtraParam', ExtraParam)
	def get_RegistryVersion(self): # String
		return self.get_query_params().get('RegistryVersion')

	def set_RegistryVersion(self, RegistryVersion):  # String
		self.add_query_param('RegistryVersion', RegistryVersion)
	def get_RegistryHostIp(self): # String
		return self.get_query_params().get('RegistryHostIp')

	def set_RegistryHostIp(self, RegistryHostIp):  # String
		self.add_query_param('RegistryHostIp', RegistryHostIp)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_RegistryRegionId(self): # String
		return self.get_query_params().get('RegistryRegionId')

	def set_RegistryRegionId(self, RegistryRegionId):  # String
		self.add_query_param('RegistryRegionId', RegistryRegionId)
	def get_TransPerHour(self): # Integer
		return self.get_query_params().get('TransPerHour')

	def set_TransPerHour(self, TransPerHour):  # Integer
		self.add_query_param('TransPerHour', TransPerHour)
	def get_RegistryType(self): # String
		return self.get_query_params().get('RegistryType')

	def set_RegistryType(self, RegistryType):  # String
		self.add_query_param('RegistryType', RegistryType)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_Port(self): # Integer
		return self.get_query_params().get('Port')

	def set_Port(self, Port):  # Integer
		self.add_query_param('Port', Port)
	def get_NetType(self): # Long
		return self.get_query_params().get('NetType')

	def set_NetType(self, NetType):  # Long
		self.add_query_param('NetType', NetType)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_ProtocolType(self): # Long
		return self.get_query_params().get('ProtocolType')

	def set_ProtocolType(self, ProtocolType):  # Long
		self.add_query_param('ProtocolType', ProtocolType)
	def get_UserName(self): # String
		return self.get_query_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_query_param('UserName', UserName)
