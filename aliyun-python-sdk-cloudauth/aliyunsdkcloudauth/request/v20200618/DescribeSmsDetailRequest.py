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
from aliyunsdkcloudauth.endpoint import endpoint_data

class DescribeSmsDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2020-06-18', 'DescribeSmsDetail','cloudauth')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SendStatus(self):
		return self.get_body_params().get('SendStatus')

	def set_SendStatus(self,SendStatus):
		self.add_body_params('SendStatus', SendStatus)

	def get_Mobile(self):
		return self.get_body_params().get('Mobile')

	def set_Mobile(self,Mobile):
		self.add_body_params('Mobile', Mobile)

	def get_CurrentPage(self):
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_body_params('CurrentPage', CurrentPage)

	def get_OuterOrderNo(self):
		return self.get_body_params().get('OuterOrderNo')

	def set_OuterOrderNo(self,OuterOrderNo):
		self.add_body_params('OuterOrderNo', OuterOrderNo)

	def get_SignName(self):
		return self.get_body_params().get('SignName')

	def set_SignName(self,SignName):
		self.add_body_params('SignName', SignName)

	def get_SendDate(self):
		return self.get_body_params().get('SendDate')

	def set_SendDate(self,SendDate):
		self.add_body_params('SendDate', SendDate)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_BizId(self):
		return self.get_body_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_body_params('BizId', BizId)

	def get_TemplateCode(self):
		return self.get_body_params().get('TemplateCode')

	def set_TemplateCode(self,TemplateCode):
		self.add_body_params('TemplateCode', TemplateCode)

	def get_ErrorCode(self):
		return self.get_body_params().get('ErrorCode')

	def set_ErrorCode(self,ErrorCode):
		self.add_body_params('ErrorCode', ErrorCode)