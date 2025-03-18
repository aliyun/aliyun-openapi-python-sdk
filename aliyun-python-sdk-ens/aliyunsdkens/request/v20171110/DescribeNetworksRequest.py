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

class DescribeNetworksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribeNetworks','ens')
		self.set_method('POST')

	def get_EnsRegionId(self): # String
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_query_param('EnsRegionId', EnsRegionId)
	def get_NetworkIds(self): # Array
		return self.get_query_params().get('NetworkIds')

	def set_NetworkIds(self, NetworkIds):  # Array
		for index1, value1 in enumerate(NetworkIds):
			self.add_query_param('NetworkIds.' + str(index1 + 1), value1)
	def get_NetworkId(self): # String
		return self.get_query_params().get('NetworkId')

	def set_NetworkId(self, NetworkId):  # String
		self.add_query_param('NetworkId', NetworkId)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_NetworkName(self): # String
		return self.get_query_params().get('NetworkName')

	def set_NetworkName(self, NetworkName):  # String
		self.add_query_param('NetworkName', NetworkName)
	def get_EnsRegionIds(self): # Array
		return self.get_query_params().get('EnsRegionIds')

	def set_EnsRegionIds(self, EnsRegionIds):  # Array
		for index1, value1 in enumerate(EnsRegionIds):
			self.add_query_param('EnsRegionIds.' + str(index1 + 1), value1)
