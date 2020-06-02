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

class CreateRepoBuildRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cr', '2018-12-01', 'CreateRepoBuildRule','acr')
		self.set_method('POST')

	def get_RepoId(self):
		return self.get_query_params().get('RepoId')

	def set_RepoId(self,RepoId):
		self.add_query_param('RepoId',RepoId)

	def get_PushName(self):
		return self.get_query_params().get('PushName')

	def set_PushName(self,PushName):
		self.add_query_param('PushName',PushName)

	def get_DockerfileName(self):
		return self.get_query_params().get('DockerfileName')

	def set_DockerfileName(self,DockerfileName):
		self.add_query_param('DockerfileName',DockerfileName)

	def get_DockerfileLocation(self):
		return self.get_query_params().get('DockerfileLocation')

	def set_DockerfileLocation(self,DockerfileLocation):
		self.add_query_param('DockerfileLocation',DockerfileLocation)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_ImageTag(self):
		return self.get_query_params().get('ImageTag')

	def set_ImageTag(self,ImageTag):
		self.add_query_param('ImageTag',ImageTag)

	def get_PushType(self):
		return self.get_query_params().get('PushType')

	def set_PushType(self,PushType):
		self.add_query_param('PushType',PushType)