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
from aliyunsdkdypnsapi.endpoint import endpoint_data

class QueryGateVerifyStatisticPublicRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dypnsapi', '2017-05-25', 'QueryGateVerifyStatisticPublic')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AuthenticationType(self):
		return self.get_query_params().get('AuthenticationType')

	def set_AuthenticationType(self,AuthenticationType):
		self.add_query_param('AuthenticationType',AuthenticationType)

	def get_StartDate(self):
		return self.get_query_params().get('StartDate')

	def set_StartDate(self,StartDate):
		self.add_query_param('StartDate',StartDate)

	def get_SceneCode(self):
		return self.get_query_params().get('SceneCode')

	def set_SceneCode(self,SceneCode):
		self.add_query_param('SceneCode',SceneCode)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OsType(self):
		return self.get_query_params().get('OsType')

	def set_OsType(self,OsType):
		self.add_query_param('OsType',OsType)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_EndDate(self):
		return self.get_query_params().get('EndDate')

	def set_EndDate(self,EndDate):
		self.add_query_param('EndDate',EndDate)