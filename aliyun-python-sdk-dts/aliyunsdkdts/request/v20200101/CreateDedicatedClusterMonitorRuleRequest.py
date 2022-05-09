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
from aliyunsdkdts.endpoint import endpoint_data

class CreateDedicatedClusterMonitorRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'CreateDedicatedClusterMonitorRule','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CpuAlarmThreshold(self): # Long
		return self.get_query_params().get('CpuAlarmThreshold')

	def set_CpuAlarmThreshold(self, CpuAlarmThreshold):  # Long
		self.add_query_param('CpuAlarmThreshold', CpuAlarmThreshold)
	def get_Phones(self): # String
		return self.get_query_params().get('Phones')

	def set_Phones(self, Phones):  # String
		self.add_query_param('Phones', Phones)
	def get_DedicatedClusterId(self): # String
		return self.get_query_params().get('DedicatedClusterId')

	def set_DedicatedClusterId(self, DedicatedClusterId):  # String
		self.add_query_param('DedicatedClusterId', DedicatedClusterId)
	def get_DiskAlarmThreshold(self): # Long
		return self.get_query_params().get('DiskAlarmThreshold')

	def set_DiskAlarmThreshold(self, DiskAlarmThreshold):  # Long
		self.add_query_param('DiskAlarmThreshold', DiskAlarmThreshold)
	def get_MemAlarmThreshold(self): # Long
		return self.get_query_params().get('MemAlarmThreshold')

	def set_MemAlarmThreshold(self, MemAlarmThreshold):  # Long
		self.add_query_param('MemAlarmThreshold', MemAlarmThreshold)
	def get_DuAlarmThreshold(self): # Long
		return self.get_query_params().get('DuAlarmThreshold')

	def set_DuAlarmThreshold(self, DuAlarmThreshold):  # Long
		self.add_query_param('DuAlarmThreshold', DuAlarmThreshold)
	def get_OwnerId(self): # String
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # String
		self.add_query_param('OwnerId', OwnerId)
	def get_NoticeSwitch(self): # Long
		return self.get_query_params().get('NoticeSwitch')

	def set_NoticeSwitch(self, NoticeSwitch):  # Long
		self.add_query_param('NoticeSwitch', NoticeSwitch)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
