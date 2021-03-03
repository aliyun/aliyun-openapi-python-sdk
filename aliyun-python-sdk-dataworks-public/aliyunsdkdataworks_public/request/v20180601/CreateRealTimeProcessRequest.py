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

class CreateRealTimeProcessRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2018-06-01', 'CreateRealTimeProcess')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_JobConfig(self):
		return self.get_query_params().get('JobConfig')

	def set_JobConfig(self,JobConfig):
		self.add_query_param('JobConfig',JobConfig)

	def get_CreateResGroup(self):
		return self.get_query_params().get('CreateResGroup')

	def set_CreateResGroup(self,CreateResGroup):
		self.add_query_param('CreateResGroup',CreateResGroup)

	def get_DataworksVersion(self):
		return self.get_query_params().get('DataworksVersion')

	def set_DataworksVersion(self,DataworksVersion):
		self.add_query_param('DataworksVersion',DataworksVersion)

	def get_ResourceSpec(self):
		return self.get_query_params().get('ResourceSpec')

	def set_ResourceSpec(self,ResourceSpec):
		self.add_query_param('ResourceSpec',ResourceSpec)

	def get_TableRule(self):
		return self.get_query_params().get('TableRule')

	def set_TableRule(self,TableRule):
		self.add_query_param('TableRule',TableRule)

	def get_Tables(self):
		return self.get_query_params().get('Tables')

	def set_Tables(self,Tables):
		self.add_query_param('Tables',Tables)

	def get_DataSource(self):
		return self.get_query_params().get('DataSource')

	def set_DataSource(self,DataSource):
		self.add_query_param('DataSource',DataSource)