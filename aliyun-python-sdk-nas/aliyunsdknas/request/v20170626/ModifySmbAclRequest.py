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
from aliyunsdknas.endpoint import endpoint_data

class ModifySmbAclRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'ModifySmbAcl','nas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EncryptData(self): # Boolean
		return self.get_query_params().get('EncryptData')

	def set_EncryptData(self, EncryptData):  # Boolean
		self.add_query_param('EncryptData', EncryptData)
	def get_Keytab(self): # String
		return self.get_query_params().get('Keytab')

	def set_Keytab(self, Keytab):  # String
		self.add_query_param('Keytab', Keytab)
	def get_SuperAdminSid(self): # String
		return self.get_query_params().get('SuperAdminSid')

	def set_SuperAdminSid(self, SuperAdminSid):  # String
		self.add_query_param('SuperAdminSid', SuperAdminSid)
	def get_KeytabMd5(self): # String
		return self.get_query_params().get('KeytabMd5')

	def set_KeytabMd5(self, KeytabMd5):  # String
		self.add_query_param('KeytabMd5', KeytabMd5)
	def get_RejectUnencryptedAccess(self): # Boolean
		return self.get_query_params().get('RejectUnencryptedAccess')

	def set_RejectUnencryptedAccess(self, RejectUnencryptedAccess):  # Boolean
		self.add_query_param('RejectUnencryptedAccess', RejectUnencryptedAccess)
	def get_FileSystemId(self): # String
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self, FileSystemId):  # String
		self.add_query_param('FileSystemId', FileSystemId)
	def get_HomeDirPath(self): # String
		return self.get_query_params().get('HomeDirPath')

	def set_HomeDirPath(self, HomeDirPath):  # String
		self.add_query_param('HomeDirPath', HomeDirPath)
	def get_EnableAnonymousAccess(self): # Boolean
		return self.get_query_params().get('EnableAnonymousAccess')

	def set_EnableAnonymousAccess(self, EnableAnonymousAccess):  # Boolean
		self.add_query_param('EnableAnonymousAccess', EnableAnonymousAccess)
