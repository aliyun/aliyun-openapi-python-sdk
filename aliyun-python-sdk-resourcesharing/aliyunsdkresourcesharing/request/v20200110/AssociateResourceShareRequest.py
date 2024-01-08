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
from aliyunsdkresourcesharing.endpoint import endpoint_data

class AssociateResourceShareRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceSharing', '2020-01-10', 'AssociateResourceShare','ressharing')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Resourcess(self): # RepeatList
		return self.get_query_params().get('Resources')

	def set_Resourcess(self, Resources):  # RepeatList
		for depth1 in range(len(Resources)):
			if Resources[depth1].get('ResourceId') is not None:
				self.add_query_param('Resources.' + str(depth1 + 1) + '.ResourceId', Resources[depth1].get('ResourceId'))
			if Resources[depth1].get('ResourceType') is not None:
				self.add_query_param('Resources.' + str(depth1 + 1) + '.ResourceType', Resources[depth1].get('ResourceType'))
	def get_Targetss(self): # RepeatList
		return self.get_query_params().get('Targets')

	def set_Targetss(self, Targets):  # RepeatList
		for depth1 in range(len(Targets)):
			self.add_query_param('Targets.' + str(depth1 + 1), Targets[depth1])
	def get_ResourceShareId(self): # String
		return self.get_query_params().get('ResourceShareId')

	def set_ResourceShareId(self, ResourceShareId):  # String
		self.add_query_param('ResourceShareId', ResourceShareId)
	def get_PermissionNamess(self): # RepeatList
		return self.get_query_params().get('PermissionNames')

	def set_PermissionNamess(self, PermissionNames):  # RepeatList
		for depth1 in range(len(PermissionNames)):
			self.add_query_param('PermissionNames.' + str(depth1 + 1), PermissionNames[depth1])
