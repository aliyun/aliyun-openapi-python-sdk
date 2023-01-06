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
from aliyunsdkquotas.endpoint import endpoint_data

class UpdateQuotaAlarmRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quotas', '2020-05-10', 'UpdateQuotaAlarm','quotas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_WebHook(self): # String
		return self.get_body_params().get('WebHook')

	def set_WebHook(self, WebHook):  # String
		self.add_body_params('WebHook', WebHook)
	def get_Threshold(self): # Float
		return self.get_body_params().get('Threshold')

	def set_Threshold(self, Threshold):  # Float
		self.add_body_params('Threshold', Threshold)
	def get_ThresholdType(self): # String
		return self.get_body_params().get('ThresholdType')

	def set_ThresholdType(self, ThresholdType):  # String
		self.add_body_params('ThresholdType', ThresholdType)
	def get_ThresholdPercent(self): # Float
		return self.get_body_params().get('ThresholdPercent')

	def set_ThresholdPercent(self, ThresholdPercent):  # Float
		self.add_body_params('ThresholdPercent', ThresholdPercent)
	def get_AlarmId(self): # String
		return self.get_body_params().get('AlarmId')

	def set_AlarmId(self, AlarmId):  # String
		self.add_body_params('AlarmId', AlarmId)
	def get_AlarmName(self): # String
		return self.get_body_params().get('AlarmName')

	def set_AlarmName(self, AlarmName):  # String
		self.add_body_params('AlarmName', AlarmName)
