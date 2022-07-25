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

class CreateIntegrationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'CreateIntegration','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AutoRecover(self): # Boolean
		return self.get_body_params().get('AutoRecover')

	def set_AutoRecover(self, AutoRecover):  # Boolean
		self.add_body_params('AutoRecover', AutoRecover)
	def get_RecoverTime(self): # Long
		return self.get_body_params().get('RecoverTime')

	def set_RecoverTime(self, RecoverTime):  # Long
		self.add_body_params('RecoverTime', RecoverTime)
	def get_IntegrationName(self): # String
		return self.get_body_params().get('IntegrationName')

	def set_IntegrationName(self, IntegrationName):  # String
		self.add_body_params('IntegrationName', IntegrationName)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_IntegrationProductType(self): # String
		return self.get_body_params().get('IntegrationProductType')

	def set_IntegrationProductType(self, IntegrationProductType):  # String
		self.add_body_params('IntegrationProductType', IntegrationProductType)
