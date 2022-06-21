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

class UnassignPrivateIpAddressesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'UnassignPrivateIpAddresses','ens')
		self.set_method('POST')

	def get_PrivateIpAddress(self): # Array
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self, PrivateIpAddress):  # Array
		for index1, value1 in enumerate(PrivateIpAddress):
			self.add_query_param('PrivateIpAddress.' + str(index1 + 1), value1)
	def get_NetworkInterfaceId(self): # String
		return self.get_query_params().get('NetworkInterfaceId')

	def set_NetworkInterfaceId(self, NetworkInterfaceId):  # String
		self.add_query_param('NetworkInterfaceId', NetworkInterfaceId)
