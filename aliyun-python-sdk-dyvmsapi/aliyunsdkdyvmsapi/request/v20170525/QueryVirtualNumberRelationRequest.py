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

class QueryVirtualNumberRelationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyvmsapi', '2017-05-25', 'QueryVirtualNumberRelation','dyvms')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SpecId(self):
		return self.get_query_params().get('SpecId')

	def set_SpecId(self,SpecId):
		self.add_query_param('SpecId',SpecId)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_RouteType(self):
		return self.get_query_params().get('RouteType')

	def set_RouteType(self,RouteType):
		self.add_query_param('RouteType',RouteType)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_RelatedNum(self):
		return self.get_query_params().get('RelatedNum')

	def set_RelatedNum(self,RelatedNum):
		self.add_query_param('RelatedNum',RelatedNum)

	def get_RegionNameCity(self):
		return self.get_query_params().get('RegionNameCity')

	def set_RegionNameCity(self,RegionNameCity):
		self.add_query_param('RegionNameCity',RegionNameCity)

	def get_QualificationId(self):
		return self.get_query_params().get('QualificationId')

	def set_QualificationId(self,QualificationId):
		self.add_query_param('QualificationId',QualificationId)

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

	def get_PageNo(self):
		return self.get_query_params().get('PageNo')

	def set_PageNo(self,PageNo):
		self.add_query_param('PageNo',PageNo)