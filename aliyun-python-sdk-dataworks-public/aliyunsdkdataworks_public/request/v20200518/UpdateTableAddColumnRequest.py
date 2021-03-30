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

class UpdateTableAddColumnRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'UpdateTableAddColumn')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TableGuid(self):
		return self.get_query_params().get('TableGuid')

	def set_TableGuid(self,TableGuid):
		self.add_query_param('TableGuid',TableGuid)

	def get_Columns(self):
		return self.get_body_params().get('Column')

	def set_Columns(self, Columns):
		for depth1 in range(len(Columns)):
			if Columns[depth1].get('ColumnNameCn') is not None:
				self.add_body_params('Column.' + str(depth1 + 1) + '.ColumnNameCn', Columns[depth1].get('ColumnNameCn'))
			if Columns[depth1].get('Comment') is not None:
				self.add_body_params('Column.' + str(depth1 + 1) + '.Comment', Columns[depth1].get('Comment'))
			if Columns[depth1].get('ColumnName') is not None:
				self.add_body_params('Column.' + str(depth1 + 1) + '.ColumnName', Columns[depth1].get('ColumnName'))
			if Columns[depth1].get('ColumnType') is not None:
				self.add_body_params('Column.' + str(depth1 + 1) + '.ColumnType', Columns[depth1].get('ColumnType'))