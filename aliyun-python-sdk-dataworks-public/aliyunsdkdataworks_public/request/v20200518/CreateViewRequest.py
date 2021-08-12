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

class CreateViewRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateView')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ViewName(self):
		return self.get_body_params().get('ViewName')

	def set_ViewName(self,ViewName):
		self.add_body_params('ViewName', ViewName)

	def get_ClientToken(self):
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_body_params('ClientToken', ClientToken)

	def get_SelectSQL(self):
		return self.get_body_params().get('SelectSQL')

	def set_SelectSQL(self,SelectSQL):
		self.add_body_params('SelectSQL', SelectSQL)

	def get_SelectWhere(self):
		return self.get_body_params().get('SelectWhere')

	def set_SelectWhere(self,SelectWhere):
		self.add_body_params('SelectWhere', SelectWhere)

	def get_SelectTableName(self):
		return self.get_body_params().get('SelectTableName')

	def set_SelectTableName(self,SelectTableName):
		self.add_body_params('SelectTableName', SelectTableName)

	def get_Comment(self):
		return self.get_body_params().get('Comment')

	def set_Comment(self,Comment):
		self.add_body_params('Comment', Comment)

	def get_SelectColumn(self):
		return self.get_body_params().get('SelectColumn')

	def set_SelectColumn(self,SelectColumn):
		self.add_body_params('SelectColumn', SelectColumn)

	def get_AppGuid(self):
		return self.get_body_params().get('AppGuid')

	def set_AppGuid(self,AppGuid):
		self.add_body_params('AppGuid', AppGuid)

	def get_ViewColumns(self):
		return self.get_body_params().get('ViewColumn')

	def set_ViewColumns(self, ViewColumns):
		for depth1 in range(len(ViewColumns)):
			if ViewColumns[depth1].get('Comment') is not None:
				self.add_body_params('ViewColumn.' + str(depth1 + 1) + '.Comment', ViewColumns[depth1].get('Comment'))
			if ViewColumns[depth1].get('ColumnName') is not None:
				self.add_body_params('ViewColumn.' + str(depth1 + 1) + '.ColumnName', ViewColumns[depth1].get('ColumnName'))