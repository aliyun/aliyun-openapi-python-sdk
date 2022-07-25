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

class CreateSyntheticTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'CreateSyntheticTask','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TaskType(self): # Long
		return self.get_query_params().get('TaskType')

	def set_TaskType(self, TaskType):  # Long
		self.add_query_param('TaskType', TaskType)
	def get_IntervalType(self): # String
		return self.get_query_params().get('IntervalType')

	def set_IntervalType(self, IntervalType):  # String
		self.add_query_param('IntervalType', IntervalType)
	def get_TaskName(self): # String
		return self.get_query_params().get('TaskName')

	def set_TaskName(self, TaskName):  # String
		self.add_query_param('TaskName', TaskName)
	def get_MonitorList(self): # Array
		return self.get_query_params().get('MonitorList')

	def set_MonitorList(self, MonitorList):  # Array
		self.add_query_param("MonitorList", json.dumps(MonitorList))
	def get_IpType(self): # Long
		return self.get_query_params().get('IpType')

	def set_IpType(self, IpType):  # Long
		self.add_query_param('IpType', IpType)
	def get_Url(self): # String
		return self.get_query_params().get('Url')

	def set_Url(self, Url):  # String
		self.add_query_param('Url', Url)
	def get_IntervalTime(self): # String
		return self.get_query_params().get('IntervalTime')

	def set_IntervalTime(self, IntervalTime):  # String
		self.add_query_param('IntervalTime', IntervalTime)
	def get_CommonParam(self): # Struct
		return self.get_query_params().get('CommonParam')

	def set_CommonParam(self, CommonParam):  # Struct
		self.add_query_param("CommonParam", json.dumps(CommonParam))
	def get_ExtendInterval(self): # Struct
		return self.get_query_params().get('ExtendInterval')

	def set_ExtendInterval(self, ExtendInterval):  # Struct
		self.add_query_param("ExtendInterval", json.dumps(ExtendInterval))
	def get_Net(self): # Struct
		return self.get_query_params().get('Net')

	def set_Net(self, Net):  # Struct
		self.add_query_param("Net", json.dumps(Net))
