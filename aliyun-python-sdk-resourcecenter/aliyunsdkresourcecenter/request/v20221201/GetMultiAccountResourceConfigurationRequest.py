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

class GetMultiAccountResourceConfigurationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceCenter', '2022-12-01', 'GetMultiAccountResourceConfiguration')
		self.set_method('POST')

	def get_AccountId(self): # String
		return self.get_query_params().get('AccountId')

	def set_AccountId(self, AccountId):  # String
		self.add_query_param('AccountId', AccountId)
	def get_ResourceRegionId(self): # String
		return self.get_query_params().get('ResourceRegionId')

	def set_ResourceRegionId(self, ResourceRegionId):  # String
		self.add_query_param('ResourceRegionId', ResourceRegionId)
	def get_ResourceId(self): # String
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self, ResourceId):  # String
		self.add_query_param('ResourceId', ResourceId)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
