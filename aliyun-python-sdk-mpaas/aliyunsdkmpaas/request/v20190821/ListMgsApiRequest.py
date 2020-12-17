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

class ListMgsApiRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mPaaS', '2019-08-21', 'ListMgsApi')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_NeedEtag(self):
		return self.get_body_params().get('NeedEtag')

	def set_NeedEtag(self,NeedEtag):
		self.add_body_params('NeedEtag', NeedEtag)

	def get_ApiType(self):
		return self.get_body_params().get('ApiType')

	def set_ApiType(self,ApiType):
		self.add_body_params('ApiType', ApiType)

	def get_OptFuzzy(self):
		return self.get_body_params().get('OptFuzzy')

	def set_OptFuzzy(self,OptFuzzy):
		self.add_body_params('OptFuzzy', OptFuzzy)

	def get_Host(self):
		return self.get_body_params().get('Host')

	def set_Host(self,Host):
		self.add_body_params('Host', Host)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_TenantId(self):
		return self.get_body_params().get('TenantId')

	def set_TenantId(self,TenantId):
		self.add_body_params('TenantId', TenantId)

	def get_PageIndex(self):
		return self.get_body_params().get('PageIndex')

	def set_PageIndex(self,PageIndex):
		self.add_body_params('PageIndex', PageIndex)

	def get_ApiStatus(self):
		return self.get_body_params().get('ApiStatus')

	def set_ApiStatus(self,ApiStatus):
		self.add_body_params('ApiStatus', ApiStatus)

	def get_SysId(self):
		return self.get_body_params().get('SysId')

	def set_SysId(self,SysId):
		self.add_body_params('SysId', SysId)

	def get_Format(self):
		return self.get_body_params().get('Format')

	def set_Format(self,Format):
		self.add_body_params('Format', Format)

	def get_NeedEncrypt(self):
		return self.get_body_params().get('NeedEncrypt')

	def set_NeedEncrypt(self,NeedEncrypt):
		self.add_body_params('NeedEncrypt', NeedEncrypt)

	def get_OperationType(self):
		return self.get_body_params().get('OperationType')

	def set_OperationType(self,OperationType):
		self.add_body_params('OperationType', OperationType)

	def get_NeedSign(self):
		return self.get_body_params().get('NeedSign')

	def set_NeedSign(self,NeedSign):
		self.add_body_params('NeedSign', NeedSign)

	def get_AppId(self):
		return self.get_body_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_body_params('AppId', AppId)

	def get_SysName(self):
		return self.get_body_params().get('SysName')

	def set_SysName(self,SysName):
		self.add_body_params('SysName', SysName)

	def get_WorkspaceId(self):
		return self.get_body_params().get('WorkspaceId')

	def set_WorkspaceId(self,WorkspaceId):
		self.add_body_params('WorkspaceId', WorkspaceId)