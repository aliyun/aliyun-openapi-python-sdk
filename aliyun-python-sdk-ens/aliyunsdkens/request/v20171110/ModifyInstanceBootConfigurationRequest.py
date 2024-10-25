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

class ModifyInstanceBootConfigurationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'ModifyInstanceBootConfiguration','ens')
		self.set_protocol_type('https')
		self.set_method('GET')

	def get_DiskSet(self): # String
		return self.get_query_params().get('DiskSet')

	def set_DiskSet(self, DiskSet):  # String
		self.add_query_param('DiskSet', DiskSet)
	def get_BootType(self): # String
		return self.get_query_params().get('BootType')

	def set_BootType(self, BootType):  # String
		self.add_query_param('BootType', BootType)
	def get_BootSet(self): # String
		return self.get_query_params().get('BootSet')

	def set_BootSet(self, BootSet):  # String
		self.add_query_param('BootSet', BootSet)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
