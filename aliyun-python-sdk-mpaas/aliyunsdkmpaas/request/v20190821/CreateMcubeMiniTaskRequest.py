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

class CreateMcubeMiniTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mPaaS', '2019-08-21', 'CreateMcubeMiniTask')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PackageId(self):
		return self.get_body_params().get('PackageId')

	def set_PackageId(self,PackageId):
		self.add_body_params('PackageId', PackageId)

	def get_Memo(self):
		return self.get_body_params().get('Memo')

	def set_Memo(self,Memo):
		self.add_body_params('Memo', Memo)

	def get_GreyConfigInfo(self):
		return self.get_body_params().get('GreyConfigInfo')

	def set_GreyConfigInfo(self,GreyConfigInfo):
		self.add_body_params('GreyConfigInfo', GreyConfigInfo)

	def get_TenantId(self):
		return self.get_body_params().get('TenantId')

	def set_TenantId(self,TenantId):
		self.add_body_params('TenantId', TenantId)

	def get_PublishMode(self):
		return self.get_body_params().get('PublishMode')

	def set_PublishMode(self,PublishMode):
		self.add_body_params('PublishMode', PublishMode)

	def get_WhitelistIds(self):
		return self.get_body_params().get('WhitelistIds')

	def set_WhitelistIds(self,WhitelistIds):
		self.add_body_params('WhitelistIds', WhitelistIds)

	def get_PublishType(self):
		return self.get_body_params().get('PublishType')

	def set_PublishType(self,PublishType):
		self.add_body_params('PublishType', PublishType)

	def get_GreyNum(self):
		return self.get_body_params().get('GreyNum')

	def set_GreyNum(self,GreyNum):
		self.add_body_params('GreyNum', GreyNum)

	def get_AppId(self):
		return self.get_body_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_body_params('AppId', AppId)

	def get_GreyEndtimeData(self):
		return self.get_body_params().get('GreyEndtimeData')

	def set_GreyEndtimeData(self,GreyEndtimeData):
		self.add_body_params('GreyEndtimeData', GreyEndtimeData)

	def get_WorkspaceId(self):
		return self.get_body_params().get('WorkspaceId')

	def set_WorkspaceId(self,WorkspaceId):
		self.add_body_params('WorkspaceId', WorkspaceId)