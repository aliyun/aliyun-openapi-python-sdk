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
class ListStaStatusRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'ListStaStatus','cloudwf')

	def get_OrderCol(self):
		return self.get_query_params().get('OrderCol')

	def set_OrderCol(self,OrderCol):
		self.add_query_param('OrderCol',OrderCol)

	def get_SearchGroupName(self):
		return self.get_query_params().get('SearchGroupName')

	def set_SearchGroupName(self,SearchGroupName):
		self.add_query_param('SearchGroupName',SearchGroupName)

	def get_SearchStatus(self):
		return self.get_query_params().get('SearchStatus')

	def set_SearchStatus(self,SearchStatus):
		self.add_query_param('SearchStatus',SearchStatus)

	def get_Length(self):
		return self.get_query_params().get('Length')

	def set_Length(self,Length):
		self.add_query_param('Length',Length)

	def get_SearchUsername(self):
		return self.get_query_params().get('SearchUsername')

	def set_SearchUsername(self,SearchUsername):
		self.add_query_param('SearchUsername',SearchUsername)

	def get_OrderDir(self):
		return self.get_query_params().get('OrderDir')

	def set_OrderDir(self,OrderDir):
		self.add_query_param('OrderDir',OrderDir)

	def get_SearchProtocal(self):
		return self.get_query_params().get('SearchProtocal')

	def set_SearchProtocal(self,SearchProtocal):
		self.add_query_param('SearchProtocal',SearchProtocal)

	def get_SearchSsid(self):
		return self.get_query_params().get('SearchSsid')

	def set_SearchSsid(self,SearchSsid):
		self.add_query_param('SearchSsid',SearchSsid)

	def get_SearchApName(self):
		return self.get_query_params().get('SearchApName')

	def set_SearchApName(self,SearchApName):
		self.add_query_param('SearchApName',SearchApName)

	def get_SearchIp(self):
		return self.get_query_params().get('SearchIp')

	def set_SearchIp(self,SearchIp):
		self.add_query_param('SearchIp',SearchIp)

	def get_PageIndex(self):
		return self.get_query_params().get('PageIndex')

	def set_PageIndex(self,PageIndex):
		self.add_query_param('PageIndex',PageIndex)

	def get_SearchMac(self):
		return self.get_query_params().get('SearchMac')

	def set_SearchMac(self,SearchMac):
		self.add_query_param('SearchMac',SearchMac)

	def get_SearchDescription(self):
		return self.get_query_params().get('SearchDescription')

	def set_SearchDescription(self,SearchDescription):
		self.add_query_param('SearchDescription',SearchDescription)