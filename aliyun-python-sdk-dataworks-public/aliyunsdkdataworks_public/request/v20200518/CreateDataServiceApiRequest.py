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

class CreateDataServiceApiRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateDataServiceApi')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ScriptDetails(self):
		return self.get_body_params().get('ScriptDetails')

	def set_ScriptDetails(self,ScriptDetails):
		self.add_body_params('ScriptDetails', ScriptDetails)

	def get_RequestMethod(self):
		return self.get_body_params().get('RequestMethod')

	def set_RequestMethod(self,RequestMethod):
		self.add_body_params('RequestMethod', RequestMethod)

	def get_GroupId(self):
		return self.get_body_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_body_params('GroupId', GroupId)

	def get_ApiPath(self):
		return self.get_body_params().get('ApiPath')

	def set_ApiPath(self,ApiPath):
		self.add_body_params('ApiPath', ApiPath)

	def get_WizardDetails(self):
		return self.get_body_params().get('WizardDetails')

	def set_WizardDetails(self,WizardDetails):
		self.add_body_params('WizardDetails', WizardDetails)

	def get_ApiMode(self):
		return self.get_body_params().get('ApiMode')

	def set_ApiMode(self,ApiMode):
		self.add_body_params('ApiMode', ApiMode)

	def get_VisibleRange(self):
		return self.get_body_params().get('VisibleRange')

	def set_VisibleRange(self,VisibleRange):
		self.add_body_params('VisibleRange', VisibleRange)

	def get_ApiDescription(self):
		return self.get_body_params().get('ApiDescription')

	def set_ApiDescription(self,ApiDescription):
		self.add_body_params('ApiDescription', ApiDescription)

	def get_Timeout(self):
		return self.get_body_params().get('Timeout')

	def set_Timeout(self,Timeout):
		self.add_body_params('Timeout', Timeout)

	def get_FolderId(self):
		return self.get_body_params().get('FolderId')

	def set_FolderId(self,FolderId):
		self.add_body_params('FolderId', FolderId)

	def get_RegistrationDetails(self):
		return self.get_body_params().get('RegistrationDetails')

	def set_RegistrationDetails(self,RegistrationDetails):
		self.add_body_params('RegistrationDetails', RegistrationDetails)

	def get_ApiName(self):
		return self.get_body_params().get('ApiName')

	def set_ApiName(self,ApiName):
		self.add_body_params('ApiName', ApiName)

	def get_TenantId(self):
		return self.get_body_params().get('TenantId')

	def set_TenantId(self,TenantId):
		self.add_body_params('TenantId', TenantId)

	def get_Protocols(self):
		return self.get_body_params().get('Protocols')

	def set_Protocols(self,Protocols):
		self.add_body_params('Protocols', Protocols)

	def get_ProjectId(self):
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_body_params('ProjectId', ProjectId)

	def get_ResponseContentType(self):
		return self.get_body_params().get('ResponseContentType')

	def set_ResponseContentType(self,ResponseContentType):
		self.add_body_params('ResponseContentType', ResponseContentType)