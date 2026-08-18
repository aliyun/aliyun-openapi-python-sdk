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
from aliyunsdkrds.endpoint import endpoint_data

class DescribeRCInstanceTypesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'DescribeRCInstanceTypes','rds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_InstanceTypeFamily(self): # String
		return self.get_query_params().get('InstanceTypeFamily')

	def set_InstanceTypeFamily(self, InstanceTypeFamily):  # String
		self.add_query_param('InstanceTypeFamily', InstanceTypeFamily)
	def get_CommodityCode(self): # String
		return self.get_query_params().get('CommodityCode')

	def set_CommodityCode(self, CommodityCode):  # String
		self.add_query_param('CommodityCode', CommodityCode)
	def get_Engine(self): # String
		return self.get_query_params().get('Engine')

	def set_Engine(self, Engine):  # String
		self.add_query_param('Engine', Engine)
	def get_InstanceType(self): # Array
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # Array
		for index1, value1 in enumerate(InstanceType):
			self.add_query_param('InstanceType.' + str(index1 + 1), value1)
