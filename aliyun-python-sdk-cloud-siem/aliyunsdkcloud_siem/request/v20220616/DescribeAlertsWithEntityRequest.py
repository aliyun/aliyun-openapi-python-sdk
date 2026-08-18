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

class DescribeAlertsWithEntityRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'DescribeAlertsWithEntity','cloud-siem')
		self.set_method('POST')

	def get_RoleFor(self): # Long
		return self.get_body_params().get('RoleFor')

	def set_RoleFor(self, RoleFor):  # Long
		self.add_body_params('RoleFor', RoleFor)
	def get_EntityId(self): # Long
		return self.get_body_params().get('EntityId')

	def set_EntityId(self, EntityId):  # Long
		self.add_body_params('EntityId', EntityId)
	def get_StartTime(self): # Long
		return self.get_body_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_body_params('StartTime', StartTime)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_RoleType(self): # Integer
		return self.get_body_params().get('RoleType')

	def set_RoleType(self, RoleType):  # Integer
		self.add_body_params('RoleType', RoleType)
	def get_SophonTaskId(self): # String
		return self.get_body_params().get('SophonTaskId')

	def set_SophonTaskId(self, SophonTaskId):  # String
		self.add_body_params('SophonTaskId', SophonTaskId)
	def get_EndTime(self): # Long
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_body_params('EndTime', EndTime)
	def get_CurrentPage(self): # Integer
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_body_params('CurrentPage', CurrentPage)
	def get_EntityUuid(self): # String
		return self.get_body_params().get('EntityUuid')

	def set_EntityUuid(self, EntityUuid):  # String
		self.add_body_params('EntityUuid', EntityUuid)
	def get_IncidentUuid(self): # String
		return self.get_body_params().get('IncidentUuid')

	def set_IncidentUuid(self, IncidentUuid):  # String
		self.add_body_params('IncidentUuid', IncidentUuid)
