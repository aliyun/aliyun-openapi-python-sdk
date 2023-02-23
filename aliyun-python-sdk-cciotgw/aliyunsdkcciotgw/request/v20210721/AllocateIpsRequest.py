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

class AllocateIpsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCIoTGW', '2021-07-21', 'AllocateIps')
		self.set_method('POST')

	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Isp(self): # String
		return self.get_query_params().get('Isp')

	def set_Isp(self, Isp):  # String
		self.add_query_param('Isp', Isp)
	def get_Ipss(self): # RepeatList
		return self.get_query_params().get('Ips')

	def set_Ipss(self, Ips):  # RepeatList
		for depth1 in range(len(Ips)):
			self.add_query_param('Ips.' + str(depth1 + 1), Ips[depth1])
	def get_CciotGwId(self): # String
		return self.get_query_params().get('CciotGwId')

	def set_CciotGwId(self, CciotGwId):  # String
		self.add_query_param('CciotGwId', CciotGwId)
	def get_IpCount(self): # Integer
		return self.get_query_params().get('IpCount')

	def set_IpCount(self, IpCount):  # Integer
		self.add_query_param('IpCount', IpCount)
	def get_Apn(self): # String
		return self.get_query_params().get('Apn')

	def set_Apn(self, Apn):  # String
		self.add_query_param('Apn', Apn)
