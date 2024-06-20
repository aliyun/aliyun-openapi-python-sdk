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

class LookupWmInfoMappingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'LookupWmInfoMapping')
		self.set_protocol_type('https')
		self.set_method('GET')

	def get_WmInfoUint(self): # String
		return self.get_query_params().get('WmInfoUint')

	def set_WmInfoUint(self, WmInfoUint):  # String
		self.add_query_param('WmInfoUint', WmInfoUint)
	def get_WmInfoSize(self): # Long
		return self.get_query_params().get('WmInfoSize')

	def set_WmInfoSize(self, WmInfoSize):  # Long
		self.add_query_param('WmInfoSize', WmInfoSize)
	def get_WmType(self): # String
		return self.get_query_params().get('WmType')

	def set_WmType(self, WmType):  # String
		self.add_query_param('WmType', WmType)
