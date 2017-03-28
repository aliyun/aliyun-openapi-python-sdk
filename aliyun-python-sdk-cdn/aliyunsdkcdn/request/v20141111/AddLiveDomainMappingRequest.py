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
class AddLiveDomainMappingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2014-11-11', 'AddLiveDomainMapping')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_PushDomain(self):
		return self.get_query_params().get('PushDomain')

	def set_PushDomain(self,PushDomain):
		self.add_query_param('PushDomain',PushDomain)

	def get_PullDomain(self):
		return self.get_query_params().get('PullDomain')

	def set_PullDomain(self,PullDomain):
		self.add_query_param('PullDomain',PullDomain)