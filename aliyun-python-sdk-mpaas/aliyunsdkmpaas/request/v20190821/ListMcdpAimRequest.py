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
from aliyunsdkmpaas.endpoint import endpoint_data

class ListMcdpAimRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mPaaS', '2019-08-21', 'ListMcdpAim')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Type(self):
		return self.get_body_params().get('Type')

	def set_Type(self,Type):
		self.add_body_params('Type', Type)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_TenantId(self):
		return self.get_body_params().get('TenantId')

	def set_TenantId(self,TenantId):
		self.add_body_params('TenantId', TenantId)

	def get_Keyword(self):
		return self.get_body_params().get('Keyword')

	def set_Keyword(self,Keyword):
		self.add_body_params('Keyword', Keyword)

	def get_Sort(self):
		return self.get_body_params().get('Sort')

	def set_Sort(self,Sort):
		self.add_body_params('Sort', Sort)

	def get_EmptyTag(self):
		return self.get_body_params().get('EmptyTag')

	def set_EmptyTag(self,EmptyTag):
		self.add_body_params('EmptyTag', EmptyTag)

	def get_PageNo(self):
		return self.get_body_params().get('PageNo')

	def set_PageNo(self,PageNo):
		self.add_body_params('PageNo', PageNo)

	def get_AppId(self):
		return self.get_body_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_body_params('AppId', AppId)

	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)

	def get_SortField(self):
		return self.get_body_params().get('SortField')

	def set_SortField(self,SortField):
		self.add_body_params('SortField', SortField)

	def get_WorkspaceId(self):
		return self.get_body_params().get('WorkspaceId')

	def set_WorkspaceId(self,WorkspaceId):
		self.add_body_params('WorkspaceId', WorkspaceId)