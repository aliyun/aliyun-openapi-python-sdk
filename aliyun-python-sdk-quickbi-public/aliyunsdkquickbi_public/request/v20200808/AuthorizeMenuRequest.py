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
from aliyunsdkquickbi_public.endpoint import endpoint_data

class AuthorizeMenuRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2020-08-08', 'AuthorizeMenu','quickbi')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DataPortalId(self):
		return self.get_query_params().get('DataPortalId')

	def set_DataPortalId(self,DataPortalId):
		self.add_query_param('DataPortalId',DataPortalId)

	def get_UserIds(self):
		return self.get_query_params().get('UserIds')

	def set_UserIds(self,UserIds):
		self.add_query_param('UserIds',UserIds)

	def get_UserGroupIds(self):
		return self.get_query_params().get('UserGroupIds')

	def set_UserGroupIds(self,UserGroupIds):
		self.add_query_param('UserGroupIds',UserGroupIds)

	def get_MenuIds(self):
		return self.get_query_params().get('MenuIds')

	def set_MenuIds(self,MenuIds):
		self.add_query_param('MenuIds',MenuIds)