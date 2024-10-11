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

class DeleteAdHocFileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataphin-public', '2023-06-30', 'DeleteAdHocFile')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_OpTenantId(self): # Long
		return self.get_query_params().get('OpTenantId')

	def set_OpTenantId(self, OpTenantId):  # Long
		self.add_query_param('OpTenantId', OpTenantId)
	def get_ProjectId(self): # Long
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_query_param('ProjectId', ProjectId)
	def get_FileId(self): # Long
		return self.get_query_params().get('FileId')

	def set_FileId(self, FileId):  # Long
		self.add_query_param('FileId', FileId)
