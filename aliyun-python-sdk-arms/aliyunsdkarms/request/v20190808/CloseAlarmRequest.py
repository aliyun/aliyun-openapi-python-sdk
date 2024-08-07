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

class CloseAlarmRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'CloseAlarm','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Solution(self): # String
		return self.get_query_params().get('Solution')

	def set_Solution(self, Solution):  # String
		self.add_query_param('Solution', Solution)
	def get_HandlerId(self): # Long
		return self.get_query_params().get('HandlerId')

	def set_HandlerId(self, HandlerId):  # Long
		self.add_query_param('HandlerId', HandlerId)
	def get_AlarmId(self): # Long
		return self.get_query_params().get('AlarmId')

	def set_AlarmId(self, AlarmId):  # Long
		self.add_query_param('AlarmId', AlarmId)
