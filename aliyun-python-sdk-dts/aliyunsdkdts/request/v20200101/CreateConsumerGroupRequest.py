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

class CreateConsumerGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'CreateConsumerGroup','dts')
		self.set_method('POST')

	def get_ConsumerGroupName(self):
		return self.get_query_params().get('ConsumerGroupName')

	def set_ConsumerGroupName(self,ConsumerGroupName):
		self.add_query_param('ConsumerGroupName',ConsumerGroupName)

	def get_SubscriptionInstanceId(self):
		return self.get_query_params().get('SubscriptionInstanceId')

	def set_SubscriptionInstanceId(self,SubscriptionInstanceId):
		self.add_query_param('SubscriptionInstanceId',SubscriptionInstanceId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ConsumerGroupPassword(self):
		return self.get_query_params().get('ConsumerGroupPassword')

	def set_ConsumerGroupPassword(self,ConsumerGroupPassword):
		self.add_query_param('ConsumerGroupPassword',ConsumerGroupPassword)

	def get_AccountId(self):
		return self.get_query_params().get('AccountId')

	def set_AccountId(self,AccountId):
		self.add_query_param('AccountId',AccountId)

	def get_ConsumerGroupUserName(self):
		return self.get_query_params().get('ConsumerGroupUserName')

	def set_ConsumerGroupUserName(self,ConsumerGroupUserName):
		self.add_query_param('ConsumerGroupUserName',ConsumerGroupUserName)