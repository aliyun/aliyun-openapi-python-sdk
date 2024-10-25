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

class DescribeSecondaryPublicIpAddressesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribeSecondaryPublicIpAddresses','ens')
		self.set_method('POST')

	def get_SecondaryPublicIpId(self): # String
		return self.get_query_params().get('SecondaryPublicIpId')

	def set_SecondaryPublicIpId(self, SecondaryPublicIpId):  # String
		self.add_query_param('SecondaryPublicIpId', SecondaryPublicIpId)
	def get_Isp(self): # String
		return self.get_query_params().get('Isp')

	def set_Isp(self, Isp):  # String
		self.add_query_param('Isp', Isp)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_EnsRegionId(self): # String
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_query_param('EnsRegionId', EnsRegionId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_SecondaryPublicIpAddress(self): # String
		return self.get_query_params().get('SecondaryPublicIpAddress')

	def set_SecondaryPublicIpAddress(self, SecondaryPublicIpAddress):  # String
		self.add_query_param('SecondaryPublicIpAddress', SecondaryPublicIpAddress)
