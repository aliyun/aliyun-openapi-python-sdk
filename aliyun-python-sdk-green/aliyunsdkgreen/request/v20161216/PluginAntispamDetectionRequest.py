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
class PluginAntispamDetectionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2016-12-16', 'PluginAntispamDetection','green')
		self.set_method('POST')

	def get_BizScene(self):
		return self.get_query_params().get('BizScene')

	def set_BizScene(self,BizScene):
		self.add_query_param('BizScene',BizScene)

	def get_ClientVersion(self):
		return self.get_query_params().get('ClientVersion')

	def set_ClientVersion(self,ClientVersion):
		self.add_query_param('ClientVersion',ClientVersion)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_TopicId(self):
		return self.get_query_params().get('TopicId')

	def set_TopicId(self,TopicId):
		self.add_query_param('TopicId',TopicId)

	def get_FeedId(self):
		return self.get_query_params().get('FeedId')

	def set_FeedId(self,FeedId):
		self.add_query_param('FeedId',FeedId)

	def get_Title(self):
		return self.get_query_params().get('Title')

	def set_Title(self,Title):
		self.add_query_param('Title',Title)

	def get_PostTime(self):
		return self.get_query_params().get('PostTime')

	def set_PostTime(self,PostTime):
		self.add_query_param('PostTime',PostTime)

	def get_PostContent(self):
		return self.get_query_params().get('PostContent')

	def set_PostContent(self,PostContent):
		self.add_query_param('PostContent',PostContent)

	def get_PostContentType(self):
		return self.get_query_params().get('PostContentType')

	def set_PostContentType(self,PostContentType):
		self.add_query_param('PostContentType',PostContentType)

	def get_DynamicProp(self):
		return self.get_query_params().get('DynamicProp')

	def set_DynamicProp(self,DynamicProp):
		self.add_query_param('DynamicProp',DynamicProp)