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

class CreateMonitorGroupByResourceGroupIdRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'CreateMonitorGroupByResourceGroupId','cms')
		self.set_method('POST')

	def get_ResourceGroupName(self):
		return self.get_query_params().get('ResourceGroupName')

	def set_ResourceGroupName(self,ResourceGroupName):
		self.add_query_param('ResourceGroupName',ResourceGroupName)

	def get_EnableSubscribeEvent(self):
		return self.get_query_params().get('EnableSubscribeEvent')

	def set_EnableSubscribeEvent(self,EnableSubscribeEvent):
		self.add_query_param('EnableSubscribeEvent',EnableSubscribeEvent)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_EnableInstallAgent(self):
		return self.get_query_params().get('EnableInstallAgent')

	def set_EnableInstallAgent(self,EnableInstallAgent):
		self.add_query_param('EnableInstallAgent',EnableInstallAgent)

	def get_ContactGroupLists(self):
		return self.get_query_params().get('ContactGroupList')

	def set_ContactGroupLists(self, ContactGroupLists):
		for depth1 in range(len(ContactGroupLists)):
			if ContactGroupLists[depth1] is not None:
				self.add_query_param('ContactGroupList.' + str(depth1 + 1) , ContactGroupLists[depth1])