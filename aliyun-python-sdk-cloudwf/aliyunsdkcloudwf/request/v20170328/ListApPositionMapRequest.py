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
class ListApPositionMapRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'ListApPositionMap','cloudwf')

	def get_OrderCol(self):
		return self.get_query_params().get('OrderCol')

	def set_OrderCol(self,OrderCol):
		self.add_query_param('OrderCol',OrderCol)

	def get_SearchName(self):
		return self.get_query_params().get('SearchName')

	def set_SearchName(self,SearchName):
		self.add_query_param('SearchName',SearchName)

	def get_TotalItem(self):
		return self.get_query_params().get('TotalItem')

	def set_TotalItem(self,TotalItem):
		self.add_query_param('TotalItem',TotalItem)

	def get_Length(self):
		return self.get_query_params().get('Length')

	def set_Length(self,Length):
		self.add_query_param('Length',Length)

	def get_MapType(self):
		return self.get_query_params().get('MapType')

	def set_MapType(self,MapType):
		self.add_query_param('MapType',MapType)

	def get_PageIndex(self):
		return self.get_query_params().get('PageIndex')

	def set_PageIndex(self,PageIndex):
		self.add_query_param('PageIndex',PageIndex)

	def get_SearchApgroupName(self):
		return self.get_query_params().get('SearchApgroupName')

	def set_SearchApgroupName(self,SearchApgroupName):
		self.add_query_param('SearchApgroupName',SearchApgroupName)

	def get_OrderDir(self):
		return self.get_query_params().get('OrderDir')

	def set_OrderDir(self,OrderDir):
		self.add_query_param('OrderDir',OrderDir)