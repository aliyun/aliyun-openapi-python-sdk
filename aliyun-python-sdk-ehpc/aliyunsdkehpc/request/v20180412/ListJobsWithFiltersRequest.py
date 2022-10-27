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
from aliyunsdkehpc.endpoint import endpoint_data

class ListJobsWithFiltersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'ListJobsWithFilters')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_JobStatus(self): # String
		return self.get_query_params().get('JobStatus')

	def set_JobStatus(self, JobStatus):  # String
		self.add_query_param('JobStatus', JobStatus)
	def get_PageNumber(self): # Long
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Long
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_ExecuteOrder(self): # String
		return self.get_query_params().get('ExecuteOrder')

	def set_ExecuteOrder(self, ExecuteOrder):  # String
		self.add_query_param('ExecuteOrder', ExecuteOrder)
	def get_JobName(self): # String
		return self.get_query_params().get('JobName')

	def set_JobName(self, JobName):  # String
		self.add_query_param('JobName', JobName)
	def get_SubmitOrder(self): # String
		return self.get_query_params().get('SubmitOrder')

	def set_SubmitOrder(self, SubmitOrder):  # String
		self.add_query_param('SubmitOrder', SubmitOrder)
	def get_PendOrder(self): # String
		return self.get_query_params().get('PendOrder')

	def set_PendOrder(self, PendOrder):  # String
		self.add_query_param('PendOrder', PendOrder)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_Users(self): # Array
		return self.get_query_params().get('Users')

	def set_Users(self, Users):  # Array
		for index1, value1 in enumerate(Users):
			self.add_query_param('Users.' + str(index1 + 1), value1)
	def get_CreateTimeEnd(self): # String
		return self.get_query_params().get('CreateTimeEnd')

	def set_CreateTimeEnd(self, CreateTimeEnd):  # String
		self.add_query_param('CreateTimeEnd', CreateTimeEnd)
	def get_Async(self): # Boolean
		return self.get_query_params().get('Async')

	def set_Async(self, _Async):  # Boolean
		self.add_query_param('Async', _Async)
	def get_Nodes(self): # Array
		return self.get_query_params().get('Nodes')

	def set_Nodes(self, Nodes):  # Array
		for index1, value1 in enumerate(Nodes):
			self.add_query_param('Nodes.' + str(index1 + 1), value1)
	def get_Queues(self): # Array
		return self.get_query_params().get('Queues')

	def set_Queues(self, Queues):  # Array
		for index1, value1 in enumerate(Queues):
			self.add_query_param('Queues.' + str(index1 + 1), value1)
	def get_CreateTimeStart(self): # String
		return self.get_query_params().get('CreateTimeStart')

	def set_CreateTimeStart(self, CreateTimeStart):  # String
		self.add_query_param('CreateTimeStart', CreateTimeStart)
