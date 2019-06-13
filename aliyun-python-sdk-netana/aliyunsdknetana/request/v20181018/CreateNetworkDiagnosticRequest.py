# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateNetworkDiagnosticRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Netana', '2018-10-18', 'CreateNetworkDiagnostic','Netana')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_RequestParams(self):
		return self.get_query_params().get('RequestParams')

	def set_RequestParams(self,RequestParams):
		self.add_query_param('RequestParams',RequestParams)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_UserRequestId(self):
		return self.get_query_params().get('UserRequestId')

	def set_UserRequestId(self,UserRequestId):
		self.add_query_param('UserRequestId',UserRequestId)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_RequestApiName(self):
		return self.get_query_params().get('RequestApiName')

	def set_RequestApiName(self,RequestApiName):
		self.add_query_param('RequestApiName',RequestApiName)

	def get_ErrorCode(self):
		return self.get_query_params().get('ErrorCode')

	def set_ErrorCode(self,ErrorCode):
		self.add_query_param('ErrorCode',ErrorCode)

	def get_ProductType(self):
		return self.get_query_params().get('ProductType')

	def set_ProductType(self,ProductType):
		self.add_query_param('ProductType',ProductType)

	def get_ResponseParams(self):
		return self.get_query_params().get('ResponseParams')

	def set_ResponseParams(self,ResponseParams):
		self.add_query_param('ResponseParams',ResponseParams)