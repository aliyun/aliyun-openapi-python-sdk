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
from aliyunsdklive.endpoint import endpoint_data

class AddCasterEpisodeGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'AddCasterEpisodeGroup','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_SideOutputUrl(self): # String
		return self.get_query_params().get('SideOutputUrl')

	def set_SideOutputUrl(self, SideOutputUrl):  # String
		self.add_query_param('SideOutputUrl', SideOutputUrl)
	def get_Items(self): # RepeatList
		return self.get_query_params().get('Item')

	def set_Items(self, Item):  # RepeatList
		for depth1 in range(len(Item)):
			if Item[depth1].get('ItemName') is not None:
				self.add_query_param('Item.' + str(depth1 + 1) + '.ItemName', Item[depth1].get('ItemName'))
			if Item[depth1].get('VodUrl') is not None:
				self.add_query_param('Item.' + str(depth1 + 1) + '.VodUrl', Item[depth1].get('VodUrl'))
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_RepeatNum(self): # Integer
		return self.get_query_params().get('RepeatNum')

	def set_RepeatNum(self, RepeatNum):  # Integer
		self.add_query_param('RepeatNum', RepeatNum)
	def get_CallbackUrl(self): # String
		return self.get_query_params().get('CallbackUrl')

	def set_CallbackUrl(self, CallbackUrl):  # String
		self.add_query_param('CallbackUrl', CallbackUrl)
