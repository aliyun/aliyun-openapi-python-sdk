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

class ListServerlessJobsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'ListServerlessJobs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SubmitTimeStart(self): # String
		return self.get_query_params().get('SubmitTimeStart')

	def set_SubmitTimeStart(self, SubmitTimeStart):  # String
		self.add_query_param('SubmitTimeStart', SubmitTimeStart)
	def get_PageNumber(self): # Long
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Long
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_State(self): # String
		return self.get_query_params().get('State')

	def set_State(self, State):  # String
		self.add_query_param('State', State)
	def get_SubmitOrder(self): # String
		return self.get_query_params().get('SubmitOrder')

	def set_SubmitOrder(self, SubmitOrder):  # String
		self.add_query_param('SubmitOrder', SubmitOrder)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_JobNames(self): # Array
		return self.get_query_params().get('JobNames')

	def set_JobNames(self, JobNames):  # Array
		for index1, value1 in enumerate(JobNames):
			self.add_query_param('JobNames.' + str(index1 + 1), value1)
	def get_Users(self): # Array
		return self.get_query_params().get('Users')

	def set_Users(self, Users):  # Array
		for index1, value1 in enumerate(Users):
			self.add_query_param('Users.' + str(index1 + 1), value1)
	def get_StartOrder(self): # String
		return self.get_query_params().get('StartOrder')

	def set_StartOrder(self, StartOrder):  # String
		self.add_query_param('StartOrder', StartOrder)
	def get_SubmitTimeEnd(self): # String
		return self.get_query_params().get('SubmitTimeEnd')

	def set_SubmitTimeEnd(self, SubmitTimeEnd):  # String
		self.add_query_param('SubmitTimeEnd', SubmitTimeEnd)
	def get_Queues(self): # Array
		return self.get_query_params().get('Queues')

	def set_Queues(self, Queues):  # Array
		for index1, value1 in enumerate(Queues):
			self.add_query_param('Queues.' + str(index1 + 1), value1)
	def get_JobIds(self): # Array
		return self.get_query_params().get('JobIds')

	def set_JobIds(self, JobIds):  # Array
		for index1, value1 in enumerate(JobIds):
			self.add_query_param('JobIds.' + str(index1 + 1), value1)
