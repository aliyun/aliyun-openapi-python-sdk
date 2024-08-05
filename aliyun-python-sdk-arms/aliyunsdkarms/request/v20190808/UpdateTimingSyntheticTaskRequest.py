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
import json

class UpdateTimingSyntheticTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'UpdateTimingSyntheticTask','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AvailableAssertions(self): # Array
		return self.get_query_params().get('AvailableAssertions')

	def set_AvailableAssertions(self, AvailableAssertions):  # Array
		self.add_query_param("AvailableAssertions", json.dumps(AvailableAssertions))
	def get_CommonSetting(self): # Struct
		return self.get_query_params().get('CommonSetting')

	def set_CommonSetting(self, CommonSetting):  # Struct
		self.add_query_param("CommonSetting", json.dumps(CommonSetting))
	def get_Frequency(self): # String
		return self.get_query_params().get('Frequency')

	def set_Frequency(self, Frequency):  # String
		self.add_query_param('Frequency', Frequency)
	def get_Tags(self): # Array
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Array
		self.add_query_param("Tags", json.dumps(Tags))
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_MonitorConf(self): # Struct
		return self.get_query_params().get('MonitorConf')

	def set_MonitorConf(self, MonitorConf):  # Struct
		self.add_query_param("MonitorConf", json.dumps(MonitorConf))
	def get_CustomPeriod(self): # Struct
		return self.get_query_params().get('CustomPeriod')

	def set_CustomPeriod(self, CustomPeriod):  # Struct
		self.add_query_param("CustomPeriod", json.dumps(CustomPeriod))
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_Monitors(self): # Array
		return self.get_query_params().get('Monitors')

	def set_Monitors(self, Monitors):  # Array
		self.add_query_param("Monitors", json.dumps(Monitors))
