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
from aliyunsdkrds.endpoint import endpoint_data

class CreateReplicationLinkRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'CreateReplicationLink','rds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ReplicatorAccount(self): # String
		return self.get_query_params().get('ReplicatorAccount')

	def set_ReplicatorAccount(self, ReplicatorAccount):  # String
		self.add_query_param('ReplicatorAccount', ReplicatorAccount)
	def get_TaskName(self): # String
		return self.get_query_params().get('TaskName')

	def set_TaskName(self, TaskName):  # String
		self.add_query_param('TaskName', TaskName)
	def get_SourcePort(self): # Long
		return self.get_query_params().get('SourcePort')

	def set_SourcePort(self, SourcePort):  # Long
		self.add_query_param('SourcePort', SourcePort)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_TaskId(self): # Long
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # Long
		self.add_query_param('TaskId', TaskId)
	def get_SourceInstanceName(self): # String
		return self.get_query_params().get('SourceInstanceName')

	def set_SourceInstanceName(self, SourceInstanceName):  # String
		self.add_query_param('SourceInstanceName', SourceInstanceName)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_SourceInstanceRegionId(self): # String
		return self.get_query_params().get('SourceInstanceRegionId')

	def set_SourceInstanceRegionId(self, SourceInstanceRegionId):  # String
		self.add_query_param('SourceInstanceRegionId', SourceInstanceRegionId)
	def get_TargetAddress(self): # String
		return self.get_query_params().get('TargetAddress')

	def set_TargetAddress(self, TargetAddress):  # String
		self.add_query_param('TargetAddress', TargetAddress)
	def get_ReplicatorPassword(self): # String
		return self.get_query_params().get('ReplicatorPassword')

	def set_ReplicatorPassword(self, ReplicatorPassword):  # String
		self.add_query_param('ReplicatorPassword', ReplicatorPassword)
	def get_SourceAddress(self): # String
		return self.get_query_params().get('SourceAddress')

	def set_SourceAddress(self, SourceAddress):  # String
		self.add_query_param('SourceAddress', SourceAddress)
	def get_SourceCategory(self): # String
		return self.get_query_params().get('SourceCategory')

	def set_SourceCategory(self, SourceCategory):  # String
		self.add_query_param('SourceCategory', SourceCategory)
