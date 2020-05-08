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
from aliyunsdksas.endpoint import endpoint_data

class DescribeCloudCenterInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeCloudCenterInstances','sas')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Criteria(self):
		return self.get_query_params().get('Criteria')

	def set_Criteria(self,Criteria):
		self.add_query_param('Criteria',Criteria)

	def get_NoPage(self):
		return self.get_query_params().get('NoPage')

	def set_NoPage(self,NoPage):
		self.add_query_param('NoPage',NoPage)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_LogicalExp(self):
		return self.get_query_params().get('LogicalExp')

	def set_LogicalExp(self,LogicalExp):
		self.add_query_param('LogicalExp',LogicalExp)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_MachineTypes(self):
		return self.get_query_params().get('MachineTypes')

	def set_MachineTypes(self,MachineTypes):
		self.add_query_param('MachineTypes',MachineTypes)