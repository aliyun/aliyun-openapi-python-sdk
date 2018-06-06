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
class DescribeRiskListDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'jarvis', '2018-02-06', 'DescribeRiskListDetail')

	def get_riskType(self):
		return self.get_query_params().get('riskType')

	def set_riskType(self,riskType):
		self.add_query_param('riskType',riskType)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_pageSize(self):
		return self.get_query_params().get('pageSize')

	def set_pageSize(self,pageSize):
		self.add_query_param('pageSize',pageSize)

	def get_queryProduct(self):
		return self.get_query_params().get('queryProduct')

	def set_queryProduct(self,queryProduct):
		self.add_query_param('queryProduct',queryProduct)

	def get_currentPage(self):
		return self.get_query_params().get('currentPage')

	def set_currentPage(self,currentPage):
		self.add_query_param('currentPage',currentPage)

	def get_riskDescribe(self):
		return self.get_query_params().get('riskDescribe')

	def set_riskDescribe(self,riskDescribe):
		self.add_query_param('riskDescribe',riskDescribe)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_srcUid(self):
		return self.get_query_params().get('srcUid')

	def set_srcUid(self,srcUid):
		self.add_query_param('srcUid',srcUid)

	def get_sourceCode(self):
		return self.get_query_params().get('sourceCode')

	def set_sourceCode(self,sourceCode):
		self.add_query_param('sourceCode',sourceCode)

	def get_queryRegionId(self):
		return self.get_query_params().get('queryRegionId')

	def set_queryRegionId(self,queryRegionId):
		self.add_query_param('queryRegionId',queryRegionId)

	def get_status(self):
		return self.get_query_params().get('status')

	def set_status(self,status):
		self.add_query_param('status',status)