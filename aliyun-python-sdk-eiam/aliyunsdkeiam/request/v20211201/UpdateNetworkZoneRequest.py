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

class UpdateNetworkZoneRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'UpdateNetworkZone','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Ipv6Cidrs(self): # Array
		return self.get_query_params().get('Ipv6Cidrs')

	def set_Ipv6Cidrs(self, Ipv6Cidrs):  # Array
		for index1, value1 in enumerate(Ipv6Cidrs):
			self.add_query_param('Ipv6Cidrs.' + str(index1 + 1), value1)
	def get_NetworkZoneId(self): # String
		return self.get_query_params().get('NetworkZoneId')

	def set_NetworkZoneId(self, NetworkZoneId):  # String
		self.add_query_param('NetworkZoneId', NetworkZoneId)
	def get_NetworkZoneName(self): # String
		return self.get_query_params().get('NetworkZoneName')

	def set_NetworkZoneName(self, NetworkZoneName):  # String
		self.add_query_param('NetworkZoneName', NetworkZoneName)
	def get_Ipv4Cidrs(self): # Array
		return self.get_query_params().get('Ipv4Cidrs')

	def set_Ipv4Cidrs(self, Ipv4Cidrs):  # Array
		for index1, value1 in enumerate(Ipv4Cidrs):
			self.add_query_param('Ipv4Cidrs.' + str(index1 + 1), value1)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
