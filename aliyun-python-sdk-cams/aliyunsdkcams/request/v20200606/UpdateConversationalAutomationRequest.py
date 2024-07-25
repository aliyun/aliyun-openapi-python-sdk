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
from aliyunsdkcams.endpoint import endpoint_data
import json

class UpdateConversationalAutomationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cams', '2020-06-06', 'UpdateConversationalAutomation','cams')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_PhoneNumber(self): # String
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self, PhoneNumber):  # String
		self.add_query_param('PhoneNumber', PhoneNumber)
	def get_EnableWelcomeMessage(self): # Boolean
		return self.get_query_params().get('EnableWelcomeMessage')

	def set_EnableWelcomeMessage(self, EnableWelcomeMessage):  # Boolean
		self.add_query_param('EnableWelcomeMessage', EnableWelcomeMessage)
	def get_Commands(self): # Array
		return self.get_query_params().get('Commands')

	def set_Commands(self, Commands):  # Array
		self.add_query_param("Commands", json.dumps(Commands))
	def get_Prompts(self): # Array
		return self.get_query_params().get('Prompts')

	def set_Prompts(self, Prompts):  # Array
		self.add_query_param("Prompts", json.dumps(Prompts))
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_CustSpaceId(self): # String
		return self.get_query_params().get('CustSpaceId')

	def set_CustSpaceId(self, CustSpaceId):  # String
		self.add_query_param('CustSpaceId', CustSpaceId)
