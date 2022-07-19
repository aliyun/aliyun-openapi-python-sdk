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

class CreateTableRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateTable')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Schema(self): # String
		return self.get_query_params().get('Schema')

	def set_Schema(self, Schema):  # String
		self.add_query_param('Schema', Schema)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Columnss(self): # RepeatList
		return self.get_body_params().get('Columns')

	def set_Columnss(self, Columns):  # RepeatList
		for depth1 in range(len(Columns)):
			if Columns[depth1].get('SeqNumber') is not None:
				self.add_body_params('Columns.' + str(depth1 + 1) + '.SeqNumber', Columns[depth1].get('SeqNumber'))
			if Columns[depth1].get('IsPartitionCol') is not None:
				self.add_body_params('Columns.' + str(depth1 + 1) + '.IsPartitionCol', Columns[depth1].get('IsPartitionCol'))
			if Columns[depth1].get('ColumnNameCn') is not None:
				self.add_body_params('Columns.' + str(depth1 + 1) + '.ColumnNameCn', Columns[depth1].get('ColumnNameCn'))
			if Columns[depth1].get('Length') is not None:
				self.add_body_params('Columns.' + str(depth1 + 1) + '.Length', Columns[depth1].get('Length'))
			if Columns[depth1].get('Comment') is not None:
				self.add_body_params('Columns.' + str(depth1 + 1) + '.Comment', Columns[depth1].get('Comment'))
			if Columns[depth1].get('ColumnName') is not None:
				self.add_body_params('Columns.' + str(depth1 + 1) + '.ColumnName', Columns[depth1].get('ColumnName'))
			if Columns[depth1].get('ColumnType') is not None:
				self.add_body_params('Columns.' + str(depth1 + 1) + '.ColumnType', Columns[depth1].get('ColumnType'))
	def get_LifeCycle(self): # Integer
		return self.get_query_params().get('LifeCycle')

	def set_LifeCycle(self, LifeCycle):  # Integer
		self.add_query_param('LifeCycle', LifeCycle)
	def get_Themess(self): # RepeatList
		return self.get_body_params().get('Themes')

	def set_Themess(self, Themes):  # RepeatList
		for depth1 in range(len(Themes)):
			if Themes[depth1].get('ThemeLevel') is not None:
				self.add_body_params('Themes.' + str(depth1 + 1) + '.ThemeLevel', Themes[depth1].get('ThemeLevel'))
			if Themes[depth1].get('ThemeId') is not None:
				self.add_body_params('Themes.' + str(depth1 + 1) + '.ThemeId', Themes[depth1].get('ThemeId'))
	def get_LogicalLevelId(self): # Long
		return self.get_query_params().get('LogicalLevelId')

	def set_LogicalLevelId(self, LogicalLevelId):  # Long
		self.add_query_param('LogicalLevelId', LogicalLevelId)
	def get_Endpoint(self): # String
		return self.get_body_params().get('Endpoint')

	def set_Endpoint(self, Endpoint):  # String
		self.add_body_params('Endpoint', Endpoint)
	def get_EnvType(self): # Integer
		return self.get_body_params().get('EnvType')

	def set_EnvType(self, EnvType):  # Integer
		self.add_body_params('EnvType', EnvType)
	def get_HasPart(self): # Integer
		return self.get_query_params().get('HasPart')

	def set_HasPart(self, HasPart):  # Integer
		self.add_query_param('HasPart', HasPart)
	def get_TableName(self): # String
		return self.get_query_params().get('TableName')

	def set_TableName(self, TableName):  # String
		self.add_query_param('TableName', TableName)
	def get_AppGuid(self): # String
		return self.get_query_params().get('AppGuid')

	def set_AppGuid(self, AppGuid):  # String
		self.add_query_param('AppGuid', AppGuid)
	def get_ProjectId(self): # Long
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_query_param('ProjectId', ProjectId)
	def get_CategoryId(self): # Long
		return self.get_query_params().get('CategoryId')

	def set_CategoryId(self, CategoryId):  # Long
		self.add_query_param('CategoryId', CategoryId)
	def get_Visibility(self): # Integer
		return self.get_query_params().get('Visibility')

	def set_Visibility(self, Visibility):  # Integer
		self.add_query_param('Visibility', Visibility)
	def get_PhysicsLevelId(self): # Long
		return self.get_query_params().get('PhysicsLevelId')

	def set_PhysicsLevelId(self, PhysicsLevelId):  # Long
		self.add_query_param('PhysicsLevelId', PhysicsLevelId)
	def get_OwnerId(self): # String
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # String
		self.add_query_param('OwnerId', OwnerId)
	def get_IsView(self): # Integer
		return self.get_query_params().get('IsView')

	def set_IsView(self, IsView):  # Integer
		self.add_query_param('IsView', IsView)
	def get_ExternalTableType(self): # String
		return self.get_query_params().get('ExternalTableType')

	def set_ExternalTableType(self, ExternalTableType):  # String
		self.add_query_param('ExternalTableType', ExternalTableType)
	def get_Location(self): # String
		return self.get_query_params().get('Location')

	def set_Location(self, Location):  # String
		self.add_query_param('Location', Location)
	def get_Comment(self): # String
		return self.get_query_params().get('Comment')

	def set_Comment(self, Comment):  # String
		self.add_query_param('Comment', Comment)
