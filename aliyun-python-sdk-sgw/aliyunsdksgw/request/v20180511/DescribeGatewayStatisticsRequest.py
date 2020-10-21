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

class DescribeGatewayStatisticsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sgw', '2018-05-11', 'DescribeGatewayStatistics','hcs_sgw')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_GatewayCategory(self):
		return self.get_query_params().get('GatewayCategory')

	def set_GatewayCategory(self,GatewayCategory):
		self.add_query_param('GatewayCategory',GatewayCategory)

	def get_GatewayLocation(self):
		return self.get_query_params().get('GatewayLocation')

	def set_GatewayLocation(self,GatewayLocation):
		self.add_query_param('GatewayLocation',GatewayLocation)

	def get_StartTimestamp(self):
		return self.get_query_params().get('StartTimestamp')

	def set_StartTimestamp(self,StartTimestamp):
		self.add_query_param('StartTimestamp',StartTimestamp)

	def get_EndTimestamp(self):
		return self.get_query_params().get('EndTimestamp')

	def set_EndTimestamp(self,EndTimestamp):
		self.add_query_param('EndTimestamp',EndTimestamp)

	def get_TargetAccountId(self):
		return self.get_query_params().get('TargetAccountId')

	def set_TargetAccountId(self,TargetAccountId):
		self.add_query_param('TargetAccountId',TargetAccountId)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)