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

class CreateVpdRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eflo', '2022-05-30', 'CreateVpd','eflo')
		self.set_method('POST')

	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_Cidr(self): # String
		return self.get_body_params().get('Cidr')

	def set_Cidr(self, Cidr):  # String
		self.add_body_params('Cidr', Cidr)
	def get_Subnetss(self): # RepeatList
		return self.get_body_params().get('Subnets')

	def set_Subnetss(self, Subnets):  # RepeatList
		for depth1 in range(len(Subnets)):
			if Subnets[depth1].get('RegionId') is not None:
				self.add_body_params('Subnets.' + str(depth1 + 1) + '.RegionId', Subnets[depth1].get('RegionId'))
			if Subnets[depth1].get('Name') is not None:
				self.add_body_params('Subnets.' + str(depth1 + 1) + '.Name', Subnets[depth1].get('Name'))
			if Subnets[depth1].get('ZoneId') is not None:
				self.add_body_params('Subnets.' + str(depth1 + 1) + '.ZoneId', Subnets[depth1].get('ZoneId'))
			if Subnets[depth1].get('Cidr') is not None:
				self.add_body_params('Subnets.' + str(depth1 + 1) + '.Cidr', Subnets[depth1].get('Cidr'))
			if Subnets[depth1].get('Type') is not None:
				self.add_body_params('Subnets.' + str(depth1 + 1) + '.Type', Subnets[depth1].get('Type'))
