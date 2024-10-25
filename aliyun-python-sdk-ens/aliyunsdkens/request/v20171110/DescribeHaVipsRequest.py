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

class DescribeHaVipsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribeHaVips','ens')
		self.set_method('GET')

	def get_EnsRegionId(self): # String
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_query_param('EnsRegionId', EnsRegionId)
	def get_HaVipId(self): # String
		return self.get_query_params().get('HaVipId')

	def set_HaVipId(self, HaVipId):  # String
		self.add_query_param('HaVipId', HaVipId)
	def get_HaVipAddress(self): # String
		return self.get_query_params().get('HaVipAddress')

	def set_HaVipAddress(self, HaVipAddress):  # String
		self.add_query_param('HaVipAddress', HaVipAddress)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_NetworkId(self): # String
		return self.get_query_params().get('NetworkId')

	def set_NetworkId(self, NetworkId):  # String
		self.add_query_param('NetworkId', NetworkId)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
	def get_PageNumber(self): # String
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # String
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
