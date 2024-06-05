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

class DownloadGatewayProgramRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-dg', '2023-09-14', 'DownloadGatewayProgram')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_UserOS(self): # String
		return self.get_body_params().get('UserOS')

	def set_UserOS(self, UserOS):  # String
		self.add_body_params('UserOS', UserOS)
	def get_DgVersion(self): # String
		return self.get_body_params().get('DgVersion')

	def set_DgVersion(self, DgVersion):  # String
		self.add_body_params('DgVersion', DgVersion)
