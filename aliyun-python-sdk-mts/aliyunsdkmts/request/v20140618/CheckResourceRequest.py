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
from aliyunsdkmts.endpoint import endpoint_data

class CheckResourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'CheckResource')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Country(self):
		return self.get_query_params().get('Country')

	def set_Country(self,Country):
		self.add_query_param('Country',Country)

	def get_Hid(self):
		return self.get_query_params().get('Hid')

	def set_Hid(self,Hid):
		self.add_query_param('Hid',Hid)

	def get_Level(self):
		return self.get_query_params().get('Level')

	def set_Level(self,Level):
		self.add_query_param('Level',Level)

	def get_Invoker(self):
		return self.get_query_params().get('Invoker')

	def set_Invoker(self,Invoker):
		self.add_query_param('Invoker',Invoker)

	def get_Message(self):
		return self.get_query_params().get('Message')

	def set_Message(self,Message):
		self.add_query_param('Message',Message)

	def get_Url(self):
		return self.get_query_params().get('Url')

	def set_Url(self,Url):
		self.add_query_param('Url',Url)

	def get_Success(self):
		return self.get_query_params().get('Success')

	def set_Success(self,Success):
		self.add_query_param('Success',Success)

	def get_Interrupt(self):
		return self.get_query_params().get('Interrupt')

	def set_Interrupt(self,Interrupt):
		self.add_query_param('Interrupt',Interrupt)

	def get_GmtWakeup(self):
		return self.get_query_params().get('GmtWakeup')

	def set_GmtWakeup(self,GmtWakeup):
		self.add_query_param('GmtWakeup',GmtWakeup)

	def get_Pk(self):
		return self.get_query_params().get('Pk')

	def set_Pk(self,Pk):
		self.add_query_param('Pk',Pk)

	def get_Bid(self):
		return self.get_query_params().get('Bid')

	def set_Bid(self,Bid):
		self.add_query_param('Bid',Bid)

	def get_Prompt(self):
		return self.get_query_params().get('Prompt')

	def set_Prompt(self,Prompt):
		self.add_query_param('Prompt',Prompt)

	def get_TaskExtraData(self):
		return self.get_query_params().get('TaskExtraData')

	def set_TaskExtraData(self,TaskExtraData):
		self.add_query_param('TaskExtraData',TaskExtraData)

	def get_TaskIdentifier(self):
		return self.get_query_params().get('TaskIdentifier')

	def set_TaskIdentifier(self,TaskIdentifier):
		self.add_query_param('TaskIdentifier',TaskIdentifier)