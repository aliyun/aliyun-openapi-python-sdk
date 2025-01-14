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
import json

class UpdateBootAndAntiUninstallPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'UpdateBootAndAntiUninstallPolicy')
		self.set_method('POST')

	def get_IsAntiUninstall(self): # Boolean
		return self.get_body_params().get('IsAntiUninstall')

	def set_IsAntiUninstall(self, IsAntiUninstall):  # Boolean
		self.add_body_params('IsAntiUninstall', IsAntiUninstall)
	def get_AllowReport(self): # Boolean
		return self.get_body_params().get('AllowReport')

	def set_AllowReport(self, AllowReport):  # Boolean
		self.add_body_params('AllowReport', AllowReport)
	def get_UserGroupIds(self): # Array
		return self.get_body_params().get('UserGroupIds')

	def set_UserGroupIds(self, UserGroupIds):  # Array
		for index1, value1 in enumerate(UserGroupIds):
			self.add_body_params('UserGroupIds.' + str(index1 + 1), value1)
	def get_WhitelistUsers(self): # Array
		return self.get_body_params().get('WhitelistUsers')

	def set_WhitelistUsers(self, WhitelistUsers):  # Array
		for index1, value1 in enumerate(WhitelistUsers):
			self.add_body_params('WhitelistUsers.' + str(index1 + 1), value1)
	def get_BlockContent(self): # Struct
		return self.get_body_params().get('BlockContent')

	def set_BlockContent(self, BlockContent):  # Struct
		self.add_body_params("BlockContent", json.dumps(BlockContent))
	def get_IsBoot(self): # Boolean
		return self.get_body_params().get('IsBoot')

	def set_IsBoot(self, IsBoot):  # Boolean
		self.add_body_params('IsBoot', IsBoot)
