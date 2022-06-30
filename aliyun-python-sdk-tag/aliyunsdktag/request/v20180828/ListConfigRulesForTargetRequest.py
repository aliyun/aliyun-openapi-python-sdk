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
from aliyunsdktag.endpoint import endpoint_data

class ListConfigRulesForTargetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Tag', '2018-08-28', 'ListConfigRulesForTarget','tag')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TargetId(self): # String
		return self.get_query_params().get('TargetId')

	def set_TargetId(self, TargetId):  # String
		self.add_query_param('TargetId', TargetId)
	def get_TargetType(self): # String
		return self.get_query_params().get('TargetType')

	def set_TargetType(self, TargetType):  # String
		self.add_query_param('TargetType', TargetType)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_PolicyType(self): # String
		return self.get_query_params().get('PolicyType')

	def set_PolicyType(self, PolicyType):  # String
		self.add_query_param('PolicyType', PolicyType)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_UserType(self): # String
		return self.get_query_params().get('UserType')

	def set_UserType(self, UserType):  # String
		self.add_query_param('UserType', UserType)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_MaxResult(self): # Integer
		return self.get_query_params().get('MaxResult')

	def set_MaxResult(self, MaxResult):  # Integer
		self.add_query_param('MaxResult', MaxResult)
	def get_TagKey(self): # String
		return self.get_query_params().get('TagKey')

	def set_TagKey(self, TagKey):  # String
		self.add_query_param('TagKey', TagKey)
