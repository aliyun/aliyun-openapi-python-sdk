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
from aliyunsdksmc.endpoint import endpoint_data

class AssociateSourceServersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'smc', '2019-06-01', 'AssociateSourceServers','smc')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SourceIds(self): # RepeatList
		return self.get_query_params().get('SourceId')

	def set_SourceIds(self, SourceId):  # RepeatList
		for depth1 in range(len(SourceId)):
			self.add_query_param('SourceId.' + str(depth1 + 1), SourceId[depth1])
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_WorkgroupId(self): # String
		return self.get_query_params().get('WorkgroupId')

	def set_WorkgroupId(self, WorkgroupId):  # String
		self.add_query_param('WorkgroupId', WorkgroupId)
