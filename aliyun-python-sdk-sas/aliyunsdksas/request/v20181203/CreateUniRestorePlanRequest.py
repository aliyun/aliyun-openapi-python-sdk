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
from aliyunsdksas.endpoint import endpoint_data

class CreateUniRestorePlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'CreateUniRestorePlan','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_InstanceUuid(self): # String
		return self.get_query_params().get('InstanceUuid')

	def set_InstanceUuid(self, InstanceUuid):  # String
		self.add_query_param('InstanceUuid', InstanceUuid)
	def get_RestoreInfo(self): # String
		return self.get_query_params().get('RestoreInfo')

	def set_RestoreInfo(self, RestoreInfo):  # String
		self.add_query_param('RestoreInfo', RestoreInfo)
	def get_Database(self): # String
		return self.get_query_params().get('Database')

	def set_Database(self, Database):  # String
		self.add_query_param('Database', Database)
	def get_PolicyId(self): # Long
		return self.get_query_params().get('PolicyId')

	def set_PolicyId(self, PolicyId):  # Long
		self.add_query_param('PolicyId', PolicyId)
	def get_ResetScn(self): # String
		return self.get_query_params().get('ResetScn')

	def set_ResetScn(self, ResetScn):  # String
		self.add_query_param('ResetScn', ResetScn)
	def get_ResetTime(self): # String
		return self.get_query_params().get('ResetTime')

	def set_ResetTime(self, ResetTime):  # String
		self.add_query_param('ResetTime', ResetTime)
	def get_TimePoint(self): # Long
		return self.get_query_params().get('TimePoint')

	def set_TimePoint(self, TimePoint):  # Long
		self.add_query_param('TimePoint', TimePoint)
