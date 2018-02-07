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
class DescribeVulDetailsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aegis', '2016-11-11', 'DescribeVulDetails','vipaegis')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Product(self):
		return self.get_query_params().get('Product')

	def set_Product(self,Product):
		self.add_query_param('Product',Product)

	def get_StatusList(self):
		return self.get_query_params().get('StatusList')

	def set_StatusList(self,StatusList):
		self.add_query_param('StatusList',StatusList)

	def get_Level(self):
		return self.get_query_params().get('Level')

	def set_Level(self,Level):
		self.add_query_param('Level',Level)

	def get_Resource(self):
		return self.get_query_params().get('Resource')

	def set_Resource(self,Resource):
		self.add_query_param('Resource',Resource)

	def get_OrderBy(self):
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self,OrderBy):
		self.add_query_param('OrderBy',OrderBy)

	def get_Dealed(self):
		return self.get_query_params().get('Dealed')

	def set_Dealed(self,Dealed):
		self.add_query_param('Dealed',Dealed)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_LastTsEnd(self):
		return self.get_query_params().get('LastTsEnd')

	def set_LastTsEnd(self,LastTsEnd):
		self.add_query_param('LastTsEnd',LastTsEnd)

	def get_BatchName(self):
		return self.get_query_params().get('BatchName')

	def set_BatchName(self,BatchName):
		self.add_query_param('BatchName',BatchName)

	def get_PatchId(self):
		return self.get_query_params().get('PatchId')

	def set_PatchId(self,PatchId):
		self.add_query_param('PatchId',PatchId)

	def get_AliasName(self):
		return self.get_query_params().get('AliasName')

	def set_AliasName(self,AliasName):
		self.add_query_param('AliasName',AliasName)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_LastTsStart(self):
		return self.get_query_params().get('LastTsStart')

	def set_LastTsStart(self,LastTsStart):
		self.add_query_param('LastTsStart',LastTsStart)

	def get_Necessity(self):
		return self.get_query_params().get('Necessity')

	def set_Necessity(self,Necessity):
		self.add_query_param('Necessity',Necessity)

	def get_Uuids(self):
		return self.get_query_params().get('Uuids')

	def set_Uuids(self,Uuids):
		self.add_query_param('Uuids',Uuids)

	def get_Direction(self):
		return self.get_query_params().get('Direction')

	def set_Direction(self,Direction):
		self.add_query_param('Direction',Direction)