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
from aliyunsdkkms.endpoint import endpoint_data

class CreateSecretRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Kms', '2016-01-20', 'CreateSecret','kms')
		self.set_protocol_type('https')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_VersionId(self):
		return self.get_query_params().get('VersionId')

	def set_VersionId(self,VersionId):
		self.add_query_param('VersionId',VersionId)

	def get_SecretData(self):
		return self.get_query_params().get('SecretData')

	def set_SecretData(self,SecretData):
		self.add_query_param('SecretData',SecretData)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_SecretName(self):
		return self.get_query_params().get('SecretName')

	def set_SecretName(self,SecretName):
		self.add_query_param('SecretName',SecretName)

	def get_EncryptionKeyId(self):
		return self.get_query_params().get('EncryptionKeyId')

	def set_EncryptionKeyId(self,EncryptionKeyId):
		self.add_query_param('EncryptionKeyId',EncryptionKeyId)

	def get_SecretDataType(self):
		return self.get_query_params().get('SecretDataType')

	def set_SecretDataType(self,SecretDataType):
		self.add_query_param('SecretDataType',SecretDataType)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_query_param('Tags',Tags)