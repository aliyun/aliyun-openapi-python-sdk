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

class ChangeMcubeMiniTaskStatusRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mPaaS', '2019-08-21', 'ChangeMcubeMiniTaskStatus')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PackageId(self):
		return self.get_body_params().get('PackageId')

	def set_PackageId(self,PackageId):
		self.add_body_params('PackageId', PackageId)

	def get_TaskStatus(self):
		return self.get_body_params().get('TaskStatus')

	def set_TaskStatus(self,TaskStatus):
		self.add_body_params('TaskStatus', TaskStatus)

	def get_TenantId(self):
		return self.get_body_params().get('TenantId')

	def set_TenantId(self,TenantId):
		self.add_body_params('TenantId', TenantId)

	def get_TaskId(self):
		return self.get_body_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_body_params('TaskId', TaskId)

	def get_BizType(self):
		return self.get_body_params().get('BizType')

	def set_BizType(self,BizType):
		self.add_body_params('BizType', BizType)

	def get_AppId(self):
		return self.get_body_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_body_params('AppId', AppId)

	def get_WorkspaceId(self):
		return self.get_body_params().get('WorkspaceId')

	def set_WorkspaceId(self,WorkspaceId):
		self.add_body_params('WorkspaceId', WorkspaceId)