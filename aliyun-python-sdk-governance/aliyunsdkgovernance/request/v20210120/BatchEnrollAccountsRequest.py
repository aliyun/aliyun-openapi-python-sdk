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
from aliyunsdkgovernance.endpoint import endpoint_data

class BatchEnrollAccountsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'governance', '2021-01-20', 'BatchEnrollAccounts','governance')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_BaselineId(self): # String
		return self.get_query_params().get('BaselineId')

	def set_BaselineId(self, BaselineId):  # String
		self.add_query_param('BaselineId', BaselineId)
	def get_BaselineItems(self): # Array
		return self.get_query_params().get('BaselineItems')

	def set_BaselineItems(self, BaselineItems):  # Array
		for index1, value1 in enumerate(BaselineItems):
			if value1.get('Name') is not None:
				self.add_query_param('BaselineItems.' + str(index1 + 1) + '.Name', value1.get('Name'))
			if value1.get('Skip') is not None:
				self.add_query_param('BaselineItems.' + str(index1 + 1) + '.Skip', value1.get('Skip'))
			if value1.get('Config') is not None:
				self.add_query_param('BaselineItems.' + str(index1 + 1) + '.Config', value1.get('Config'))
			if value1.get('Version') is not None:
				self.add_query_param('BaselineItems.' + str(index1 + 1) + '.Version', value1.get('Version'))
	def get_Accounts(self): # Array
		return self.get_query_params().get('Accounts')

	def set_Accounts(self, Accounts):  # Array
		for index1, value1 in enumerate(Accounts):
			if value1.get('AccountUid') is not None:
				self.add_query_param('Accounts.' + str(index1 + 1) + '.AccountUid', value1.get('AccountUid'))
