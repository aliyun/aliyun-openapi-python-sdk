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
from aliyunsdkmpaas.endpoint import endpoint_data

class DeleteMpaasMrtcArtvcRecordfileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mPaaS', '2019-08-21', 'DeleteMpaasMrtcArtvcRecordfile')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TenantId(self):
		return self.get_body_params().get('TenantId')

	def set_TenantId(self,TenantId):
		self.add_body_params('TenantId', TenantId)

	def get_BizRequestId(self):
		return self.get_body_params().get('BizRequestId')

	def set_BizRequestId(self,BizRequestId):
		self.add_body_params('BizRequestId', BizRequestId)

	def get_BizName(self):
		return self.get_body_params().get('BizName')

	def set_BizName(self,BizName):
		self.add_body_params('BizName', BizName)

	def get_BizAppCode(self):
		return self.get_body_params().get('BizAppCode')

	def set_BizAppCode(self,BizAppCode):
		self.add_body_params('BizAppCode', BizAppCode)

	def get_RoomId(self):
		return self.get_body_params().get('RoomId')

	def set_RoomId(self,RoomId):
		self.add_body_params('RoomId', RoomId)

	def get_RecordId(self):
		return self.get_body_params().get('RecordId')

	def set_RecordId(self,RecordId):
		self.add_body_params('RecordId', RecordId)

	def get_S(self):
		return self.get_body_params().get('S')

	def set_S(self,S):
		self.add_body_params('S', S)

	def get_AppId(self):
		return self.get_body_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_body_params('AppId', AppId)

	def get_MediaType(self):
		return self.get_body_params().get('MediaType')

	def set_MediaType(self,MediaType):
		self.add_body_params('MediaType', MediaType)

	def get_WorkspaceId(self):
		return self.get_body_params().get('WorkspaceId')

	def set_WorkspaceId(self,WorkspaceId):
		self.add_body_params('WorkspaceId', WorkspaceId)