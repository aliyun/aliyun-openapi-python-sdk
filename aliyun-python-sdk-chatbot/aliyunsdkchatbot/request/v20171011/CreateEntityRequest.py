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
class CreateEntityRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Chatbot', '2017-10-11', 'CreateEntity','beebot')

	def get_Regex(self):
		return self.get_query_params().get('Regex')

	def set_Regex(self,Regex):
		self.add_query_param('Regex',Regex)

	def get_EntityType(self):
		return self.get_query_params().get('EntityType')

	def set_EntityType(self,EntityType):
		self.add_query_param('EntityType',EntityType)

	def get_Members(self):
		return self.get_body_params().get('Members')

	def set_Members(self,Members):
		self.add_body_params('Members', Members)

	def get_EntityName(self):
		return self.get_query_params().get('EntityName')

	def set_EntityName(self,EntityName):
		self.add_query_param('EntityName',EntityName)

	def get_DialogId(self):
		return self.get_query_params().get('DialogId')

	def set_DialogId(self,DialogId):
		self.add_query_param('DialogId',DialogId)