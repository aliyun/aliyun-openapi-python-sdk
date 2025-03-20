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

class CreateConditionalAccessPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'CreateConditionalAccessPolicy','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ConditionsConfig(self): # Struct
		return self.get_query_params().get('ConditionsConfig')

	def set_ConditionsConfig(self, ConditionsConfig):  # Struct
		if ConditionsConfig.get('NetworkZones') is not None:
			if ConditionsConfig.get('NetworkZones').get('ExcludeNetworkZones') is not None:
				for index1, value1 in enumerate(ConditionsConfig.get('NetworkZones').get('ExcludeNetworkZones')):
					self.add_query_param('ConditionsConfig.NetworkZones.ExcludeNetworkZones.' + str(index1 + 1), value1)
			if ConditionsConfig.get('NetworkZones').get('IncludeNetworkZones') is not None:
				for index1, value1 in enumerate(ConditionsConfig.get('NetworkZones').get('IncludeNetworkZones')):
					self.add_query_param('ConditionsConfig.NetworkZones.IncludeNetworkZones.' + str(index1 + 1), value1)
		if ConditionsConfig.get('Users') is not None:
			if ConditionsConfig.get('Users').get('IncludeGroups') is not None:
				for index1, value1 in enumerate(ConditionsConfig.get('Users').get('IncludeGroups')):
					self.add_query_param('ConditionsConfig.Users.IncludeGroups.' + str(index1 + 1), value1)
			if ConditionsConfig.get('Users').get('ExcludeUsers') is not None:
				for index1, value1 in enumerate(ConditionsConfig.get('Users').get('ExcludeUsers')):
					self.add_query_param('ConditionsConfig.Users.ExcludeUsers.' + str(index1 + 1), value1)
			if ConditionsConfig.get('Users').get('IncludeOrganizationalUnits') is not None:
				for index1, value1 in enumerate(ConditionsConfig.get('Users').get('IncludeOrganizationalUnits')):
					self.add_query_param('ConditionsConfig.Users.IncludeOrganizationalUnits.' + str(index1 + 1), value1)
			if ConditionsConfig.get('Users').get('ExcludeOrganizationalUnits') is not None:
				for index1, value1 in enumerate(ConditionsConfig.get('Users').get('ExcludeOrganizationalUnits')):
					self.add_query_param('ConditionsConfig.Users.ExcludeOrganizationalUnits.' + str(index1 + 1), value1)
			if ConditionsConfig.get('Users').get('ExcludeGroups') is not None:
				for index1, value1 in enumerate(ConditionsConfig.get('Users').get('ExcludeGroups')):
					self.add_query_param('ConditionsConfig.Users.ExcludeGroups.' + str(index1 + 1), value1)
			if ConditionsConfig.get('Users').get('IncludeUsers') is not None:
				for index1, value1 in enumerate(ConditionsConfig.get('Users').get('IncludeUsers')):
					self.add_query_param('ConditionsConfig.Users.IncludeUsers.' + str(index1 + 1), value1)
		if ConditionsConfig.get('Applications') is not None:
			if ConditionsConfig.get('Applications').get('ExcludeApplications') is not None:
				for index1, value1 in enumerate(ConditionsConfig.get('Applications').get('ExcludeApplications')):
					self.add_query_param('ConditionsConfig.Applications.ExcludeApplications.' + str(index1 + 1), value1)
			if ConditionsConfig.get('Applications').get('IncludeApplications') is not None:
				for index1, value1 in enumerate(ConditionsConfig.get('Applications').get('IncludeApplications')):
					self.add_query_param('ConditionsConfig.Applications.IncludeApplications.' + str(index1 + 1), value1)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_ConditionalAccessPolicyType(self): # String
		return self.get_query_params().get('ConditionalAccessPolicyType')

	def set_ConditionalAccessPolicyType(self, ConditionalAccessPolicyType):  # String
		self.add_query_param('ConditionalAccessPolicyType', ConditionalAccessPolicyType)
	def get_DecisionType(self): # String
		return self.get_query_params().get('DecisionType')

	def set_DecisionType(self, DecisionType):  # String
		self.add_query_param('DecisionType', DecisionType)
	def get_EvaluateAt(self): # String
		return self.get_query_params().get('EvaluateAt')

	def set_EvaluateAt(self, EvaluateAt):  # String
		self.add_query_param('EvaluateAt', EvaluateAt)
	def get_Priority(self): # Integer
		return self.get_query_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_query_param('Priority', Priority)
	def get_DecisionConfig(self): # Struct
		return self.get_query_params().get('DecisionConfig')

	def set_DecisionConfig(self, DecisionConfig):  # Struct
		if DecisionConfig.get('MfaType') is not None:
			self.add_query_param('DecisionConfig.MfaType', DecisionConfig.get('MfaType'))
		if DecisionConfig.get('MfaAuthenticationIntervalSeconds') is not None:
			self.add_query_param('DecisionConfig.MfaAuthenticationIntervalSeconds', DecisionConfig.get('MfaAuthenticationIntervalSeconds'))
		if DecisionConfig.get('Effect') is not None:
			self.add_query_param('DecisionConfig.Effect', DecisionConfig.get('Effect'))
		if DecisionConfig.get('ActiveSessionReuseStatus') is not None:
			self.add_query_param('DecisionConfig.ActiveSessionReuseStatus', DecisionConfig.get('ActiveSessionReuseStatus'))
		if DecisionConfig.get('MfaAuthenticationMethods') is not None:
			for index1, value1 in enumerate(DecisionConfig.get('MfaAuthenticationMethods')):
				self.add_query_param('DecisionConfig.MfaAuthenticationMethods.' + str(index1 + 1), value1)
	def get_ConditionalAccessPolicyName(self): # String
		return self.get_query_params().get('ConditionalAccessPolicyName')

	def set_ConditionalAccessPolicyName(self, ConditionalAccessPolicyName):  # String
		self.add_query_param('ConditionalAccessPolicyName', ConditionalAccessPolicyName)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
