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
from aliyunsdkretailcloud.endpoint import endpoint_data

class ListPodsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'ListPods','retailcloud')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StatusLists(self):
		return self.get_body_params().get('StatusLists')

	def set_StatusLists(self, StatusLists):
		for depth1 in range(len(StatusLists)):
			if StatusLists[depth1] is not None:
				self.add_body_params('StatusList.' + str(depth1 + 1) , StatusLists[depth1])

	def get_DeployOrderId(self):
		return self.get_query_params().get('DeployOrderId')

	def set_DeployOrderId(self,DeployOrderId):
		self.add_query_param('DeployOrderId',DeployOrderId)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_ResultLists(self):
		return self.get_body_params().get('ResultLists')

	def set_ResultLists(self, ResultLists):
		for depth1 in range(len(ResultLists)):
			if ResultLists[depth1] is not None:
				self.add_body_params('ResultList.' + str(depth1 + 1) , ResultLists[depth1])