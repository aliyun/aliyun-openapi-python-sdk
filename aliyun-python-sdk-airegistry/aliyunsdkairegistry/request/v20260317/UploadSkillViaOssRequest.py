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

class UploadSkillViaOssRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'AIRegistry', '2026-03-17', 'UploadSkillViaOss','AIRegistry')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_NamespaceId(self): # String
		return self.get_query_params().get('NamespaceId')

	def set_NamespaceId(self, NamespaceId):  # String
		self.add_query_param('NamespaceId', NamespaceId)
	def get_Overwrite(self): # Boolean
		return self.get_query_params().get('Overwrite')

	def set_Overwrite(self, Overwrite):  # Boolean
		self.add_query_param('Overwrite', Overwrite)
	def get_TargetVersion(self): # String
		return self.get_query_params().get('TargetVersion')

	def set_TargetVersion(self, TargetVersion):  # String
		self.add_query_param('TargetVersion', TargetVersion)
	def get_OssObjectName(self): # String
		return self.get_query_params().get('OssObjectName')

	def set_OssObjectName(self, OssObjectName):  # String
		self.add_query_param('OssObjectName', OssObjectName)
	def get_CommitMsg(self): # String
		return self.get_query_params().get('CommitMsg')

	def set_CommitMsg(self, CommitMsg):  # String
		self.add_query_param('CommitMsg', CommitMsg)
