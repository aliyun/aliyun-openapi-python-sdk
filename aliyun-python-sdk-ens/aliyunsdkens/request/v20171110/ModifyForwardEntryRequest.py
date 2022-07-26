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

class ModifyForwardEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'ModifyForwardEntry','ens')
		self.set_method('POST')

	def get_ForwardEntryId(self): # String
		return self.get_query_params().get('ForwardEntryId')

	def set_ForwardEntryId(self, ForwardEntryId):  # String
		self.add_query_param('ForwardEntryId', ForwardEntryId)
	def get_ForwardEntryName(self): # String
		return self.get_query_params().get('ForwardEntryName')

	def set_ForwardEntryName(self, ForwardEntryName):  # String
		self.add_query_param('ForwardEntryName', ForwardEntryName)
	def get_HealthCheckPort(self): # Integer
		return self.get_query_params().get('HealthCheckPort')

	def set_HealthCheckPort(self, HealthCheckPort):  # Integer
		self.add_query_param('HealthCheckPort', HealthCheckPort)
