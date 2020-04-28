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

class UpdateVerifySettingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2019-03-07', 'UpdateVerifySetting','cloudauth')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_GuideStep(self):
		return self.get_query_params().get('GuideStep')

	def set_GuideStep(self,GuideStep):
		self.add_query_param('GuideStep',GuideStep)

	def get_ResultStep(self):
		return self.get_query_params().get('ResultStep')

	def set_ResultStep(self,ResultStep):
		self.add_query_param('ResultStep',ResultStep)

	def get_Solution(self):
		return self.get_query_params().get('Solution')

	def set_Solution(self,Solution):
		self.add_query_param('Solution',Solution)

	def get_BizName(self):
		return self.get_query_params().get('BizName')

	def set_BizName(self,BizName):
		self.add_query_param('BizName',BizName)

	def get_BizType(self):
		return self.get_query_params().get('BizType')

	def set_BizType(self,BizType):
		self.add_query_param('BizType',BizType)

	def get_PrivacyStep(self):
		return self.get_query_params().get('PrivacyStep')

	def set_PrivacyStep(self,PrivacyStep):
		self.add_query_param('PrivacyStep',PrivacyStep)