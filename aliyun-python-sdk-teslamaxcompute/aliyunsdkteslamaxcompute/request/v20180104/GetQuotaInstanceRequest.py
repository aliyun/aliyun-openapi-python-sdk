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
class GetQuotaInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'TeslaMaxCompute', '2018-01-04', 'GetQuotaInstance')

	def get_Cluster(self):
		return self.get_query_params().get('Cluster')

	def set_Cluster(self,Cluster):
		self.add_query_param('Cluster',Cluster)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_QuotaId(self):
		return self.get_query_params().get('QuotaId')

	def set_QuotaId(self,QuotaId):
		self.add_query_param('QuotaId',QuotaId)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)

	def get_QuotaName(self):
		return self.get_query_params().get('QuotaName')

	def set_QuotaName(self,QuotaName):
		self.add_query_param('QuotaName',QuotaName)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)