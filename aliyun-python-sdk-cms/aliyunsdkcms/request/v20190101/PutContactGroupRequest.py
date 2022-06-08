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

class PutContactGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutContactGroup','cms')
		self.set_method('POST')

	def get_EnableSubscribed(self): # Boolean
		return self.get_query_params().get('EnableSubscribed')

	def set_EnableSubscribed(self, EnableSubscribed):  # Boolean
		self.add_query_param('EnableSubscribed', EnableSubscribed)
	def get_ContactGroupName(self): # String
		return self.get_query_params().get('ContactGroupName')

	def set_ContactGroupName(self, ContactGroupName):  # String
		self.add_query_param('ContactGroupName', ContactGroupName)
	def get_Describe(self): # String
		return self.get_query_params().get('Describe')

	def set_Describe(self, Describe):  # String
		self.add_query_param('Describe', Describe)
	def get_ContactNamess(self): # RepeatList
		return self.get_query_params().get('ContactNames')

	def set_ContactNamess(self, ContactNames):  # RepeatList
		for depth1 in range(len(ContactNames)):
			self.add_query_param('ContactNames.' + str(depth1 + 1), ContactNames[depth1])
