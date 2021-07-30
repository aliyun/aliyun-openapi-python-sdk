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

class AddVirtualNumberRelationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyvmsapi', '2017-05-25', 'AddVirtualNumberRelation','dyvms')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_NumberList(self):
		return self.get_query_params().get('NumberList')

	def set_NumberList(self,NumberList):
		self.add_query_param('NumberList',NumberList)

	def get_RouteType(self):
		return self.get_query_params().get('RouteType')

	def set_RouteType(self,RouteType):
		self.add_query_param('RouteType',RouteType)

	def get_CorpNameList(self):
		return self.get_query_params().get('CorpNameList')

	def set_CorpNameList(self,CorpNameList):
		self.add_query_param('CorpNameList',CorpNameList)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ProdCode(self):
		return self.get_query_params().get('ProdCode')

	def set_ProdCode(self,ProdCode):
		self.add_query_param('ProdCode',ProdCode)

	def get_PhoneNum(self):
		return self.get_query_params().get('PhoneNum')

	def set_PhoneNum(self,PhoneNum):
		self.add_query_param('PhoneNum',PhoneNum)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)