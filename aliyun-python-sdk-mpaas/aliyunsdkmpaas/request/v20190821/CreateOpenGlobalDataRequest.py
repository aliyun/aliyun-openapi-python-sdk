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

class CreateOpenGlobalDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mPaaS', '2019-08-21', 'CreateOpenGlobalData')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ExtAttrStr(self):
		return self.get_body_params().get('ExtAttrStr')

	def set_ExtAttrStr(self,ExtAttrStr):
		self.add_body_params('ExtAttrStr', ExtAttrStr)

	def get_MinUid(self):
		return self.get_body_params().get('MinUid')

	def set_MinUid(self,MinUid):
		self.add_body_params('MinUid', MinUid)

	def get_ThirdMsgId(self):
		return self.get_body_params().get('ThirdMsgId')

	def set_ThirdMsgId(self,ThirdMsgId):
		self.add_body_params('ThirdMsgId', ThirdMsgId)

	def get_ValidTimeEnd(self):
		return self.get_body_params().get('ValidTimeEnd')

	def set_ValidTimeEnd(self,ValidTimeEnd):
		self.add_body_params('ValidTimeEnd', ValidTimeEnd)

	def get_Payload(self):
		return self.get_body_params().get('Payload')

	def set_Payload(self,Payload):
		self.add_body_params('Payload', Payload)

	def get_Uids(self):
		return self.get_body_params().get('Uids')

	def set_Uids(self,Uids):
		self.add_body_params('Uids', Uids)

	def get_AppMinVersion(self):
		return self.get_body_params().get('AppMinVersion')

	def set_AppMinVersion(self,AppMinVersion):
		self.add_body_params('AppMinVersion', AppMinVersion)

	def get_ValidTimeStart(self):
		return self.get_body_params().get('ValidTimeStart')

	def set_ValidTimeStart(self,ValidTimeStart):
		self.add_body_params('ValidTimeStart', ValidTimeStart)

	def get_MaxUid(self):
		return self.get_body_params().get('MaxUid')

	def set_MaxUid(self,MaxUid):
		self.add_body_params('MaxUid', MaxUid)

	def get_OsType(self):
		return self.get_body_params().get('OsType')

	def set_OsType(self,OsType):
		self.add_body_params('OsType', OsType)

	def get_BizType(self):
		return self.get_body_params().get('BizType')

	def set_BizType(self,BizType):
		self.add_body_params('BizType', BizType)

	def get_AppMaxVersion(self):
		return self.get_body_params().get('AppMaxVersion')

	def set_AppMaxVersion(self,AppMaxVersion):
		self.add_body_params('AppMaxVersion', AppMaxVersion)

	def get_AppId(self):
		return self.get_body_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_body_params('AppId', AppId)

	def get_WorkspaceId(self):
		return self.get_body_params().get('WorkspaceId')

	def set_WorkspaceId(self,WorkspaceId):
		self.add_body_params('WorkspaceId', WorkspaceId)