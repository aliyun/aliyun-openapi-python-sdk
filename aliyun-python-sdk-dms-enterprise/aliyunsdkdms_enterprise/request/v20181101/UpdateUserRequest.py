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
from aliyunsdkdms_enterprise.endpoint import endpoint_data

class UpdateUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'UpdateUser','dms-enterprise')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RoleNames(self): # String
		return self.get_query_params().get('RoleNames')

	def set_RoleNames(self, RoleNames):  # String
		self.add_query_param('RoleNames', RoleNames)
	def get_MaxResultCount(self): # Long
		return self.get_query_params().get('MaxResultCount')

	def set_MaxResultCount(self, MaxResultCount):  # Long
		self.add_query_param('MaxResultCount', MaxResultCount)
	def get_MaxExecuteCount(self): # Long
		return self.get_query_params().get('MaxExecuteCount')

	def set_MaxExecuteCount(self, MaxExecuteCount):  # Long
		self.add_query_param('MaxExecuteCount', MaxExecuteCount)
	def get_UserNick(self): # String
		return self.get_query_params().get('UserNick')

	def set_UserNick(self, UserNick):  # String
		self.add_query_param('UserNick', UserNick)
	def get_Mobile(self): # String
		return self.get_query_params().get('Mobile')

	def set_Mobile(self, Mobile):  # String
		self.add_query_param('Mobile', Mobile)
	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
	def get_Uid(self): # Long
		return self.get_query_params().get('Uid')

	def set_Uid(self, Uid):  # Long
		self.add_query_param('Uid', Uid)
