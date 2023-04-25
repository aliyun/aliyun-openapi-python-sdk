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
from aliyunsdkccc.endpoint import endpoint_data

class ListCampaignsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2020-07-01', 'ListCampaigns','CCC')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ActualStartTimeTo(self): # String
		return self.get_query_params().get('ActualStartTimeTo')

	def set_ActualStartTimeTo(self, ActualStartTimeTo):  # String
		self.add_query_param('ActualStartTimeTo', ActualStartTimeTo)
	def get_QueueId(self): # String
		return self.get_query_params().get('QueueId')

	def set_QueueId(self, QueueId):  # String
		self.add_query_param('QueueId', QueueId)
	def get_ActualStartTimeFrom(self): # String
		return self.get_query_params().get('ActualStartTimeFrom')

	def set_ActualStartTimeFrom(self, ActualStartTimeFrom):  # String
		self.add_query_param('ActualStartTimeFrom', ActualStartTimeFrom)
	def get_PageNumber(self): # Long
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Long
		self.add_query_param('PageNumber', PageNumber)
	def get_PlanedStartTimeFrom(self): # String
		return self.get_query_params().get('PlanedStartTimeFrom')

	def set_PlanedStartTimeFrom(self, PlanedStartTimeFrom):  # String
		self.add_query_param('PlanedStartTimeFrom', PlanedStartTimeFrom)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_PlanedStartTimeTo(self): # String
		return self.get_query_params().get('PlanedStartTimeTo')

	def set_PlanedStartTimeTo(self, PlanedStartTimeTo):  # String
		self.add_query_param('PlanedStartTimeTo', PlanedStartTimeTo)
	def get_State(self): # String
		return self.get_query_params().get('State')

	def set_State(self, State):  # String
		self.add_query_param('State', State)
