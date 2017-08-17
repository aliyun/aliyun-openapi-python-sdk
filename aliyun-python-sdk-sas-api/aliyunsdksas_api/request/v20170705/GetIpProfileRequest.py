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
class GetIpProfileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas-api', '2017-07-05', 'GetIpProfile')

	def get_DeviceIdMd5(self):
		return self.get_query_params().get('DeviceIdMd5')

	def set_DeviceIdMd5(self,DeviceIdMd5):
		self.add_query_param('DeviceIdMd5',DeviceIdMd5)

	def get_Carrier(self):
		return self.get_query_params().get('Carrier')

	def set_Carrier(self,Carrier):
		self.add_query_param('Carrier',Carrier)

	def get_Os(self):
		return self.get_query_params().get('Os')

	def set_Os(self,Os):
		self.add_query_param('Os',Os)

	def get_RequestUrl(self):
		return self.get_query_params().get('RequestUrl')

	def set_RequestUrl(self,RequestUrl):
		self.add_query_param('RequestUrl',RequestUrl)

	def get_Ip(self):
		return self.get_query_params().get('Ip')

	def set_Ip(self,Ip):
		self.add_query_param('Ip',Ip)

	def get_UserAgent(self):
		return self.get_query_params().get('UserAgent')

	def set_UserAgent(self,UserAgent):
		self.add_query_param('UserAgent',UserAgent)

	def get_ConnectionType(self):
		return self.get_query_params().get('ConnectionType')

	def set_ConnectionType(self,ConnectionType):
		self.add_query_param('ConnectionType',ConnectionType)

	def get_SensType(self):
		return self.get_query_params().get('SensType')

	def set_SensType(self,SensType):
		self.add_query_param('SensType',SensType)

	def get_DeviceType(self):
		return self.get_query_params().get('DeviceType')

	def set_DeviceType(self,DeviceType):
		self.add_query_param('DeviceType',DeviceType)

	def get_BusinessType(self):
		return self.get_query_params().get('BusinessType')

	def set_BusinessType(self,BusinessType):
		self.add_query_param('BusinessType',BusinessType)