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
from aliyunsdkreid.endpoint import endpoint_data

class DescribeBaseStatisticsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'reid', '2019-09-28', 'DescribeBaseStatistics','1.1.7')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Date(self):
		return self.get_body_params().get('Date')

	def set_Date(self,Date):
		self.add_body_params('Date', Date)

	def get_ExtraStatisticTypes(self):
		return self.get_body_params().get('ExtraStatisticTypes')

	def set_ExtraStatisticTypes(self,ExtraStatisticTypes):
		self.add_body_params('ExtraStatisticTypes', ExtraStatisticTypes)

	def get_StoreId(self):
		return self.get_body_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_body_params('StoreId', StoreId)

	def get_SummaryType(self):
		return self.get_body_params().get('SummaryType')

	def set_SummaryType(self,SummaryType):
		self.add_body_params('SummaryType', SummaryType)

	def get_LocationId(self):
		return self.get_body_params().get('LocationId')

	def set_LocationId(self,LocationId):
		self.add_body_params('LocationId', LocationId)