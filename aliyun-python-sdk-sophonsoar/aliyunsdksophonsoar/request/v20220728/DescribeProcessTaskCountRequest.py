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

class DescribeProcessTaskCountRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sophonsoar', '2022-07-28', 'DescribeProcessTaskCount')
		self.set_protocol_type('https')
		self.set_method('GET')

	def get_EntityUuidLists(self): # RepeatList
		return self.get_query_params().get('EntityUuidList')

	def set_EntityUuidLists(self, EntityUuidList):  # RepeatList
		for depth1 in range(len(EntityUuidList)):
			self.add_query_param('EntityUuidList.' + str(depth1 + 1), EntityUuidList[depth1])
	def get_RoleFor(self): # Long
		return self.get_query_params().get('RoleFor')

	def set_RoleFor(self, RoleFor):  # Long
		self.add_query_param('RoleFor', RoleFor)
	def get_RoleType(self): # String
		return self.get_query_params().get('RoleType')

	def set_RoleType(self, RoleType):  # String
		self.add_query_param('RoleType', RoleType)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
