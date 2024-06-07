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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class CreateDIAlarmRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateDIAlarmRule')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MetricType(self): # String
		return self.get_body_params().get('MetricType')

	def set_MetricType(self, MetricType):  # String
		self.add_body_params('MetricType', MetricType)
	def get_TriggerConditions(self): # String
		return self.get_body_params().get('TriggerConditions')

	def set_TriggerConditions(self, TriggerConditions):  # String
		self.add_body_params('TriggerConditions', TriggerConditions)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_NotificationSettings(self): # String
		return self.get_body_params().get('NotificationSettings')

	def set_NotificationSettings(self, NotificationSettings):  # String
		self.add_body_params('NotificationSettings', NotificationSettings)
	def get_Enabled(self): # Boolean
		return self.get_body_params().get('Enabled')

	def set_Enabled(self, Enabled):  # Boolean
		self.add_body_params('Enabled', Enabled)
	def get_DIJobId(self): # Long
		return self.get_body_params().get('DIJobId')

	def set_DIJobId(self, DIJobId):  # Long
		self.add_body_params('DIJobId', DIJobId)
