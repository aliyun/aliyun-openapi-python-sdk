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

class GetVmListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'GetVmList','ens')
		self.set_method('GET')

	def get_InstanceUuid(self): # String
		return self.get_query_params().get('InstanceUuid')

	def set_InstanceUuid(self, InstanceUuid):  # String
		self.add_query_param('InstanceUuid', InstanceUuid)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_GroupUuid(self): # String
		return self.get_query_params().get('GroupUuid')

	def set_GroupUuid(self, GroupUuid):  # String
		self.add_query_param('GroupUuid', GroupUuid)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_AliUid(self): # Long
		return self.get_query_params().get('AliUid')

	def set_AliUid(self, AliUid):  # Long
		self.add_query_param('AliUid', AliUid)
	def get_WorkloadUuid(self): # String
		return self.get_query_params().get('WorkloadUuid')

	def set_WorkloadUuid(self, WorkloadUuid):  # String
		self.add_query_param('WorkloadUuid', WorkloadUuid)
