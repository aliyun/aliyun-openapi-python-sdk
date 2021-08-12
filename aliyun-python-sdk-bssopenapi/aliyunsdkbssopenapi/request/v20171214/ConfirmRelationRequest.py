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
from aliyunsdkbssopenapi.endpoint import endpoint_data

class ConfirmRelationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'ConfirmRelation')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_RelationType(self):
		return self.get_query_params().get('RelationType')

	def set_RelationType(self,RelationType):
		self.add_query_param('RelationType',RelationType)

	def get_ParentUserId(self):
		return self.get_query_params().get('ParentUserId')

	def set_ParentUserId(self,ParentUserId):
		self.add_query_param('ParentUserId',ParentUserId)

	def get_ConfirmCode(self):
		return self.get_query_params().get('ConfirmCode')

	def set_ConfirmCode(self,ConfirmCode):
		self.add_query_param('ConfirmCode',ConfirmCode)

	def get_ChildUserId(self):
		return self.get_query_params().get('ChildUserId')

	def set_ChildUserId(self,ChildUserId):
		self.add_query_param('ChildUserId',ChildUserId)

	def get_RequestId(self):
		return self.get_query_params().get('RequestId')

	def set_RequestId(self,RequestId):
		self.add_query_param('RequestId',RequestId)

	def get_PermissionCodess(self):
		return self.get_query_params().get('PermissionCodes')

	def set_PermissionCodess(self, PermissionCodess):
		for depth1 in range(len(PermissionCodess)):
			if PermissionCodess[depth1] is not None:
				self.add_query_param('PermissionCodes.' + str(depth1 + 1) , PermissionCodess[depth1])