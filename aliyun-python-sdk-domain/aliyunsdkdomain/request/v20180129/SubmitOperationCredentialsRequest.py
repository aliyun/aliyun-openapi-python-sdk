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
from aliyunsdkdomain.endpoint import endpoint_data

class SubmitOperationCredentialsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'SubmitOperationCredentials')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Credentials(self):
		return self.get_query_params().get('Credentials')

	def set_Credentials(self,Credentials):
		self.add_query_param('Credentials',Credentials)

	def get_AuditRecordId(self):
		return self.get_query_params().get('AuditRecordId')

	def set_AuditRecordId(self,AuditRecordId):
		self.add_query_param('AuditRecordId',AuditRecordId)

	def get_RegType(self):
		return self.get_query_params().get('RegType')

	def set_RegType(self,RegType):
		self.add_query_param('RegType',RegType)

	def get_AuditType(self):
		return self.get_query_params().get('AuditType')

	def set_AuditType(self,AuditType):
		self.add_query_param('AuditType',AuditType)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)