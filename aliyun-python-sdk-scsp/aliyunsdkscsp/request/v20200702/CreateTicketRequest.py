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
from aliyunsdkscsp.endpoint import endpoint_data

class CreateTicketRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'scsp', '2020-07-02', 'CreateTicket')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_TemplateId(self): # Long
		return self.get_body_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # Long
		self.add_body_params('TemplateId', TemplateId)
	def get_CategoryId(self): # Long
		return self.get_body_params().get('CategoryId')

	def set_CategoryId(self, CategoryId):  # Long
		self.add_body_params('CategoryId', CategoryId)
	def get_CreatorId(self): # Long
		return self.get_body_params().get('CreatorId')

	def set_CreatorId(self, CreatorId):  # Long
		self.add_body_params('CreatorId', CreatorId)
	def get_CreatorType(self): # Integer
		return self.get_body_params().get('CreatorType')

	def set_CreatorType(self, CreatorType):  # Integer
		self.add_body_params('CreatorType', CreatorType)
	def get_CreatorName(self): # String
		return self.get_body_params().get('CreatorName')

	def set_CreatorName(self, CreatorName):  # String
		self.add_body_params('CreatorName', CreatorName)
	def get_MemberId(self): # Long
		return self.get_body_params().get('MemberId')

	def set_MemberId(self, MemberId):  # Long
		self.add_body_params('MemberId', MemberId)
	def get_MemberName(self): # String
		return self.get_body_params().get('MemberName')

	def set_MemberName(self, MemberName):  # String
		self.add_body_params('MemberName', MemberName)
	def get_FromInfo(self): # String
		return self.get_body_params().get('FromInfo')

	def set_FromInfo(self, FromInfo):  # String
		self.add_body_params('FromInfo', FromInfo)
	def get_Priority(self): # Integer
		return self.get_body_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_body_params('Priority', Priority)
	def get_CarbonCopy(self): # String
		return self.get_body_params().get('CarbonCopy')

	def set_CarbonCopy(self, CarbonCopy):  # String
		self.add_body_params('CarbonCopy', CarbonCopy)
	def get_FormData(self): # String
		return self.get_body_params().get('FormData')

	def set_FormData(self, FormData):  # String
		self.add_body_params('FormData', FormData)
