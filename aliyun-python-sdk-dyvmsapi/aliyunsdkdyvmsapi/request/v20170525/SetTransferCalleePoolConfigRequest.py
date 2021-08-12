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
from aliyunsdkdyvmsapi.endpoint import endpoint_data

class SetTransferCalleePoolConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyvmsapi', '2017-05-25', 'SetTransferCalleePoolConfig','dyvms')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PhoneNumber(self):
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self,PhoneNumber):
		self.add_query_param('PhoneNumber',PhoneNumber)

	def get_Detailss(self):
		return self.get_query_params().get('Details')

	def set_Detailss(self, Detailss):
		for depth1 in range(len(Detailss)):
			if Detailss[depth1].get('Caller') is not None:
				self.add_query_param('Details.' + str(depth1 + 1) + '.Caller', Detailss[depth1].get('Caller'))
			if Detailss[depth1].get('Called') is not None:
				self.add_query_param('Details.' + str(depth1 + 1) + '.Called', Detailss[depth1].get('Called'))

	def get_CalledRouteMode(self):
		return self.get_query_params().get('CalledRouteMode')

	def set_CalledRouteMode(self,CalledRouteMode):
		self.add_query_param('CalledRouteMode',CalledRouteMode)

	def get_QualificationId(self):
		return self.get_query_params().get('QualificationId')

	def set_QualificationId(self,QualificationId):
		self.add_query_param('QualificationId',QualificationId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)