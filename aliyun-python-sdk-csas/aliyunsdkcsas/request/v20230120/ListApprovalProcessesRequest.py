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

class ListApprovalProcessesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'ListApprovalProcesses')
		self.set_method('GET')

	def get_ProcessIds(self): # Array
		return self.get_query_params().get('ProcessIds')

	def set_ProcessIds(self, ProcessIds):  # Array
		for index1, value1 in enumerate(ProcessIds):
			self.add_query_param('ProcessIds.' + str(index1 + 1), value1)
	def get_PolicyId(self): # String
		return self.get_query_params().get('PolicyId')

	def set_PolicyId(self, PolicyId):  # String
		self.add_query_param('PolicyId', PolicyId)
	def get_SaseUserId(self): # String
		return self.get_query_params().get('SaseUserId')

	def set_SaseUserId(self, SaseUserId):  # String
		self.add_query_param('SaseUserId', SaseUserId)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_PolicyType(self): # String
		return self.get_query_params().get('PolicyType')

	def set_PolicyType(self, PolicyType):  # String
		self.add_query_param('PolicyType', PolicyType)
	def get_ProcessName(self): # String
		return self.get_query_params().get('ProcessName')

	def set_ProcessName(self, ProcessName):  # String
		self.add_query_param('ProcessName', ProcessName)
	def get_CurrentPage(self): # Long
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Long
		self.add_query_param('CurrentPage', CurrentPage)
	def get_Username(self): # String
		return self.get_query_params().get('Username')

	def set_Username(self, Username):  # String
		self.add_query_param('Username', Username)
