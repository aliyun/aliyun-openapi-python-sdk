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

class ListTagResourcesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BPStudio', '2021-09-31', 'ListTagResources','bpstudio')
		self.set_method('POST')

	def get_ResourceId(self): # Array
		return self.get_body_params().get('ResourceId')

	def set_ResourceId(self, ResourceId):  # Array
		for index1, value1 in enumerate(ResourceId):
			self.add_body_params('ResourceId.' + str(index1 + 1), value1)
	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_ResourceType(self): # String
		return self.get_body_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_body_params('ResourceType', ResourceType)
	def get_NextToken(self): # String
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_body_params('NextToken', NextToken)
	def get_Tag(self): # Array
		return self.get_body_params().get('Tag')

	def set_Tag(self, Tag):  # Array
		for index1, value1 in enumerate(Tag):
			if value1.get('Value') is not None:
				self.add_body_params('Tag.' + str(index1 + 1) + '.Value', value1.get('Value'))
			if value1.get('Key') is not None:
				self.add_body_params('Tag.' + str(index1 + 1) + '.Key', value1.get('Key'))
