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

class CreateSubnetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eflo', '2022-05-30', 'CreateSubnet','eflo')
		self.set_method('POST')

	def get_Type(self): # String
		return self.get_body_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_body_params('Type', Type)
	def get_VpdId(self): # String
		return self.get_body_params().get('VpdId')

	def set_VpdId(self, VpdId):  # String
		self.add_body_params('VpdId', VpdId)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_ZoneId(self): # String
		return self.get_body_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_body_params('ZoneId', ZoneId)
	def get_Cidr(self): # String
		return self.get_body_params().get('Cidr')

	def set_Cidr(self, Cidr):  # String
		self.add_body_params('Cidr', Cidr)
