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

class GetUserDatabasesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-dg', '2023-09-14', 'GetUserDatabases')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_SearchKey(self): # String
		return self.get_body_params().get('SearchKey')

	def set_SearchKey(self, SearchKey):  # String
		self.add_body_params('SearchKey', SearchKey)
	def get_PageNumber(self): # String
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # String
		self.add_body_params('PageNumber', PageNumber)
	def get_PageSize(self): # String
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_body_params('PageSize', PageSize)
	def get_Host(self): # String
		return self.get_body_params().get('Host')

	def set_Host(self, Host):  # String
		self.add_body_params('Host', Host)
	def get_GatewayId(self): # String
		return self.get_body_params().get('GatewayId')

	def set_GatewayId(self, GatewayId):  # String
		self.add_body_params('GatewayId', GatewayId)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_Port(self): # Integer
		return self.get_body_params().get('Port')

	def set_Port(self, Port):  # Integer
		self.add_body_params('Port', Port)
	def get_DbType(self): # String
		return self.get_body_params().get('DbType')

	def set_DbType(self, DbType):  # String
		self.add_body_params('DbType', DbType)
