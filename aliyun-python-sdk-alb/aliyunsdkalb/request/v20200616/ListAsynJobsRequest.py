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
from aliyunsdkalb.endpoint import endpoint_data

class ListAsynJobsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'ListAsynJobs','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_BeginTime(self): # Long
		return self.get_query_params().get('BeginTime')

	def set_BeginTime(self, BeginTime):  # Long
		self.add_query_param('BeginTime', BeginTime)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_ApiName(self): # String
		return self.get_query_params().get('ApiName')

	def set_ApiName(self, ApiName):  # String
		self.add_query_param('ApiName', ApiName)
	def get_JobIds(self): # Array
		return self.get_query_params().get('JobIds')

	def set_JobIds(self, JobIds):  # Array
		for index1, value1 in enumerate(JobIds):
			self.add_query_param('JobIds.' + str(index1 + 1), value1)
	def get_MaxResults(self): # Long
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_query_param('MaxResults', MaxResults)
	def get_ResourceIds(self): # Array
		return self.get_query_params().get('ResourceIds')

	def set_ResourceIds(self, ResourceIds):  # Array
		for index1, value1 in enumerate(ResourceIds):
			self.add_query_param('ResourceIds.' + str(index1 + 1), value1)
