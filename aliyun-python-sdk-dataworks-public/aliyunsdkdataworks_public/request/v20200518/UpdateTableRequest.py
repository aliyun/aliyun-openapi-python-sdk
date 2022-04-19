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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class UpdateTableRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'UpdateTable')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Columnss(self):
		return self.get_body_params().get('Columns')

	def set_Columnss(self, Columnss):
		for depth1 in range(len(Columnss)):
			if Columnss[depth1].get('SeqNumber') is not None:
				self.add_body_params('Columns.' + str(depth1 + 1) + '.SeqNumber', Columnss[depth1].get('SeqNumber'))
			if Columnss[depth1].get('IsPartitionCol') is not None:
				self.add_body_params('Columns.' + str(depth1 + 1) + '.IsPartitionCol', Columnss[depth1].get('IsPartitionCol'))
			if Columnss[depth1].get('ColumnNameCn') is not None:
				self.add_body_params('Columns.' + str(depth1 + 1) + '.ColumnNameCn', Columnss[depth1].get('ColumnNameCn'))
			if Columnss[depth1].get('Length') is not None:
				self.add_body_params('Columns.' + str(depth1 + 1) + '.Length', Columnss[depth1].get('Length'))
			if Columnss[depth1].get('Comment') is not None:
				self.add_body_params('Columns.' + str(depth1 + 1) + '.Comment', Columnss[depth1].get('Comment'))
			if Columnss[depth1].get('ColumnName') is not None:
				self.add_body_params('Columns.' + str(depth1 + 1) + '.ColumnName', Columnss[depth1].get('ColumnName'))
			if Columnss[depth1].get('ColumnType') is not None:
				self.add_body_params('Columns.' + str(depth1 + 1) + '.ColumnType', Columnss[depth1].get('ColumnType'))

	def get_LifeCycle(self):
		return self.get_query_params().get('LifeCycle')

	def set_LifeCycle(self,LifeCycle):
		self.add_query_param('LifeCycle',LifeCycle)

	def get_Themess(self):
		return self.get_body_params().get('Themes')

	def set_Themess(self, Themess):
		for depth1 in range(len(Themess)):
			if Themess[depth1].get('ThemeLevel') is not None:
				self.add_body_params('Themes.' + str(depth1 + 1) + '.ThemeLevel', Themess[depth1].get('ThemeLevel'))
			if Themess[depth1].get('ThemeId') is not None:
				self.add_body_params('Themes.' + str(depth1 + 1) + '.ThemeId', Themess[depth1].get('ThemeId'))

	def get_LogicalLevelId(self):
		return self.get_query_params().get('LogicalLevelId')

	def set_LogicalLevelId(self,LogicalLevelId):
		self.add_query_param('LogicalLevelId',LogicalLevelId)

	def get_Endpoint(self):
		return self.get_body_params().get('Endpoint')

	def set_Endpoint(self,Endpoint):
		self.add_body_params('Endpoint', Endpoint)

	def get_EnvType(self):
		return self.get_body_params().get('EnvType')

	def set_EnvType(self,EnvType):
		self.add_body_params('EnvType', EnvType)

	def get_HasPart(self):
		return self.get_query_params().get('HasPart')

	def set_HasPart(self,HasPart):
		self.add_query_param('HasPart',HasPart)

	def get_TableName(self):
		return self.get_query_params().get('TableName')

	def set_TableName(self,TableName):
		self.add_query_param('TableName',TableName)

	def get_AppGuid(self):
		return self.get_query_params().get('AppGuid')

	def set_AppGuid(self,AppGuid):
		self.add_query_param('AppGuid',AppGuid)

	def get_ProjectId(self):
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_query_param('ProjectId',ProjectId)

	def get_CategoryId(self):
		return self.get_query_params().get('CategoryId')

	def set_CategoryId(self,CategoryId):
		self.add_query_param('CategoryId',CategoryId)

	def get_Visibility(self):
		return self.get_query_params().get('Visibility')

	def set_Visibility(self,Visibility):
		self.add_query_param('Visibility',Visibility)

	def get_PhysicsLevelId(self):
		return self.get_query_params().get('PhysicsLevelId')

	def set_PhysicsLevelId(self,PhysicsLevelId):
		self.add_query_param('PhysicsLevelId',PhysicsLevelId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_IsView(self):
		return self.get_query_params().get('IsView')

	def set_IsView(self,IsView):
		self.add_query_param('IsView',IsView)

	def get_ExternalTableType(self):
		return self.get_query_params().get('ExternalTableType')

	def set_ExternalTableType(self,ExternalTableType):
		self.add_query_param('ExternalTableType',ExternalTableType)

	def get_Location(self):
		return self.get_query_params().get('Location')

	def set_Location(self,Location):
		self.add_query_param('Location',Location)

	def get_Comment(self):
		return self.get_query_params().get('Comment')

	def set_Comment(self,Comment):
		self.add_query_param('Comment',Comment)

	def get_CreateIfNotExists(self):
		return self.get_query_params().get('CreateIfNotExists')

	def set_CreateIfNotExists(self,CreateIfNotExists):
		self.add_query_param('CreateIfNotExists',CreateIfNotExists)