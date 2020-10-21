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
from aliyunsdksgw.endpoint import endpoint_data

class DescribeSubscriptionPriceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sgw', '2018-05-11', 'DescribeSubscriptionPrice','hcs_sgw')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_GatewayClass(self):
		return self.get_query_params().get('GatewayClass')

	def set_GatewayClass(self,GatewayClass):
		self.add_query_param('GatewayClass',GatewayClass)

	def get_CacheSSDSize(self):
		return self.get_query_params().get('CacheSSDSize')

	def set_CacheSSDSize(self,CacheSSDSize):
		self.add_query_param('CacheSSDSize',CacheSSDSize)

	def get_PeriodUnit(self):
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self,PeriodUnit):
		self.add_query_param('PeriodUnit',PeriodUnit)

	def get_PeriodQuantity(self):
		return self.get_query_params().get('PeriodQuantity')

	def set_PeriodQuantity(self,PeriodQuantity):
		self.add_query_param('PeriodQuantity',PeriodQuantity)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_CacheCloudEfficiencySize(self):
		return self.get_query_params().get('CacheCloudEfficiencySize')

	def set_CacheCloudEfficiencySize(self,CacheCloudEfficiencySize):
		self.add_query_param('CacheCloudEfficiencySize',CacheCloudEfficiencySize)