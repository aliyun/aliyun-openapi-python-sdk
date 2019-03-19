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
class DoLogicalDeleteResourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Qualitycheck', '2019-01-15', 'DoLogicalDeleteResource')

	def get_Country(self):
		return self.get_query_params().get('Country')

	def set_Country(self,Country):
		self.add_query_param('Country',Country)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Hid(self):
		return self.get_query_params().get('Hid')

	def set_Hid(self,Hid):
		self.add_query_param('Hid',Hid)

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

	def get_Message(self):
		return self.get_query_params().get('Message')

	def set_Message(self,Message):
		self.add_query_param('Message',Message)

	def get_TaskExtraData(self):
		return self.get_query_params().get('TaskExtraData')

	def set_TaskExtraData(self,TaskExtraData):
		self.add_query_param('TaskExtraData',TaskExtraData)

	def get_TaskIdentifier(self):
		return self.get_query_params().get('TaskIdentifier')

	def set_TaskIdentifier(self,TaskIdentifier):
		self.add_query_param('TaskIdentifier',TaskIdentifier)