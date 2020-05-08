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
from aliyunsdkemr.endpoint import endpoint_data

class CreateAlertContactRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'CreateAlertContact','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_EmailVerificationCode(self):
		return self.get_query_params().get('EmailVerificationCode')

	def set_EmailVerificationCode(self,EmailVerificationCode):
		self.add_query_param('EmailVerificationCode',EmailVerificationCode)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PhoneNumberVerificationCode(self):
		return self.get_query_params().get('PhoneNumberVerificationCode')

	def set_PhoneNumberVerificationCode(self,PhoneNumberVerificationCode):
		self.add_query_param('PhoneNumberVerificationCode',PhoneNumberVerificationCode)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_PhoneNumber(self):
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self,PhoneNumber):
		self.add_query_param('PhoneNumber',PhoneNumber)

	def get_Email(self):
		return self.get_query_params().get('Email')

	def set_Email(self,Email):
		self.add_query_param('Email',Email)