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
class ResetUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'ResetUser')

	def get_Bizid(self):
		return self.get_body_params().get('Bizid')

	def set_Bizid(self,Bizid):
		self.add_body_params('Bizid', Bizid)

	def get_Bid(self):
		return self.get_body_params().get('Bid')

	def set_Bid(self,Bid):
		self.add_body_params('Bid', Bid)

	def get_Operation(self):
		return self.get_body_params().get('Operation')

	def set_Operation(self,Operation):
		self.add_body_params('Operation', Operation)

	def get_UserName(self):
		return self.get_body_params().get('UserName')

	def set_UserName(self,UserName):
		self.add_body_params('UserName', UserName)