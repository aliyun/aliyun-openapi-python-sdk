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
from aliyunsdkbssopenapi.endpoint import endpoint_data

class DescribeSavingsPlansUsageTotalRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'DescribeSavingsPlansUsageTotal')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PeriodType(self):
		return self.get_query_params().get('PeriodType')

	def set_PeriodType(self,PeriodType):
		self.add_query_param('PeriodType',PeriodType)

	def get_BillOwnerId(self):
		return self.get_query_params().get('BillOwnerId')

	def set_BillOwnerId(self,BillOwnerId):
		self.add_query_param('BillOwnerId',BillOwnerId)

	def get_StartPeriod(self):
		return self.get_query_params().get('StartPeriod')

	def set_StartPeriod(self,StartPeriod):
		self.add_query_param('StartPeriod',StartPeriod)

	def get_EndPeriod(self):
		return self.get_query_params().get('EndPeriod')

	def set_EndPeriod(self,EndPeriod):
		self.add_query_param('EndPeriod',EndPeriod)