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

class UpdateIntegrationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'UpdateIntegration','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ShortToken(self): # String
		return self.get_body_params().get('ShortToken')

	def set_ShortToken(self, ShortToken):  # String
		self.add_body_params('ShortToken', ShortToken)
	def get_FieldRedefineRules(self): # String
		return self.get_body_params().get('FieldRedefineRules')

	def set_FieldRedefineRules(self, FieldRedefineRules):  # String
		self.add_body_params('FieldRedefineRules', FieldRedefineRules)
	def get_Stat(self): # String
		return self.get_body_params().get('Stat')

	def set_Stat(self, Stat):  # String
		self.add_body_params('Stat', Stat)
	def get_Liveness(self): # String
		return self.get_body_params().get('Liveness')

	def set_Liveness(self, Liveness):  # String
		self.add_body_params('Liveness', Liveness)
	def get_IntegrationId(self): # Long
		return self.get_body_params().get('IntegrationId')

	def set_IntegrationId(self, IntegrationId):  # Long
		self.add_body_params('IntegrationId', IntegrationId)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_ApiEndpoint(self): # String
		return self.get_body_params().get('ApiEndpoint')

	def set_ApiEndpoint(self, ApiEndpoint):  # String
		self.add_body_params('ApiEndpoint', ApiEndpoint)
	def get_AutoRecover(self): # Boolean
		return self.get_body_params().get('AutoRecover')

	def set_AutoRecover(self, AutoRecover):  # Boolean
		self.add_body_params('AutoRecover', AutoRecover)
	def get_RecoverTime(self): # Long
		return self.get_body_params().get('RecoverTime')

	def set_RecoverTime(self, RecoverTime):  # Long
		self.add_body_params('RecoverTime', RecoverTime)
	def get_DuplicateKey(self): # String
		return self.get_body_params().get('DuplicateKey')

	def set_DuplicateKey(self, DuplicateKey):  # String
		self.add_body_params('DuplicateKey', DuplicateKey)
	def get_IntegrationName(self): # String
		return self.get_body_params().get('IntegrationName')

	def set_IntegrationName(self, IntegrationName):  # String
		self.add_body_params('IntegrationName', IntegrationName)
	def get_State(self): # Boolean
		return self.get_body_params().get('State')

	def set_State(self, State):  # Boolean
		self.add_body_params('State', State)
	def get_ExtendedFieldRedefineRules(self): # String
		return self.get_body_params().get('ExtendedFieldRedefineRules')

	def set_ExtendedFieldRedefineRules(self, ExtendedFieldRedefineRules):  # String
		self.add_body_params('ExtendedFieldRedefineRules', ExtendedFieldRedefineRules)
	def get_IntegrationProductType(self): # String
		return self.get_body_params().get('IntegrationProductType')

	def set_IntegrationProductType(self, IntegrationProductType):  # String
		self.add_body_params('IntegrationProductType', IntegrationProductType)
