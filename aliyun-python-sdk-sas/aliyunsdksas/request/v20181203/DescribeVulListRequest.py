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
from aliyunsdksas.endpoint import endpoint_data

class DescribeVulListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeVulList','sas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TargetType(self):
		return self.get_query_params().get('TargetType')

	def set_TargetType(self,TargetType):
		self.add_query_param('TargetType',TargetType)

	def get_MinScore(self):
		return self.get_query_params().get('MinScore')

	def set_MinScore(self,MinScore):
		self.add_query_param('MinScore',MinScore)

	def get_Remark(self):
		return self.get_query_params().get('Remark')

	def set_Remark(self,Remark):
		self.add_query_param('Remark',Remark)

	def get_AttachTypes(self):
		return self.get_query_params().get('AttachTypes')

	def set_AttachTypes(self,AttachTypes):
		self.add_query_param('AttachTypes',AttachTypes)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_VpcInstanceIds(self):
		return self.get_query_params().get('VpcInstanceIds')

	def set_VpcInstanceIds(self,VpcInstanceIds):
		self.add_query_param('VpcInstanceIds',VpcInstanceIds)

	def get_CreateTsStart(self):
		return self.get_query_params().get('CreateTsStart')

	def set_CreateTsStart(self,CreateTsStart):
		self.add_query_param('CreateTsStart',CreateTsStart)

	def get_ContainerFieldName(self):
		return self.get_query_params().get('ContainerFieldName')

	def set_ContainerFieldName(self,ContainerFieldName):
		self.add_query_param('ContainerFieldName',ContainerFieldName)

	def get_ContainerFieldValue(self):
		return self.get_query_params().get('ContainerFieldValue')

	def set_ContainerFieldValue(self,ContainerFieldValue):
		self.add_query_param('ContainerFieldValue',ContainerFieldValue)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ModifyTsStart(self):
		return self.get_query_params().get('ModifyTsStart')

	def set_ModifyTsStart(self,ModifyTsStart):
		self.add_query_param('ModifyTsStart',ModifyTsStart)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_ModifyTsEnd(self):
		return self.get_query_params().get('ModifyTsEnd')

	def set_ModifyTsEnd(self,ModifyTsEnd):
		self.add_query_param('ModifyTsEnd',ModifyTsEnd)

	def get_Level(self):
		return self.get_query_params().get('Level')

	def set_Level(self,Level):
		self.add_query_param('Level',Level)

	def get_Resource(self):
		return self.get_query_params().get('Resource')

	def set_Resource(self,Resource):
		self.add_query_param('Resource',Resource)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_Dealed(self):
		return self.get_query_params().get('Dealed')

	def set_Dealed(self,Dealed):
		self.add_query_param('Dealed',Dealed)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_BatchName(self):
		return self.get_query_params().get('BatchName')

	def set_BatchName(self,BatchName):
		self.add_query_param('BatchName',BatchName)

	def get_AliasName(self):
		return self.get_query_params().get('AliasName')

	def set_AliasName(self,AliasName):
		self.add_query_param('AliasName',AliasName)

	def get_CreateTsEnd(self):
		return self.get_query_params().get('CreateTsEnd')

	def set_CreateTsEnd(self,CreateTsEnd):
		self.add_query_param('CreateTsEnd',CreateTsEnd)

	def get_Necessity(self):
		return self.get_query_params().get('Necessity')

	def set_Necessity(self,Necessity):
		self.add_query_param('Necessity',Necessity)

	def get_Uuids(self):
		return self.get_query_params().get('Uuids')

	def set_Uuids(self,Uuids):
		self.add_query_param('Uuids',Uuids)