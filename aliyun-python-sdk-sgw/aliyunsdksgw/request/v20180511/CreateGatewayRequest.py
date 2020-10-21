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
from aliyunsdksgw.endpoint import endpoint_data

class CreateGatewayRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sgw', '2018-05-11', 'CreateGateway','hcs_sgw')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_GatewayClass(self):
		return self.get_query_params().get('GatewayClass')

	def set_GatewayClass(self,GatewayClass):
		self.add_query_param('GatewayClass',GatewayClass)

	def get_PostPaid(self):
		return self.get_query_params().get('PostPaid')

	def set_PostPaid(self,PostPaid):
		self.add_query_param('PostPaid',PostPaid)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_ReleaseAfterExpiration(self):
		return self.get_query_params().get('ReleaseAfterExpiration')

	def set_ReleaseAfterExpiration(self,ReleaseAfterExpiration):
		self.add_query_param('ReleaseAfterExpiration',ReleaseAfterExpiration)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_StorageBundleId(self):
		return self.get_query_params().get('StorageBundleId')

	def set_StorageBundleId(self,StorageBundleId):
		self.add_query_param('StorageBundleId',StorageBundleId)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Location(self):
		return self.get_query_params().get('Location')

	def set_Location(self,Location):
		self.add_query_param('Location',Location)

	def get_PublicNetworkBandwidth(self):
		return self.get_query_params().get('PublicNetworkBandwidth')

	def set_PublicNetworkBandwidth(self,PublicNetworkBandwidth):
		self.add_query_param('PublicNetworkBandwidth',PublicNetworkBandwidth)