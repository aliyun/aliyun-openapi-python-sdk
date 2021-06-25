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
from aliyunsdkoutboundbot.endpoint import endpoint_data

class QueryJobsWithResultRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'QueryJobsWithResult','outboundbot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_HasReachedEndOfFlowFilter(self):
		return self.get_query_params().get('HasReachedEndOfFlowFilter')

	def set_HasReachedEndOfFlowFilter(self,HasReachedEndOfFlowFilter):
		self.add_query_param('HasReachedEndOfFlowFilter',HasReachedEndOfFlowFilter)

	def get_HasAnsweredFilter(self):
		return self.get_query_params().get('HasAnsweredFilter')

	def set_HasAnsweredFilter(self,HasAnsweredFilter):
		self.add_query_param('HasAnsweredFilter',HasAnsweredFilter)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_QueryText(self):
		return self.get_query_params().get('QueryText')

	def set_QueryText(self,QueryText):
		self.add_query_param('QueryText',QueryText)

	def get_HasHangUpByRejectionFilter(self):
		return self.get_query_params().get('HasHangUpByRejectionFilter')

	def set_HasHangUpByRejectionFilter(self,HasHangUpByRejectionFilter):
		self.add_query_param('HasHangUpByRejectionFilter',HasHangUpByRejectionFilter)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_JobStatusFilter(self):
		return self.get_query_params().get('JobStatusFilter')

	def set_JobStatusFilter(self,JobStatusFilter):
		self.add_query_param('JobStatusFilter',JobStatusFilter)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_JobGroupId(self):
		return self.get_query_params().get('JobGroupId')

	def set_JobGroupId(self,JobGroupId):
		self.add_query_param('JobGroupId',JobGroupId)