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
from aliyunsdkdg.endpoint import endpoint_data

class RetryDatabaseRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dg', '2019-03-27', 'RetryDatabase','dg')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientToken(self):
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_body_params('ClientToken', ClientToken)

	def get_Host(self):
		return self.get_body_params().get('Host')

	def set_Host(self,Host):
		self.add_body_params('Host', Host)

	def get_DbUserName(self):
		return self.get_body_params().get('DbUserName')

	def set_DbUserName(self,DbUserName):
		self.add_body_params('DbUserName', DbUserName)

	def get_DbDescription(self):
		return self.get_body_params().get('DbDescription')

	def set_DbDescription(self,DbDescription):
		self.add_body_params('DbDescription', DbDescription)

	def get_GatewayId(self):
		return self.get_body_params().get('GatewayId')

	def set_GatewayId(self,GatewayId):
		self.add_body_params('GatewayId', GatewayId)

	def get_DbName(self):
		return self.get_body_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_body_params('DbName', DbName)

	def get_Port(self):
		return self.get_body_params().get('Port')

	def set_Port(self,Port):
		self.add_body_params('Port', Port)

	def get_DbPassword(self):
		return self.get_body_params().get('DbPassword')

	def set_DbPassword(self,DbPassword):
		self.add_body_params('DbPassword', DbPassword)

	def get_DbType(self):
		return self.get_body_params().get('DbType')

	def set_DbType(self,DbType):
		self.add_body_params('DbType', DbType)