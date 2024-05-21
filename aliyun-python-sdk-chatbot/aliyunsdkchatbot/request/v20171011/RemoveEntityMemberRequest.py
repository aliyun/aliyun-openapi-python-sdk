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
class RemoveEntityMemberRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Chatbot', '2017-10-11', 'RemoveEntityMember','beebot')

	def get_RemoveType(self):
		return self.get_query_params().get('RemoveType')

	def set_RemoveType(self,RemoveType):
		self.add_query_param('RemoveType',RemoveType)

	def get_Member(self):
		return self.get_body_params().get('Member')

	def set_Member(self,Member):
		self.add_body_params('Member', Member)

	def get_EntityId(self):
		return self.get_query_params().get('EntityId')

	def set_EntityId(self,EntityId):
		self.add_query_param('EntityId',EntityId)