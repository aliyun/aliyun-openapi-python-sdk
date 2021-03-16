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
from aliyunsdksas.endpoint import endpoint_data

class HandleSecurityEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'HandleSecurityEvents','sas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MarkMissParam(self):
		return self.get_query_params().get('MarkMissParam')

	def set_MarkMissParam(self,MarkMissParam):
		self.add_query_param('MarkMissParam',MarkMissParam)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SecurityEventIdss(self):
		return self.get_query_params().get('SecurityEventIds')

	def set_SecurityEventIdss(self, SecurityEventIdss):
		for depth1 in range(len(SecurityEventIdss)):
			if SecurityEventIdss[depth1] is not None:
				self.add_query_param('SecurityEventIds.' + str(depth1 + 1) , SecurityEventIdss[depth1])

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_OperationCode(self):
		return self.get_query_params().get('OperationCode')

	def set_OperationCode(self,OperationCode):
		self.add_query_param('OperationCode',OperationCode)

	def get_OperationParams(self):
		return self.get_query_params().get('OperationParams')

	def set_OperationParams(self,OperationParams):
		self.add_query_param('OperationParams',OperationParams)

	def get_MarkBatch(self):
		return self.get_query_params().get('MarkBatch')

	def set_MarkBatch(self,MarkBatch):
		self.add_query_param('MarkBatch',MarkBatch)