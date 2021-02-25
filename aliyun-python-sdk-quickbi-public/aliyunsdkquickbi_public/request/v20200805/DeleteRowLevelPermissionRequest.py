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
from aliyunsdkquickbi_public.endpoint import endpoint_data

class DeleteRowLevelPermissionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2020-08-05', 'DeleteRowLevelPermission','quickbi')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TargetTypes(self):
		return self.get_query_params().get('TargetTypes')

	def set_TargetTypes(self,TargetTypes):
		self.add_query_param('TargetTypes',TargetTypes)

	def get_TargetIds(self):
		return self.get_query_params().get('TargetIds')

	def set_TargetIds(self,TargetIds):
		self.add_query_param('TargetIds',TargetIds)

	def get_ColumnIds(self):
		return self.get_query_params().get('ColumnIds')

	def set_ColumnIds(self,ColumnIds):
		self.add_query_param('ColumnIds',ColumnIds)

	def get_DatasetId(self):
		return self.get_query_params().get('DatasetId')

	def set_DatasetId(self,DatasetId):
		self.add_query_param('DatasetId',DatasetId)

	def get_DeleteType(self):
		return self.get_query_params().get('DeleteType')

	def set_DeleteType(self,DeleteType):
		self.add_query_param('DeleteType',DeleteType)