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

class UnAssignPrivateIpAddressRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eflo', '2022-05-30', 'UnAssignPrivateIpAddress','eflo')
		self.set_method('POST')

	def get_SubnetId(self): # String
		return self.get_body_params().get('SubnetId')

	def set_SubnetId(self, SubnetId):  # String
		self.add_body_params('SubnetId', SubnetId)
	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_PrivateIpAddress(self): # String
		return self.get_body_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self, PrivateIpAddress):  # String
		self.add_body_params('PrivateIpAddress', PrivateIpAddress)
	def get_IpName(self): # String
		return self.get_body_params().get('IpName')

	def set_IpName(self, IpName):  # String
		self.add_body_params('IpName', IpName)
	def get_NetworkInterfaceId(self): # String
		return self.get_body_params().get('NetworkInterfaceId')

	def set_NetworkInterfaceId(self, NetworkInterfaceId):  # String
		self.add_body_params('NetworkInterfaceId', NetworkInterfaceId)
