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

class ListDeployOrdersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'ListDeployOrders','retailcloud')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StartTimeGreaterThanOrEqualTo(self):
		return self.get_query_params().get('StartTimeGreaterThanOrEqualTo')

	def set_StartTimeGreaterThanOrEqualTo(self,StartTimeGreaterThanOrEqualTo):
		self.add_query_param('StartTimeGreaterThanOrEqualTo',StartTimeGreaterThanOrEqualTo)

	def get_StatusLists(self):
		return self.get_body_params().get('StatusLists')

	def set_StatusLists(self, StatusLists):
		for depth1 in range(len(StatusLists)):
			if StatusLists[depth1] is not None:
				self.add_body_params('StatusList.' + str(depth1 + 1) , StatusLists[depth1])

	def get_EnvId(self):
		return self.get_query_params().get('EnvId')

	def set_EnvId(self,EnvId):
		self.add_query_param('EnvId',EnvId)

	def get_EndTimeGreaterThan(self):
		return self.get_query_params().get('EndTimeGreaterThan')

	def set_EndTimeGreaterThan(self,EndTimeGreaterThan):
		self.add_query_param('EndTimeGreaterThan',EndTimeGreaterThan)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PauseType(self):
		return self.get_query_params().get('PauseType')

	def set_PauseType(self,PauseType):
		self.add_query_param('PauseType',PauseType)

	def get_ResultLists(self):
		return self.get_body_params().get('ResultLists')

	def set_ResultLists(self, ResultLists):
		for depth1 in range(len(ResultLists)):
			if ResultLists[depth1] is not None:
				self.add_body_params('ResultList.' + str(depth1 + 1) , ResultLists[depth1])

	def get_StartTimeGreaterThan(self):
		return self.get_query_params().get('StartTimeGreaterThan')

	def set_StartTimeGreaterThan(self,StartTimeGreaterThan):
		self.add_query_param('StartTimeGreaterThan',StartTimeGreaterThan)

	def get_StartTimeLessThan(self):
		return self.get_query_params().get('StartTimeLessThan')

	def set_StartTimeLessThan(self,StartTimeLessThan):
		self.add_query_param('StartTimeLessThan',StartTimeLessThan)

	def get_StartTimeLessThanOrEqualTo(self):
		return self.get_query_params().get('StartTimeLessThanOrEqualTo')

	def set_StartTimeLessThanOrEqualTo(self,StartTimeLessThanOrEqualTo):
		self.add_query_param('StartTimeLessThanOrEqualTo',StartTimeLessThanOrEqualTo)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_EnvType(self):
		return self.get_query_params().get('EnvType')

	def set_EnvType(self,EnvType):
		self.add_query_param('EnvType',EnvType)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_EndTimeGreaterThanOrEqualTo(self):
		return self.get_query_params().get('EndTimeGreaterThanOrEqualTo')

	def set_EndTimeGreaterThanOrEqualTo(self,EndTimeGreaterThanOrEqualTo):
		self.add_query_param('EndTimeGreaterThanOrEqualTo',EndTimeGreaterThanOrEqualTo)

	def get_EndTimeLessThan(self):
		return self.get_query_params().get('EndTimeLessThan')

	def set_EndTimeLessThan(self,EndTimeLessThan):
		self.add_query_param('EndTimeLessThan',EndTimeLessThan)

	def get_EndTimeLessThanOrEqualTo(self):
		return self.get_query_params().get('EndTimeLessThanOrEqualTo')

	def set_EndTimeLessThanOrEqualTo(self,EndTimeLessThanOrEqualTo):
		self.add_query_param('EndTimeLessThanOrEqualTo',EndTimeLessThanOrEqualTo)

	def get_PartitionType(self):
		return self.get_query_params().get('PartitionType')

	def set_PartitionType(self,PartitionType):
		self.add_query_param('PartitionType',PartitionType)

	def get_DeployCategory(self):
		return self.get_query_params().get('DeployCategory')

	def set_DeployCategory(self,DeployCategory):
		self.add_query_param('DeployCategory',DeployCategory)

	def get_DeployType(self):
		return self.get_query_params().get('DeployType')

	def set_DeployType(self,DeployType):
		self.add_query_param('DeployType',DeployType)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)