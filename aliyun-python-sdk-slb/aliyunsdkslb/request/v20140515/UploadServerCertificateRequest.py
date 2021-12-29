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
from aliyunsdkslb.endpoint import endpoint_data

class UploadServerCertificateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Slb', '2014-05-15', 'UploadServerCertificate','Slb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ServerCertificate(self): # String
		return self.get_query_params().get('ServerCertificate')

	def set_ServerCertificate(self, ServerCertificate):  # String
		self.add_query_param('ServerCertificate', ServerCertificate)
	def get_AliCloudCertificateName(self): # String
		return self.get_query_params().get('AliCloudCertificateName')

	def set_AliCloudCertificateName(self, AliCloudCertificateName):  # String
		self.add_query_param('AliCloudCertificateName', AliCloudCertificateName)
	def get_AliCloudCertificateId(self): # String
		return self.get_query_params().get('AliCloudCertificateId')

	def set_AliCloudCertificateId(self, AliCloudCertificateId):  # String
		self.add_query_param('AliCloudCertificateId', AliCloudCertificateId)
	def get_PrivateKey(self): # String
		return self.get_query_params().get('PrivateKey')

	def set_PrivateKey(self, PrivateKey):  # String
		self.add_query_param('PrivateKey', PrivateKey)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_AliCloudCertificateRegionId(self): # String
		return self.get_query_params().get('AliCloudCertificateRegionId')

	def set_AliCloudCertificateRegionId(self, AliCloudCertificateRegionId):  # String
		self.add_query_param('AliCloudCertificateRegionId', AliCloudCertificateRegionId)
	def get_ServerCertificateName(self): # String
		return self.get_query_params().get('ServerCertificateName')

	def set_ServerCertificateName(self, ServerCertificateName):  # String
		self.add_query_param('ServerCertificateName', ServerCertificateName)
