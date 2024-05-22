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
from aliyunsdkpolardbx.endpoint import endpoint_data

class ModifyActiveOperationMaintainConfRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardbx', '2020-02-02', 'ModifyActiveOperationMaintainConf','polardbx')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CycleTime(self): # String
		return self.get_query_params().get('CycleTime')

	def set_CycleTime(self, CycleTime):  # String
		self.add_query_param('CycleTime', CycleTime)
	def get_MaintainStartTime(self): # String
		return self.get_query_params().get('MaintainStartTime')

	def set_MaintainStartTime(self, MaintainStartTime):  # String
		self.add_query_param('MaintainStartTime', MaintainStartTime)
	def get_CycleType(self): # String
		return self.get_query_params().get('CycleType')

	def set_CycleType(self, CycleType):  # String
		self.add_query_param('CycleType', CycleType)
	def get_MaintainEndTime(self): # String
		return self.get_query_params().get('MaintainEndTime')

	def set_MaintainEndTime(self, MaintainEndTime):  # String
		self.add_query_param('MaintainEndTime', MaintainEndTime)
	def get_Status(self): # Integer
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_query_param('Status', Status)
