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

class CreateMySqlDataSourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'CreateMySqlDataSource','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Schema(self): # String
		return self.get_body_params().get('Schema')

	def set_Schema(self, Schema):  # String
		self.add_body_params('Schema', Schema)
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
	def get_DgInstanceId(self): # String
		return self.get_body_params().get('DgInstanceId')

	def set_DgInstanceId(self, DgInstanceId):  # String
		self.add_body_params('DgInstanceId', DgInstanceId)
	def get_Ip(self): # String
		return self.get_body_params().get('Ip')

	def set_Ip(self, Ip):  # String
		self.add_body_params('Ip', Ip)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
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
	def get_UserName(self): # String
		return self.get_body_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_body_params('UserName', UserName)
