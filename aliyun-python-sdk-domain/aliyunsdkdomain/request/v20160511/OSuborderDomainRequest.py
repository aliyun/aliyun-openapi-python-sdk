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
class OSuborderDomainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2016-05-11', 'OSuborderDomain')

	def get_endDate(self):
		return self.get_query_params().get('endDate')

	def set_endDate(self,endDate):
		self.add_query_param('endDate',endDate)

	def get_pageSize(self):
		return self.get_query_params().get('pageSize')

	def set_pageSize(self,pageSize):
		self.add_query_param('pageSize',pageSize)

	def get_type(self):
		return self.get_query_params().get('type')

	def set_type(self,type):
		self.add_query_param('type',type)

	def get_startDate(self):
		return self.get_query_params().get('startDate')

	def set_startDate(self,startDate):
		self.add_query_param('startDate',startDate)

	def get_pageNum(self):
		return self.get_query_params().get('pageNum')

	def set_pageNum(self,pageNum):
		self.add_query_param('pageNum',pageNum)