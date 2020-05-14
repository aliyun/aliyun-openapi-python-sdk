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
from aliyunsdkschedulerx2.endpoint import endpoint_data

class CreateAppGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'schedulerx2', '2019-04-30', 'CreateAppGroup')
		self.set_protocol_type('https')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MaxJobs(self):
		return self.get_query_params().get('MaxJobs')

	def set_MaxJobs(self,MaxJobs):
		self.add_query_param('MaxJobs',MaxJobs)

	def get_NamespaceName(self):
		return self.get_query_params().get('NamespaceName')

	def set_NamespaceName(self,NamespaceName):
		self.add_query_param('NamespaceName',NamespaceName)

	def get_NamespaceSource(self):
		return self.get_query_params().get('NamespaceSource')

	def set_NamespaceSource(self,NamespaceSource):
		self.add_query_param('NamespaceSource',NamespaceSource)

	def get_MetricsThresholdJson(self):
		return self.get_query_params().get('MetricsThresholdJson')

	def set_MetricsThresholdJson(self,MetricsThresholdJson):
		self.add_query_param('MetricsThresholdJson',MetricsThresholdJson)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_AppName(self):
		return self.get_query_params().get('AppName')

	def set_AppName(self,AppName):
		self.add_query_param('AppName',AppName)

	def get_Namespace(self):
		return self.get_query_params().get('Namespace')

	def set_Namespace(self,Namespace):
		self.add_query_param('Namespace',Namespace)

	def get_AlarmJson(self):
		return self.get_query_params().get('AlarmJson')

	def set_AlarmJson(self,AlarmJson):
		self.add_query_param('AlarmJson',AlarmJson)