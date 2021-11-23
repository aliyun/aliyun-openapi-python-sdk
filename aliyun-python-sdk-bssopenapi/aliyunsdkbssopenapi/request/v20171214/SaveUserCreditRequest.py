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
from aliyunsdkbssopenapi.endpoint import endpoint_data

class SaveUserCreditRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'SaveUserCredit')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AvoidExpiration(self): # Boolean
		return self.get_query_params().get('AvoidExpiration')

	def set_AvoidExpiration(self, AvoidExpiration):  # Boolean
		self.add_query_param('AvoidExpiration', AvoidExpiration)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_AvoidPrepaidNotification(self): # Boolean
		return self.get_query_params().get('AvoidPrepaidNotification')

	def set_AvoidPrepaidNotification(self, AvoidPrepaidNotification):  # Boolean
		self.add_query_param('AvoidPrepaidNotification', AvoidPrepaidNotification)
	def get_AvoidPrepaidExpiration(self): # Boolean
		return self.get_query_params().get('AvoidPrepaidExpiration')

	def set_AvoidPrepaidExpiration(self, AvoidPrepaidExpiration):  # Boolean
		self.add_query_param('AvoidPrepaidExpiration', AvoidPrepaidExpiration)
	def get_AvoidNotification(self): # Boolean
		return self.get_query_params().get('AvoidNotification')

	def set_AvoidNotification(self, AvoidNotification):  # Boolean
		self.add_query_param('AvoidNotification', AvoidNotification)
	def get_Operator(self): # String
		return self.get_query_params().get('Operator')

	def set_Operator(self, Operator):  # String
		self.add_query_param('Operator', Operator)
	def get_CreditValue(self): # String
		return self.get_query_params().get('CreditValue')

	def set_CreditValue(self, CreditValue):  # String
		self.add_query_param('CreditValue', CreditValue)
	def get_CreditType(self): # String
		return self.get_query_params().get('CreditType')

	def set_CreditType(self, CreditType):  # String
		self.add_query_param('CreditType', CreditType)
