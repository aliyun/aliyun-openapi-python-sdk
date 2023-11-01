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

class DescribeEntityInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'DescribeEntityInfo','cloud-siem')
		self.set_method('POST')

	def get_EntityIdentity(self): # String
		return self.get_body_params().get('EntityIdentity')

	def set_EntityIdentity(self, EntityIdentity):  # String
		self.add_body_params('EntityIdentity', EntityIdentity)
	def get_EntityId(self): # Long
		return self.get_body_params().get('EntityId')

	def set_EntityId(self, EntityId):  # Long
		self.add_body_params('EntityId', EntityId)
	def get_SophonTaskId(self): # String
		return self.get_body_params().get('SophonTaskId')

	def set_SophonTaskId(self, SophonTaskId):  # String
		self.add_body_params('SophonTaskId', SophonTaskId)
	def get_IncidentUuid(self): # String
		return self.get_body_params().get('IncidentUuid')

	def set_IncidentUuid(self, IncidentUuid):  # String
		self.add_body_params('IncidentUuid', IncidentUuid)
