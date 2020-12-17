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

class PushSimpleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mPaaS', '2019-08-21', 'PushSimple')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TaskName(self):
		return self.get_body_params().get('TaskName')

	def set_TaskName(self,TaskName):
		self.add_body_params('TaskName', TaskName)

	def get_Title(self):
		return self.get_body_params().get('Title')

	def set_Title(self,Title):
		self.add_body_params('Title', Title)

	def get_Content(self):
		return self.get_body_params().get('Content')

	def set_Content(self,Content):
		self.add_body_params('Content', Content)

	def get_PushAction(self):
		return self.get_body_params().get('PushAction')

	def set_PushAction(self,PushAction):
		self.add_body_params('PushAction', PushAction)

	def get_DeliveryType(self):
		return self.get_body_params().get('DeliveryType')

	def set_DeliveryType(self,DeliveryType):
		self.add_body_params('DeliveryType', DeliveryType)

	def get_NotifyType(self):
		return self.get_body_params().get('NotifyType')

	def set_NotifyType(self,NotifyType):
		self.add_body_params('NotifyType', NotifyType)

	def get_TargetMsgkey(self):
		return self.get_body_params().get('TargetMsgkey')

	def set_TargetMsgkey(self,TargetMsgkey):
		self.add_body_params('TargetMsgkey', TargetMsgkey)

	def get_ExtendedParams(self):
		return self.get_body_params().get('ExtendedParams')

	def set_ExtendedParams(self,ExtendedParams):
		self.add_body_params('ExtendedParams', ExtendedParams)

	def get_Silent(self):
		return self.get_body_params().get('Silent')

	def set_Silent(self,Silent):
		self.add_body_params('Silent', Silent)

	def get_Uri(self):
		return self.get_body_params().get('Uri')

	def set_Uri(self,Uri):
		self.add_body_params('Uri', Uri)

	def get_ExpiredSeconds(self):
		return self.get_body_params().get('ExpiredSeconds')

	def set_ExpiredSeconds(self,ExpiredSeconds):
		self.add_body_params('ExpiredSeconds', ExpiredSeconds)

	def get_AppId(self):
		return self.get_body_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_body_params('AppId', AppId)

	def get_WorkspaceId(self):
		return self.get_body_params().get('WorkspaceId')

	def set_WorkspaceId(self,WorkspaceId):
		self.add_body_params('WorkspaceId', WorkspaceId)