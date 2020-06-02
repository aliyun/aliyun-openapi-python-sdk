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

class CreateRepoTriggerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cr', '2018-12-01', 'CreateRepoTrigger','acr')
		self.set_method('POST')

	def get_RepoId(self):
		return self.get_query_params().get('RepoId')

	def set_RepoId(self,RepoId):
		self.add_query_param('RepoId',RepoId)

	def get_TriggerTag(self):
		return self.get_query_params().get('TriggerTag')

	def set_TriggerTag(self,TriggerTag):
		self.add_query_param('TriggerTag',TriggerTag)

	def get_TriggerType(self):
		return self.get_query_params().get('TriggerType')

	def set_TriggerType(self,TriggerType):
		self.add_query_param('TriggerType',TriggerType)

	def get_TriggerUrl(self):
		return self.get_query_params().get('TriggerUrl')

	def set_TriggerUrl(self,TriggerUrl):
		self.add_query_param('TriggerUrl',TriggerUrl)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_TriggerName(self):
		return self.get_query_params().get('TriggerName')

	def set_TriggerName(self,TriggerName):
		self.add_query_param('TriggerName',TriggerName)