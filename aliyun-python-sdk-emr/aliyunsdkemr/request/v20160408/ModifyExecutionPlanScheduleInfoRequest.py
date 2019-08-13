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
from aliyunsdkemr.endpoint import endpoint_data

class ModifyExecutionPlanScheduleInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ModifyExecutionPlanScheduleInfo','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_TimeInterval(self):
		return self.get_query_params().get('TimeInterval')

	def set_TimeInterval(self,TimeInterval):
		self.add_query_param('TimeInterval',TimeInterval)

	def get_DayOfWeek(self):
		return self.get_query_params().get('DayOfWeek')

	def set_DayOfWeek(self,DayOfWeek):
		self.add_query_param('DayOfWeek',DayOfWeek)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_Strategy(self):
		return self.get_query_params().get('Strategy')

	def set_Strategy(self,Strategy):
		self.add_query_param('Strategy',Strategy)

	def get_TimeUnit(self):
		return self.get_query_params().get('TimeUnit')

	def set_TimeUnit(self,TimeUnit):
		self.add_query_param('TimeUnit',TimeUnit)

	def get_DayOfMonth(self):
		return self.get_query_params().get('DayOfMonth')

	def set_DayOfMonth(self,DayOfMonth):
		self.add_query_param('DayOfMonth',DayOfMonth)