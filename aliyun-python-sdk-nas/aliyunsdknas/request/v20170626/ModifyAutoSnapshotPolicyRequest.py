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
from aliyunsdknas.endpoint import endpoint_data

class ModifyAutoSnapshotPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'ModifyAutoSnapshotPolicy','nas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AutoSnapshotPolicyId(self): # String
		return self.get_query_params().get('AutoSnapshotPolicyId')

	def set_AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):  # String
		self.add_query_param('AutoSnapshotPolicyId', AutoSnapshotPolicyId)
	def get_TimePoints(self): # String
		return self.get_query_params().get('TimePoints')

	def set_TimePoints(self, TimePoints):  # String
		self.add_query_param('TimePoints', TimePoints)
	def get_RepeatWeekdays(self): # String
		return self.get_query_params().get('RepeatWeekdays')

	def set_RepeatWeekdays(self, RepeatWeekdays):  # String
		self.add_query_param('RepeatWeekdays', RepeatWeekdays)
	def get_AutoSnapshotPolicyName(self): # String
		return self.get_query_params().get('AutoSnapshotPolicyName')

	def set_AutoSnapshotPolicyName(self, AutoSnapshotPolicyName):  # String
		self.add_query_param('AutoSnapshotPolicyName', AutoSnapshotPolicyName)
	def get_RetentionDays(self): # Integer
		return self.get_query_params().get('RetentionDays')

	def set_RetentionDays(self, RetentionDays):  # Integer
		self.add_query_param('RetentionDays', RetentionDays)
