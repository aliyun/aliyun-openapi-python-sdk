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
from aliyunsdkhbase.endpoint import endpoint_data

class CreateRestorePlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'HBase', '2019-01-01', 'CreateRestorePlan','hbase')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_RestoreToDate(self):
		return self.get_query_params().get('RestoreToDate')

	def set_RestoreToDate(self,RestoreToDate):
		self.add_query_param('RestoreToDate',RestoreToDate)

	def get_Tables(self):
		return self.get_query_params().get('Tables')

	def set_Tables(self,Tables):
		self.add_query_param('Tables',Tables)

	def get_RestoreByCopy(self):
		return self.get_query_params().get('RestoreByCopy')

	def set_RestoreByCopy(self,RestoreByCopy):
		self.add_query_param('RestoreByCopy',RestoreByCopy)

	def get_RestoreAllTable(self):
		return self.get_query_params().get('RestoreAllTable')

	def set_RestoreAllTable(self,RestoreAllTable):
		self.add_query_param('RestoreAllTable',RestoreAllTable)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_TargetClusterId(self):
		return self.get_query_params().get('TargetClusterId')

	def set_TargetClusterId(self,TargetClusterId):
		self.add_query_param('TargetClusterId',TargetClusterId)