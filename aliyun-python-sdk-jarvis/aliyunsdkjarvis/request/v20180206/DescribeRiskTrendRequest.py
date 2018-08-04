# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeRiskTrendRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'jarvis', '2018-02-06', 'DescribeRiskTrend')

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_QueryProduct(self):
		return self.get_query_params().get('QueryProduct')

	def set_QueryProduct(self,QueryProduct):
		self.add_query_param('QueryProduct',QueryProduct)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Peroid(self):
		return self.get_query_params().get('Peroid')

	def set_Peroid(self,Peroid):
		self.add_query_param('Peroid',Peroid)

	def get_SourceCode(self):
		return self.get_query_params().get('SourceCode')

	def set_SourceCode(self,SourceCode):
		self.add_query_param('SourceCode',SourceCode)

	def get_QueryRegionId(self):
		return self.get_query_params().get('QueryRegionId')

	def set_QueryRegionId(self,QueryRegionId):
		self.add_query_param('QueryRegionId',QueryRegionId)