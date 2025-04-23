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
from aliyunsdkeds_user.endpoint import endpoint_data

class UnlockUsersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eds-user', '2021-03-08', 'UnlockUsers','eds-user')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AutoLockTime(self): # String
		return self.get_query_params().get('AutoLockTime')

	def set_AutoLockTime(self, AutoLockTime):  # String
		self.add_query_param('AutoLockTime', AutoLockTime)
	def get_Userss(self): # RepeatList
		return self.get_body_params().get('Users')

	def set_Userss(self, Users):  # RepeatList
		for depth1 in range(len(Users)):
			self.add_body_params('Users.' + str(depth1 + 1), Users[depth1])
