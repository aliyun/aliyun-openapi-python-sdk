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
from aliyunsdkcloudesl.endpoint import endpoint_data

class AddCompanyTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2020-02-01', 'AddCompanyTemplate')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ExtraParams(self):
		return self.get_body_params().get('ExtraParams')

	def set_ExtraParams(self,ExtraParams):
		self.add_body_params('ExtraParams', ExtraParams)

	def get_EslSize(self):
		return self.get_body_params().get('EslSize')

	def set_EslSize(self,EslSize):
		self.add_body_params('EslSize', EslSize)

	def get_IfPromotion(self):
		return self.get_body_params().get('IfPromotion')

	def set_IfPromotion(self,IfPromotion):
		self.add_body_params('IfPromotion', IfPromotion)

	def get_DeviceType(self):
		return self.get_body_params().get('DeviceType')

	def set_DeviceType(self,DeviceType):
		self.add_body_params('DeviceType', DeviceType)

	def get_Scene(self):
		return self.get_body_params().get('Scene')

	def set_Scene(self,Scene):
		self.add_body_params('Scene', Scene)

	def get_TemplateVersion(self):
		return self.get_body_params().get('TemplateVersion')

	def set_TemplateVersion(self,TemplateVersion):
		self.add_body_params('TemplateVersion', TemplateVersion)

	def get_TemplateType(self):
		return self.get_body_params().get('TemplateType')

	def set_TemplateType(self,TemplateType):
		self.add_body_params('TemplateType', TemplateType)

	def get_Vendor(self):
		return self.get_body_params().get('Vendor')

	def set_Vendor(self,Vendor):
		self.add_body_params('Vendor', Vendor)

	def get_IfDefault(self):
		return self.get_body_params().get('IfDefault')

	def set_IfDefault(self,IfDefault):
		self.add_body_params('IfDefault', IfDefault)

	def get_TemplateName(self):
		return self.get_body_params().get('TemplateName')

	def set_TemplateName(self,TemplateName):
		self.add_body_params('TemplateName', TemplateName)

	def get_IfSourceCode(self):
		return self.get_body_params().get('IfSourceCode')

	def set_IfSourceCode(self,IfSourceCode):
		self.add_body_params('IfSourceCode', IfSourceCode)

	def get_IfMember(self):
		return self.get_body_params().get('IfMember')

	def set_IfMember(self,IfMember):
		self.add_body_params('IfMember', IfMember)

	def get_Layout(self):
		return self.get_body_params().get('Layout')

	def set_Layout(self,Layout):
		self.add_body_params('Layout', Layout)

	def get_IfOutOfInventory(self):
		return self.get_body_params().get('IfOutOfInventory')

	def set_IfOutOfInventory(self,IfOutOfInventory):
		self.add_body_params('IfOutOfInventory', IfOutOfInventory)