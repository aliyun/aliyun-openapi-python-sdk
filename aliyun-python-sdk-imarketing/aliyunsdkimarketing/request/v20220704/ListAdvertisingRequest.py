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
import json

class ListAdvertisingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imarketing', '2022-07-04', 'ListAdvertising')
		self.set_method('GET')

	def get_App(self): # Struct
		return self.get_query_params().get('App')

	def set_App(self, App):  # Struct
		self.add_query_param("App", json.dumps(App))
	def get_Ext(self): # Map
		return self.get_query_params().get('Ext')

	def set_Ext(self, Ext):  # Map
		self.add_query_param("Ext", json.dumps(Ext))
	def get_Test(self): # Integer
		return self.get_query_params().get('Test')

	def set_Test(self, Test):  # Integer
		self.add_query_param('Test', Test)
	def get_Imp(self): # Array
		return self.get_query_params().get('Imp')

	def set_Imp(self, Imp):  # Array
		self.add_query_param("Imp", json.dumps(Imp))
	def get_Id(self): # String
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # String
		self.add_query_param('Id', Id)
	def get_User(self): # Struct
		return self.get_query_params().get('User')

	def set_User(self, User):  # Struct
		self.add_query_param("User", json.dumps(User))
	def get_Device(self): # Struct
		return self.get_query_params().get('Device')

	def set_Device(self, Device):  # Struct
		self.add_query_param("Device", json.dumps(Device))
	def get_Dealtype(self): # Integer
		return self.get_query_params().get('Dealtype')

	def set_Dealtype(self, Dealtype):  # Integer
		self.add_query_param('Dealtype', Dealtype)
