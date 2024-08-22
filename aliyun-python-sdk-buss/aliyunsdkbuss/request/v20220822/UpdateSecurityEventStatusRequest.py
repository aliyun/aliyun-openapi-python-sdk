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

class UpdateSecurityEventStatusRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Buss', '2022-08-22', 'UpdateSecurityEventStatus')
		self.set_protocol_type('https')
		self.set_method('GET')

	def get_EventId(self): # String
		return self.get_query_params().get('EventId')

	def set_EventId(self, EventId):  # String
		self.add_query_param('EventId', EventId)
	def get_callerParentId(self): # Long
		return self.get_query_params().get('callerParentId')

	def set_callerParentId(self, callerParentId):  # Long
		self.add_query_param('callerParentId', callerParentId)
	def get_AliUid(self): # String
		return self.get_query_params().get('AliUid')

	def set_AliUid(self, AliUid):  # String
		self.add_query_param('AliUid', AliUid)
	def get_callerType(self): # String
		return self.get_query_params().get('callerType')

	def set_callerType(self, callerType):  # String
		self.add_query_param('callerType', callerType)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
	def get_callerUid(self): # Long
		return self.get_query_params().get('callerUid')

	def set_callerUid(self, callerUid):  # Long
		self.add_query_param('callerUid', callerUid)
