# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateTrafficControlRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'CreateTrafficControl','apigateway')

	def get_ApiDefault(self):
		return self.get_query_params().get('ApiDefault')

	def set_ApiDefault(self,ApiDefault):
		self.add_query_param('ApiDefault',ApiDefault)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_TrafficControlName(self):
		return self.get_query_params().get('TrafficControlName')

	def set_TrafficControlName(self,TrafficControlName):
		self.add_query_param('TrafficControlName',TrafficControlName)

	def get_TrafficControlUnit(self):
		return self.get_query_params().get('TrafficControlUnit')

	def set_TrafficControlUnit(self,TrafficControlUnit):
		self.add_query_param('TrafficControlUnit',TrafficControlUnit)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_UserDefault(self):
		return self.get_query_params().get('UserDefault')

	def set_UserDefault(self,UserDefault):
		self.add_query_param('UserDefault',UserDefault)

	def get_AppDefault(self):
		return self.get_query_params().get('AppDefault')

	def set_AppDefault(self,AppDefault):
		self.add_query_param('AppDefault',AppDefault)