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
class PluginAntispamResultsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2016-12-16', 'PluginAntispamResults','green')
		self.set_method('POST')

	def get_BizScene(self):
		return self.get_query_params().get('BizScene')

	def set_BizScene(self,BizScene):
		self.add_query_param('BizScene',BizScene)

	def get_ClientVersion(self):
		return self.get_query_params().get('ClientVersion')

	def set_ClientVersion(self,ClientVersion):
		self.add_query_param('ClientVersion',ClientVersion)

	def get_PostContentType(self):
		return self.get_query_params().get('PostContentType')

	def set_PostContentType(self,PostContentType):
		self.add_query_param('PostContentType',PostContentType)

	def get_PageIndex(self):
		return self.get_query_params().get('PageIndex')

	def set_PageIndex(self,PageIndex):
		self.add_query_param('PageIndex',PageIndex)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)