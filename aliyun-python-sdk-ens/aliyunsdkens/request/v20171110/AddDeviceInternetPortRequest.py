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

class AddDeviceInternetPortRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'AddDeviceInternetPort','ens')
		self.set_method('GET')

	def get_ISP(self): # String
		return self.get_query_params().get('ISP')

	def set_ISP(self, ISP):  # String
		self.add_query_param('ISP', ISP)
	def get_InternalIp(self): # String
		return self.get_query_params().get('InternalIp')

	def set_InternalIp(self, InternalIp):  # String
		self.add_query_param('InternalIp', InternalIp)
	def get_NatType(self): # String
		return self.get_query_params().get('NatType')

	def set_NatType(self, NatType):  # String
		self.add_query_param('NatType', NatType)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_InternalPort(self): # String
		return self.get_query_params().get('InternalPort')

	def set_InternalPort(self, InternalPort):  # String
		self.add_query_param('InternalPort', InternalPort)
