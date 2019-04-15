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
class CreateOrUpdateDataSourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aegis', '2016-11-11', 'CreateOrUpdateDataSource','vipaegis')

	def get_ProjectName(self):
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self,ProjectName):
		self.add_query_param('ProjectName',ProjectName)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_LogStoreName(self):
		return self.get_query_params().get('LogStoreName')

	def set_LogStoreName(self,LogStoreName):
		self.add_query_param('LogStoreName',LogStoreName)

	def get_DatasourceDescription(self):
		return self.get_query_params().get('DatasourceDescription')

	def set_DatasourceDescription(self,DatasourceDescription):
		self.add_query_param('DatasourceDescription',DatasourceDescription)

	def get_Fields(self):
		return self.get_query_params().get('Fields')

	def set_Fields(self,Fields):
		self.add_query_param('Fields',Fields)

	def get_RegionNo(self):
		return self.get_query_params().get('RegionNo')

	def set_RegionNo(self,RegionNo):
		self.add_query_param('RegionNo',RegionNo)