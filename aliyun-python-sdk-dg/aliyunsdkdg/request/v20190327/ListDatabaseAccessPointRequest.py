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

class ListDatabaseAccessPointRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dg', '2019-03-27', 'ListDatabaseAccessPoint','dg')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SearchKey(self):
		return self.get_body_params().get('SearchKey')

	def set_SearchKey(self,SearchKey):
		self.add_body_params('SearchKey', SearchKey)

	def get_PageNumber(self):
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_body_params('PageNumber', PageNumber)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_Host(self):
		return self.get_body_params().get('Host')

	def set_Host(self,Host):
		self.add_body_params('Host', Host)

	def get_DbInstanceId(self):
		return self.get_body_params().get('DbInstanceId')

	def set_DbInstanceId(self,DbInstanceId):
		self.add_body_params('DbInstanceId', DbInstanceId)

	def get_GatewayId(self):
		return self.get_body_params().get('GatewayId')

	def set_GatewayId(self,GatewayId):
		self.add_body_params('GatewayId', GatewayId)

	def get_Port(self):
		return self.get_body_params().get('Port')

	def set_Port(self,Port):
		self.add_body_params('Port', Port)

	def get_VpcId(self):
		return self.get_body_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_body_params('VpcId', VpcId)