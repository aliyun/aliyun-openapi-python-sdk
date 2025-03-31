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

class SetStorageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'SetStorage','cloud-siem')
		self.set_method('POST')

	def get_RoleFor(self): # Long
		return self.get_body_params().get('RoleFor')

	def set_RoleFor(self, RoleFor):  # Long
		self.add_body_params('RoleFor', RoleFor)
	def get_RoleType(self): # Integer
		return self.get_body_params().get('RoleType')

	def set_RoleType(self, RoleType):  # Integer
		self.add_body_params('RoleType', RoleType)
	def get_Ttl(self): # Integer
		return self.get_body_params().get('Ttl')

	def set_Ttl(self, Ttl):  # Integer
		self.add_body_params('Ttl', Ttl)
	def get_Region(self): # String
		return self.get_body_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_body_params('Region', Region)
