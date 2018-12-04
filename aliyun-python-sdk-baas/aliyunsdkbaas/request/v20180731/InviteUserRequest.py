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
class InviteUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'InviteUser')

	def get_Bizid(self):
		return self.get_body_params().get('Bizid')

	def set_Bizid(self,Bizid):
		self.add_body_params('Bizid', Bizid)

	def get_Bid(self):
		return self.get_body_params().get('Bid')

	def set_Bid(self,Bid):
		self.add_body_params('Bid', Bid)

	def get_UserId(self):
		return self.get_body_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_body_params('UserId', UserId)

	def get_UserEmail(self):
		return self.get_body_params().get('UserEmail')

	def set_UserEmail(self,UserEmail):
		self.add_body_params('UserEmail', UserEmail)