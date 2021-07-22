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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class SendTaskMetaCallbackRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2018-06-01', 'SendTaskMetaCallback')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Code(self):
		return self.get_body_params().get('Code')

	def set_Code(self,Code):
		self.add_body_params('Code', Code)

	def get_EndTime(self):
		return self.get_body_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_body_params('EndTime', EndTime)

	def get_Resourcess(self):
		return self.get_body_params().get('Resources')

	def set_Resourcess(self, Resourcess):
		for depth1 in range(len(Resourcess)):
			if Resourcess[depth1] is not None:
				self.add_body_params('Resources.' + str(depth1 + 1) , Resourcess[depth1])

	def get_StartTime(self):
		return self.get_body_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_body_params('StartTime', StartTime)

	def get_Type(self):
		return self.get_body_params().get('Type')

	def set_Type(self,Type):
		self.add_body_params('Type', Type)

	def get_ConnectionInfo(self):
		return self.get_body_params().get('ConnectionInfo')

	def set_ConnectionInfo(self,ConnectionInfo):
		self.add_body_params('ConnectionInfo', ConnectionInfo)

	def get_TaskEnvParam(self):
		return self.get_body_params().get('TaskEnvParam')

	def set_TaskEnvParam(self,TaskEnvParam):
		self.add_body_params('TaskEnvParam', TaskEnvParam)

	def get_SubType(self):
		return self.get_body_params().get('SubType')

	def set_SubType(self,SubType):
		self.add_body_params('SubType', SubType)

	def get_TenantId(self):
		return self.get_body_params().get('TenantId')

	def set_TenantId(self,TenantId):
		self.add_body_params('TenantId', TenantId)

	def get_User(self):
		return self.get_body_params().get('User')

	def set_User(self,User):
		self.add_body_params('User', User)