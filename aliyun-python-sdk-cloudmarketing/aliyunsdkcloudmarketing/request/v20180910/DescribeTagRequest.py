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

class DescribeTagRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudmarketing', '2018-09-10', 'DescribeTag')
		self.set_method('POST')

	def get_StatusLists(self):
		return self.get_query_params().get('StatusLists')

	def set_StatusLists(self, StatusLists):
		for depth1 in range(len(StatusLists)):
			if StatusLists[depth1] is not None:
				self.add_query_param('StatusList.' + str(depth1 + 1) , StatusLists[depth1])

	def get_IncludeChild(self):
		return self.get_query_params().get('IncludeChild')

	def set_IncludeChild(self,IncludeChild):
		self.add_query_param('IncludeChild',IncludeChild)

	def get_OnlyFavorite(self):
		return self.get_query_params().get('OnlyFavorite')

	def set_OnlyFavorite(self,OnlyFavorite):
		self.add_query_param('OnlyFavorite',OnlyFavorite)

	def get_PageNo(self):
		return self.get_query_params().get('PageNo')

	def set_PageNo(self,PageNo):
		self.add_query_param('PageNo',PageNo)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Keyword(self):
		return self.get_query_params().get('Keyword')

	def set_Keyword(self,Keyword):
		self.add_query_param('Keyword',Keyword)

	def get_CategoryId(self):
		return self.get_query_params().get('CategoryId')

	def set_CategoryId(self,CategoryId):
		self.add_query_param('CategoryId',CategoryId)