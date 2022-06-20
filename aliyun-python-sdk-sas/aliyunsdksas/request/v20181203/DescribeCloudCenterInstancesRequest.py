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
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeCloudCenterInstances')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Criteria(self): # String
		return self.get_query_params().get('Criteria')

	def set_Criteria(self, Criteria):  # String
		self.add_query_param('Criteria', Criteria)
	def get_Importance(self): # Integer
		return self.get_query_params().get('Importance')

	def set_Importance(self, Importance):  # Integer
		self.add_query_param('Importance', Importance)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_LogicalExp(self): # String
		return self.get_query_params().get('LogicalExp')

	def set_LogicalExp(self, LogicalExp):  # String
		self.add_query_param('LogicalExp', LogicalExp)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_MachineTypes(self): # String
		return self.get_query_params().get('MachineTypes')

	def set_MachineTypes(self, MachineTypes):  # String
		self.add_query_param('MachineTypes', MachineTypes)
	def get_NoGroupTrace(self): # Boolean
		return self.get_query_params().get('NoGroupTrace')

	def set_NoGroupTrace(self, NoGroupTrace):  # Boolean
		self.add_query_param('NoGroupTrace', NoGroupTrace)
