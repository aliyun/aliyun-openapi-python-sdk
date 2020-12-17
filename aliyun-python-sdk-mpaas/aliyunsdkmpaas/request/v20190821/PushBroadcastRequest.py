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

class PushBroadcastRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mPaaS', '2019-08-21', 'PushBroadcast')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TaskName(self):
		return self.get_body_params().get('TaskName')

	def set_TaskName(self,TaskName):
		self.add_body_params('TaskName', TaskName)

	def get_TemplateKeyValue(self):
		return self.get_body_params().get('TemplateKeyValue')

	def set_TemplateKeyValue(self,TemplateKeyValue):
		self.add_body_params('TemplateKeyValue', TemplateKeyValue)

	def get_PushAction(self):
		return self.get_body_params().get('PushAction')

	def set_PushAction(self,PushAction):
		self.add_body_params('PushAction', PushAction)

	def get_DeliveryType(self):
		return self.get_body_params().get('DeliveryType')

	def set_DeliveryType(self,DeliveryType):
		self.add_body_params('DeliveryType', DeliveryType)

	def get_TemplateName(self):
		return self.get_body_params().get('TemplateName')

	def set_TemplateName(self,TemplateName):
		self.add_body_params('TemplateName', TemplateName)

	def get_NotifyType(self):
		return self.get_body_params().get('NotifyType')

	def set_NotifyType(self,NotifyType):
		self.add_body_params('NotifyType', NotifyType)

	def get_ExtendedParams(self):
		return self.get_body_params().get('ExtendedParams')

	def set_ExtendedParams(self,ExtendedParams):
		self.add_body_params('ExtendedParams', ExtendedParams)

	def get_Silent(self):
		return self.get_body_params().get('Silent')

	def set_Silent(self,Silent):
		self.add_body_params('Silent', Silent)

	def get_PushStatus(self):
		return self.get_body_params().get('PushStatus')

	def set_PushStatus(self,PushStatus):
		self.add_body_params('PushStatus', PushStatus)

	def get_UnBindPeriod(self):
		return self.get_body_params().get('UnBindPeriod')

	def set_UnBindPeriod(self,UnBindPeriod):
		self.add_body_params('UnBindPeriod', UnBindPeriod)

	def get_ExpiredSeconds(self):
		return self.get_body_params().get('ExpiredSeconds')

	def set_ExpiredSeconds(self,ExpiredSeconds):
		self.add_body_params('ExpiredSeconds', ExpiredSeconds)

	def get_AppId(self):
		return self.get_body_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_body_params('AppId', AppId)

	def get_Msgkey(self):
		return self.get_body_params().get('Msgkey')

	def set_Msgkey(self,Msgkey):
		self.add_body_params('Msgkey', Msgkey)

	def get_WorkspaceId(self):
		return self.get_body_params().get('WorkspaceId')

	def set_WorkspaceId(self,WorkspaceId):
		self.add_body_params('WorkspaceId', WorkspaceId)