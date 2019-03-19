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
class ListApStatusRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'ListApStatus','cloudwf')

	def get_OrderCol(self):
		return self.get_query_params().get('OrderCol')

	def set_OrderCol(self,OrderCol):
		self.add_query_param('OrderCol',OrderCol)

	def get_SearchName(self):
		return self.get_query_params().get('SearchName')

	def set_SearchName(self,SearchName):
		self.add_query_param('SearchName',SearchName)

	def get_SearchGroupName(self):
		return self.get_query_params().get('SearchGroupName')

	def set_SearchGroupName(self,SearchGroupName):
		self.add_query_param('SearchGroupName',SearchGroupName)

	def get_SearchStatus(self):
		return self.get_query_params().get('SearchStatus')

	def set_SearchStatus(self,SearchStatus):
		self.add_query_param('SearchStatus',SearchStatus)

	def get_SearchWanIp(self):
		return self.get_query_params().get('SearchWanIp')

	def set_SearchWanIp(self,SearchWanIp):
		self.add_query_param('SearchWanIp',SearchWanIp)

	def get_SearchApModelName(self):
		return self.get_query_params().get('SearchApModelName')

	def set_SearchApModelName(self,SearchApModelName):
		self.add_query_param('SearchApModelName',SearchApModelName)

	def get_Length(self):
		return self.get_query_params().get('Length')

	def set_Length(self,Length):
		self.add_query_param('Length',Length)

	def get_OrderDir(self):
		return self.get_query_params().get('OrderDir')

	def set_OrderDir(self,OrderDir):
		self.add_query_param('OrderDir',OrderDir)

	def get_SearchBssEquals(self):
		return self.get_query_params().get('SearchBssEquals')

	def set_SearchBssEquals(self,SearchBssEquals):
		self.add_query_param('SearchBssEquals',SearchBssEquals)

	def get_SearchSwVersion(self):
		return self.get_query_params().get('SearchSwVersion')

	def set_SearchSwVersion(self,SearchSwVersion):
		self.add_query_param('SearchSwVersion',SearchSwVersion)

	def get_SearchCompanyName(self):
		return self.get_query_params().get('SearchCompanyName')

	def set_SearchCompanyName(self,SearchCompanyName):
		self.add_query_param('SearchCompanyName',SearchCompanyName)

	def get_SearchMac(self):
		return self.get_query_params().get('SearchMac')

	def set_SearchMac(self,SearchMac):
		self.add_query_param('SearchMac',SearchMac)

	def get_PageIndex(self):
		return self.get_query_params().get('PageIndex')

	def set_PageIndex(self,PageIndex):
		self.add_query_param('PageIndex',PageIndex)