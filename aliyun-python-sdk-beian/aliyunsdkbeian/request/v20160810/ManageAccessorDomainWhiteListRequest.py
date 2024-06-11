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

class ManageAccessorDomainWhiteListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Beian', '2016-08-10', 'ManageAccessorDomainWhiteList')
		self.set_method('POST')

	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_Domainss(self): # RepeatList
		return self.get_query_params().get('Domains')

	def set_Domainss(self, Domains):  # RepeatList
		for depth1 in range(len(Domains)):
			self.add_query_param('Domains.' + str(depth1 + 1), Domains[depth1])
	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_Caller(self): # String
		return self.get_query_params().get('Caller')

	def set_Caller(self, Caller):  # String
		self.add_query_param('Caller', Caller)
	def get_Operation(self): # String
		return self.get_query_params().get('Operation')

	def set_Operation(self, Operation):  # String
		self.add_query_param('Operation', Operation)
