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
from aliyunsdkram.endpoint import endpoint_data

class SetPasswordPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ram', '2015-05-01', 'SetPasswordPolicy','ram')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PasswordReusePrevention(self): # Integer
		return self.get_query_params().get('PasswordReusePrevention')

	def set_PasswordReusePrevention(self, PasswordReusePrevention):  # Integer
		self.add_query_param('PasswordReusePrevention', PasswordReusePrevention)
	def get_RequireUppercaseCharacters(self): # Boolean
		return self.get_query_params().get('RequireUppercaseCharacters')

	def set_RequireUppercaseCharacters(self, RequireUppercaseCharacters):  # Boolean
		self.add_query_param('RequireUppercaseCharacters', RequireUppercaseCharacters)
	def get_MinimumPasswordLength(self): # Integer
		return self.get_query_params().get('MinimumPasswordLength')

	def set_MinimumPasswordLength(self, MinimumPasswordLength):  # Integer
		self.add_query_param('MinimumPasswordLength', MinimumPasswordLength)
	def get_RequireNumbers(self): # Boolean
		return self.get_query_params().get('RequireNumbers')

	def set_RequireNumbers(self, RequireNumbers):  # Boolean
		self.add_query_param('RequireNumbers', RequireNumbers)
	def get_RequireLowercaseCharacters(self): # Boolean
		return self.get_query_params().get('RequireLowercaseCharacters')

	def set_RequireLowercaseCharacters(self, RequireLowercaseCharacters):  # Boolean
		self.add_query_param('RequireLowercaseCharacters', RequireLowercaseCharacters)
	def get_MaxPasswordAge(self): # Integer
		return self.get_query_params().get('MaxPasswordAge')

	def set_MaxPasswordAge(self, MaxPasswordAge):  # Integer
		self.add_query_param('MaxPasswordAge', MaxPasswordAge)
	def get_MaxLoginAttemps(self): # Integer
		return self.get_query_params().get('MaxLoginAttemps')

	def set_MaxLoginAttemps(self, MaxLoginAttemps):  # Integer
		self.add_query_param('MaxLoginAttemps', MaxLoginAttemps)
	def get_HardExpiry(self): # Boolean
		return self.get_query_params().get('HardExpiry')

	def set_HardExpiry(self, HardExpiry):  # Boolean
		self.add_query_param('HardExpiry', HardExpiry)
	def get_RequireSymbols(self): # Boolean
		return self.get_query_params().get('RequireSymbols')

	def set_RequireSymbols(self, RequireSymbols):  # Boolean
		self.add_query_param('RequireSymbols', RequireSymbols)
