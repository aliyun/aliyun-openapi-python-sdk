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
from aliyunsdkmse.endpoint import endpoint_data

class CreateCircuitBreakerRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'CreateCircuitBreakerRule','mse')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Threshold(self): # Float
		return self.get_query_params().get('Threshold')

	def set_Threshold(self, Threshold):  # Float
		self.add_query_param('Threshold', Threshold)
	def get_RetryTimeoutMs(self): # Integer
		return self.get_query_params().get('RetryTimeoutMs')

	def set_RetryTimeoutMs(self, RetryTimeoutMs):  # Integer
		self.add_query_param('RetryTimeoutMs', RetryTimeoutMs)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_Enable(self): # Boolean
		return self.get_query_params().get('Enable')

	def set_Enable(self, Enable):  # Boolean
		self.add_query_param('Enable', Enable)
	def get_MinRequestAmount(self): # Integer
		return self.get_query_params().get('MinRequestAmount')

	def set_MinRequestAmount(self, MinRequestAmount):  # Integer
		self.add_query_param('MinRequestAmount', MinRequestAmount)
	def get_Resource(self): # String
		return self.get_query_params().get('Resource')

	def set_Resource(self, Resource):  # String
		self.add_query_param('Resource', Resource)
	def get_MaxAllowedRtMs(self): # Integer
		return self.get_query_params().get('MaxAllowedRtMs')

	def set_MaxAllowedRtMs(self, MaxAllowedRtMs):  # Integer
		self.add_query_param('MaxAllowedRtMs', MaxAllowedRtMs)
	def get_HalfOpenBaseAmountPerStep(self): # Integer
		return self.get_query_params().get('HalfOpenBaseAmountPerStep')

	def set_HalfOpenBaseAmountPerStep(self, HalfOpenBaseAmountPerStep):  # Integer
		self.add_query_param('HalfOpenBaseAmountPerStep', HalfOpenBaseAmountPerStep)
	def get_StatIntervalMs(self): # Integer
		return self.get_query_params().get('StatIntervalMs')

	def set_StatIntervalMs(self, StatIntervalMs):  # Integer
		self.add_query_param('StatIntervalMs', StatIntervalMs)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
	def get_HalfOpenRecoveryStepNum(self): # Integer
		return self.get_query_params().get('HalfOpenRecoveryStepNum')

	def set_HalfOpenRecoveryStepNum(self, HalfOpenRecoveryStepNum):  # Integer
		self.add_query_param('HalfOpenRecoveryStepNum', HalfOpenRecoveryStepNum)
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
	def get_Strategy(self): # Integer
		return self.get_query_params().get('Strategy')

	def set_Strategy(self, Strategy):  # Integer
		self.add_query_param('Strategy', Strategy)
