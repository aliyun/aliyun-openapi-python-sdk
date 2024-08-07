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

class AddCustomImageShareAccountRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SWAS-OPEN', '2020-06-01', 'AddCustomImageShareAccount','SWAS-OPEN')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Accounts(self): # RepeatList
		return self.get_query_params().get('Account')

	def set_Accounts(self, Account):  # RepeatList
		for depth1 in range(len(Account)):
			self.add_query_param('Account.' + str(depth1 + 1), Account[depth1])
