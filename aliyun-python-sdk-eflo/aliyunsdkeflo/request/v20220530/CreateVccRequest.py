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

class CreateVccRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eflo', '2022-05-30', 'CreateVcc','eflo')
		self.set_method('POST')

	def get_BgpCidr(self): # String
		return self.get_body_params().get('BgpCidr')

	def set_BgpCidr(self, BgpCidr):  # String
		self.add_body_params('BgpCidr', BgpCidr)
	def get_CenId(self): # String
		return self.get_body_params().get('CenId')

	def set_CenId(self, CenId):  # String
		self.add_body_params('CenId', CenId)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_AccessCouldService(self): # Boolean
		return self.get_body_params().get('AccessCouldService')

	def set_AccessCouldService(self, AccessCouldService):  # Boolean
		self.add_body_params('AccessCouldService', AccessCouldService)
	def get_VccId(self): # String
		return self.get_body_params().get('VccId')

	def set_VccId(self, VccId):  # String
		self.add_body_params('VccId', VccId)
	def get_VSwitchId(self): # String
		return self.get_body_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_body_params('VSwitchId', VSwitchId)
	def get_VpdId(self): # String
		return self.get_body_params().get('VpdId')

	def set_VpdId(self, VpdId):  # String
		self.add_body_params('VpdId', VpdId)
	def get_VpcId(self): # String
		return self.get_body_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_body_params('VpcId', VpcId)
