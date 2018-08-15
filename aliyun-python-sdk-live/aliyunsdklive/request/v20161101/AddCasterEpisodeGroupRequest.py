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
class AddCasterEpisodeGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'AddCasterEpisodeGroup','live')

	def get_SideOutputUrl(self):
		return self.get_query_params().get('SideOutputUrl')

	def set_SideOutputUrl(self,SideOutputUrl):
		self.add_query_param('SideOutputUrl',SideOutputUrl)

	def get_Items(self):
		return self.get_query_params().get('Items')

	def set_Items(self,Items):
		for i in range(len(Items)):	
			if Items[i].get('VodUrl') is not None:
				self.add_query_param('Item.' + str(i + 1) + '.VodUrl' , Items[i].get('VodUrl'))
			if Items[i].get('ItemName') is not None:
				self.add_query_param('Item.' + str(i + 1) + '.ItemName' , Items[i].get('ItemName'))


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_RepeatNum(self):
		return self.get_query_params().get('RepeatNum')

	def set_RepeatNum(self,RepeatNum):
		self.add_query_param('RepeatNum',RepeatNum)

	def get_CallbackUrl(self):
		return self.get_query_params().get('CallbackUrl')

	def set_CallbackUrl(self,CallbackUrl):
		self.add_query_param('CallbackUrl',CallbackUrl)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)