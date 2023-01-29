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
from aliyunsdkdbfs.endpoint import endpoint_data
import json

class ModifyAutoSnapshotPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DBFS', '2020-04-18', 'ModifyAutoSnapshotPolicy')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TimePoints(self): # Array
		return self.get_query_params().get('TimePoints')

	def set_TimePoints(self, TimePoints):  # Array
		self.add_query_param("TimePoints", json.dumps(TimePoints))
	def get_RepeatWeekdays(self): # Array
		return self.get_query_params().get('RepeatWeekdays')

	def set_RepeatWeekdays(self, RepeatWeekdays):  # Array
		self.add_query_param("RepeatWeekdays", json.dumps(RepeatWeekdays))
	def get_PolicyId(self): # String
		return self.get_query_params().get('PolicyId')

	def set_PolicyId(self, PolicyId):  # String
		self.add_query_param('PolicyId', PolicyId)
	def get_PolicyName(self): # String
		return self.get_query_params().get('PolicyName')

	def set_PolicyName(self, PolicyName):  # String
		self.add_query_param('PolicyName', PolicyName)
	def get_RetentionDays(self): # Integer
		return self.get_query_params().get('RetentionDays')

	def set_RetentionDays(self, RetentionDays):  # Integer
		self.add_query_param('RetentionDays', RetentionDays)
