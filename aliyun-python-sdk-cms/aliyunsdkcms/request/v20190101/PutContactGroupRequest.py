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
class PutContactGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutContactGroup','cms')

	def get_Describe(self):
		return self.get_query_params().get('Describe')

	def set_Describe(self,Describe):
		self.add_query_param('Describe',Describe)

	def get_ContactGroupName(self):
		return self.get_query_params().get('ContactGroupName')

	def set_ContactGroupName(self,ContactGroupName):
		self.add_query_param('ContactGroupName',ContactGroupName)

	def get_ContactNamess(self):
		return self.get_query_params().get('ContactNamess')

	def set_ContactNamess(self,ContactNamess):
		for i in range(len(ContactNamess)):	
			if ContactNamess[i] is not None:
				self.add_query_param('ContactNames.' + str(i + 1) , ContactNamess[i]);