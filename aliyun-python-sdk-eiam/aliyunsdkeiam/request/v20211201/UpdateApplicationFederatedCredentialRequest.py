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

class UpdateApplicationFederatedCredentialRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'UpdateApplicationFederatedCredential','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_ApplicationFederatedCredentialId(self): # String
		return self.get_query_params().get('ApplicationFederatedCredentialId')

	def set_ApplicationFederatedCredentialId(self, ApplicationFederatedCredentialId):  # String
		self.add_query_param('ApplicationFederatedCredentialId', ApplicationFederatedCredentialId)
	def get_AttributeMappings(self): # Array
		return self.get_query_params().get('AttributeMappings')

	def set_AttributeMappings(self, AttributeMappings):  # Array
		for index1, value1 in enumerate(AttributeMappings):
			if value1.get('SourceValueExpression') is not None:
				self.add_query_param('AttributeMappings.' + str(index1 + 1) + '.SourceValueExpression', value1.get('SourceValueExpression'))
			if value1.get('TargetField') is not None:
				self.add_query_param('AttributeMappings.' + str(index1 + 1) + '.TargetField', value1.get('TargetField'))
	def get_ApplicationId(self): # String
		return self.get_query_params().get('ApplicationId')

	def set_ApplicationId(self, ApplicationId):  # String
		self.add_query_param('ApplicationId', ApplicationId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_VerificationCondition(self): # String
		return self.get_query_params().get('VerificationCondition')

	def set_VerificationCondition(self, VerificationCondition):  # String
		self.add_query_param('VerificationCondition', VerificationCondition)
