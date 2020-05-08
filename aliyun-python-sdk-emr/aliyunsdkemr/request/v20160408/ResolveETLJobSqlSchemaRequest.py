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
from aliyunsdkemr.endpoint import endpoint_data

class ResolveETLJobSqlSchemaRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ResolveETLJobSqlSchema','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StageName(self):
		return self.get_query_params().get('StageName')

	def set_StageName(self,StageName):
		self.add_query_param('StageName',StageName)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_EtlJobId(self):
		return self.get_query_params().get('EtlJobId')

	def set_EtlJobId(self,EtlJobId):
		self.add_query_param('EtlJobId',EtlJobId)

	def get_DataSourceId(self):
		return self.get_query_params().get('DataSourceId')

	def set_DataSourceId(self,DataSourceId):
		self.add_query_param('DataSourceId',DataSourceId)

	def get_Sql(self):
		return self.get_query_params().get('Sql')

	def set_Sql(self,Sql):
		self.add_query_param('Sql',Sql)