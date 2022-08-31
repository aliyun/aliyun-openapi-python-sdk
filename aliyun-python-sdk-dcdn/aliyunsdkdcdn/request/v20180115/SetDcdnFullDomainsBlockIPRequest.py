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
from aliyunsdkdcdn.endpoint import endpoint_data

class SetDcdnFullDomainsBlockIPRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dcdn', '2018-01-15', 'SetDcdnFullDomainsBlockIP')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IPList(self): # String
		return self.get_body_params().get('IPList')

	def set_IPList(self, IPList):  # String
		self.add_body_params('IPList', IPList)
	def get_BlockInterval(self): # Integer
		return self.get_body_params().get('BlockInterval')

	def set_BlockInterval(self, BlockInterval):  # Integer
		self.add_body_params('BlockInterval', BlockInterval)
	def get_OperationType(self): # String
		return self.get_body_params().get('OperationType')

	def set_OperationType(self, OperationType):  # String
		self.add_body_params('OperationType', OperationType)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
