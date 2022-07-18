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

class CopyCompanyTemplateViewRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2020-02-01', 'CopyCompanyTemplateView')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ExtraParams(self):
		return self.get_body_params().get('ExtraParams')

	def set_ExtraParams(self,ExtraParams):
		self.add_body_params('ExtraParams', ExtraParams)

	def get_TargetName(self):
		return self.get_body_params().get('TargetName')

	def set_TargetName(self,TargetName):
		self.add_body_params('TargetName', TargetName)

	def get_ModelId(self):
		return self.get_body_params().get('ModelId')

	def set_ModelId(self,ModelId):
		self.add_body_params('ModelId', ModelId)

	def get_TargetVersion(self):
		return self.get_body_params().get('TargetVersion')

	def set_TargetVersion(self,TargetVersion):
		self.add_body_params('TargetVersion', TargetVersion)

	def get_TemplateId(self):
		return self.get_body_params().get('TemplateId')

	def set_TemplateId(self,TemplateId):
		self.add_body_params('TemplateId', TemplateId)

	def get_TargetGroupId(self):
		return self.get_body_params().get('TargetGroupId')

	def set_TargetGroupId(self,TargetGroupId):
		self.add_body_params('TargetGroupId', TargetGroupId)