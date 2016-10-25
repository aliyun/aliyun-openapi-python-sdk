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
class PushByteMessageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Push', '2015-08-27', 'PushByteMessage')

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_SendType(self):
		return self.get_query_params().get('SendType')

	def set_SendType(self,SendType):
		self.add_query_param('SendType',SendType)

	def get_Accounts(self):
		return self.get_query_params().get('Accounts')

	def set_Accounts(self,Accounts):
		self.add_query_param('Accounts',Accounts)

	def get_DeviceIds(self):
		return self.get_query_params().get('DeviceIds')

	def set_DeviceIds(self,DeviceIds):
		self.add_query_param('DeviceIds',DeviceIds)

	def get_PushContent(self):
		return self.get_query_params().get('PushContent')

	def set_PushContent(self,PushContent):
		self.add_query_param('PushContent',PushContent)