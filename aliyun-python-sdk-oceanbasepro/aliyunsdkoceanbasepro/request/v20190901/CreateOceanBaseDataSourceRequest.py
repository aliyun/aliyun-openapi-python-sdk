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
from aliyunsdkoceanbasepro.endpoint import endpoint_data

class CreateOceanBaseDataSourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'CreateOceanBaseDataSource','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Cluster(self): # String
		return self.get_body_params().get('Cluster')

	def set_Cluster(self, Cluster):  # String
		self.add_body_params('Cluster', Cluster)
	def get_DrcUserName(self): # String
		return self.get_body_params().get('DrcUserName')

	def set_DrcUserName(self, DrcUserName):  # String
		self.add_body_params('DrcUserName', DrcUserName)
	def get_LogProxyIp(self): # String
		return self.get_body_params().get('LogProxyIp')

	def set_LogProxyIp(self, LogProxyIp):  # String
		self.add_body_params('LogProxyIp', LogProxyIp)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_Type(self): # String
		return self.get_body_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_body_params('Type', Type)
	def get_Password(self): # String
		return self.get_body_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_body_params('Password', Password)
	def get_InnerDrcPassword(self): # String
		return self.get_body_params().get('InnerDrcPassword')

	def set_InnerDrcPassword(self, InnerDrcPassword):  # String
		self.add_body_params('InnerDrcPassword', InnerDrcPassword)
	def get_Tenant(self): # String
		return self.get_body_params().get('Tenant')

	def set_Tenant(self, Tenant):  # String
		self.add_body_params('Tenant', Tenant)
	def get_ConfigUrl(self): # String
		return self.get_body_params().get('ConfigUrl')

	def set_ConfigUrl(self, ConfigUrl):  # String
		self.add_body_params('ConfigUrl', ConfigUrl)
	def get_Ip(self): # String
		return self.get_body_params().get('Ip')

	def set_Ip(self, Ip):  # String
		self.add_body_params('Ip', Ip)
	def get_Port(self): # Integer
		return self.get_body_params().get('Port')

	def set_Port(self, Port):  # Integer
		self.add_body_params('Port', Port)
	def get_VpcId(self): # String
		return self.get_body_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_body_params('VpcId', VpcId)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_DrcPassword(self): # String
		return self.get_body_params().get('DrcPassword')

	def set_DrcPassword(self, DrcPassword):  # String
		self.add_body_params('DrcPassword', DrcPassword)
	def get_LogProxyPort(self): # String
		return self.get_body_params().get('LogProxyPort')

	def set_LogProxyPort(self, LogProxyPort):  # String
		self.add_body_params('LogProxyPort', LogProxyPort)
	def get_UserName(self): # String
		return self.get_body_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_body_params('UserName', UserName)
