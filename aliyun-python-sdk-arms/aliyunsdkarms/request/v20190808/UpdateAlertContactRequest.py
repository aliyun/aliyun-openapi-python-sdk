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
from aliyunsdkarms.endpoint import endpoint_data

class UpdateAlertContactRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'UpdateAlertContact','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ContactId(self): # Long
		return self.get_query_params().get('ContactId')

	def set_ContactId(self, ContactId):  # Long
		self.add_query_param('ContactId', ContactId)
	def get_PhoneNum(self): # String
		return self.get_query_params().get('PhoneNum')

	def set_PhoneNum(self, PhoneNum):  # String
		self.add_query_param('PhoneNum', PhoneNum)
	def get_ContactName(self): # String
		return self.get_query_params().get('ContactName')

	def set_ContactName(self, ContactName):  # String
		self.add_query_param('ContactName', ContactName)
	def get_DingRobotWebhookUrl(self): # String
		return self.get_query_params().get('DingRobotWebhookUrl')

	def set_DingRobotWebhookUrl(self, DingRobotWebhookUrl):  # String
		self.add_query_param('DingRobotWebhookUrl', DingRobotWebhookUrl)
	def get_Email(self): # String
		return self.get_query_params().get('Email')

	def set_Email(self, Email):  # String
		self.add_query_param('Email', Email)
	def get_SystemNoc(self): # Boolean
		return self.get_query_params().get('SystemNoc')

	def set_SystemNoc(self, SystemNoc):  # Boolean
		self.add_query_param('SystemNoc', SystemNoc)
