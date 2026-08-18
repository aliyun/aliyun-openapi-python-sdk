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

class DescribeNetworkInterfacesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribeNetworkInterfaces','ens')
		self.set_method('POST')

	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_EnsRegionId(self): # String
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_query_param('EnsRegionId', EnsRegionId)
	def get_NetworkInterfaceName(self): # String
		return self.get_query_params().get('NetworkInterfaceName')

	def set_NetworkInterfaceName(self, NetworkInterfaceName):  # String
		self.add_query_param('NetworkInterfaceName', NetworkInterfaceName)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_NetworkId(self): # String
		return self.get_query_params().get('NetworkId')

	def set_NetworkId(self, NetworkId):  # String
		self.add_query_param('NetworkId', NetworkId)
	def get_Ipv6Address(self): # Array
		return self.get_query_params().get('Ipv6Address')

	def set_Ipv6Address(self, Ipv6Address):  # Array
		for index1, value1 in enumerate(Ipv6Address):
			self.add_query_param('Ipv6Address.' + str(index1 + 1), value1)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
	def get_NetworkInterfaceIds(self): # Array
		return self.get_query_params().get('NetworkInterfaceIds')

	def set_NetworkInterfaceIds(self, NetworkInterfaceIds):  # Array
		for index1, value1 in enumerate(NetworkInterfaceIds):
			self.add_query_param('NetworkInterfaceIds.' + str(index1 + 1), value1)
	def get_SecurityGroupId(self): # String
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self, SecurityGroupId):  # String
		self.add_query_param('SecurityGroupId', SecurityGroupId)
	def get_PageNumber(self): # String
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # String
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_EnsRegionIds(self): # Array
		return self.get_query_params().get('EnsRegionIds')

	def set_EnsRegionIds(self, EnsRegionIds):  # Array
		for index1, value1 in enumerate(EnsRegionIds):
			self.add_query_param('EnsRegionIds.' + str(index1 + 1), value1)
	def get_PrimaryIpAddress(self): # String
		return self.get_query_params().get('PrimaryIpAddress')

	def set_PrimaryIpAddress(self, PrimaryIpAddress):  # String
		self.add_query_param('PrimaryIpAddress', PrimaryIpAddress)
	def get_NetworkInterfaceId(self): # String
		return self.get_query_params().get('NetworkInterfaceId')

	def set_NetworkInterfaceId(self, NetworkInterfaceId):  # String
		self.add_query_param('NetworkInterfaceId', NetworkInterfaceId)
