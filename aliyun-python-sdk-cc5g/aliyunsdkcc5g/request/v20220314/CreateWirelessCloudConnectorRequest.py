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

class CreateWirelessCloudConnectorRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CC5G', '2022-03-14', 'CreateWirelessCloudConnector','fivegcc')
		self.set_method('POST')

	def get_UseCase(self): # String
		return self.get_query_params().get('UseCase')

	def set_UseCase(self, UseCase):  # String
		self.add_query_param('UseCase', UseCase)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ISP(self): # String
		return self.get_query_params().get('ISP')

	def set_ISP(self, ISP):  # String
		self.add_query_param('ISP', ISP)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_BusinessType(self): # String
		return self.get_query_params().get('BusinessType')

	def set_BusinessType(self, BusinessType):  # String
		self.add_query_param('BusinessType', BusinessType)
	def get_NetLinks(self): # Array
		return self.get_query_params().get('NetLinks')

	def set_NetLinks(self, NetLinks):  # Array
		for index1, value1 in enumerate(NetLinks):
			if value1.get('RegionId') is not None:
				self.add_query_param('NetLinks.' + str(index1 + 1) + '.RegionId', value1.get('RegionId'))
			if value1.get('VpcId') is not None:
				self.add_query_param('NetLinks.' + str(index1 + 1) + '.VpcId', value1.get('VpcId'))
			if value1.get('VSwitchs') is not None:
				for index2, value2 in enumerate(value1.get('VSwitchs')):
					self.add_query_param('NetLinks.' + str(index1 + 1) + '.VSwitchs.' + str(index2 + 1), value2)
			if value1.get('APN') is not None:
				self.add_query_param('NetLinks.' + str(index1 + 1) + '.APN', value1.get('APN'))
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
