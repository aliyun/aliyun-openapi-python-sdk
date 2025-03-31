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

class PostEventDisposeAndWhiteruleListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'PostEventDisposeAndWhiteruleList','cloud-siem')
		self.set_method('POST')

	def get_RoleFor(self): # Long
		return self.get_body_params().get('RoleFor')

	def set_RoleFor(self, RoleFor):  # Long
		self.add_body_params('RoleFor', RoleFor)
	def get_Remark(self): # String
		return self.get_body_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_body_params('Remark', Remark)
	def get_EventDispose(self): # String
		return self.get_body_params().get('EventDispose')

	def set_EventDispose(self, EventDispose):  # String
		self.add_body_params('EventDispose', EventDispose)
	def get_ReceiverInfo(self): # String
		return self.get_body_params().get('ReceiverInfo')

	def set_ReceiverInfo(self, ReceiverInfo):  # String
		self.add_body_params('ReceiverInfo', ReceiverInfo)
	def get_RoleType(self): # Integer
		return self.get_body_params().get('RoleType')

	def set_RoleType(self, RoleType):  # Integer
		self.add_body_params('RoleType', RoleType)
	def get_ThreatLevel(self): # String
		return self.get_body_params().get('ThreatLevel')

	def set_ThreatLevel(self, ThreatLevel):  # String
		self.add_body_params('ThreatLevel', ThreatLevel)
	def get_IncidentUuid(self): # String
		return self.get_body_params().get('IncidentUuid')

	def set_IncidentUuid(self, IncidentUuid):  # String
		self.add_body_params('IncidentUuid', IncidentUuid)
	def get_Status(self): # Integer
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_body_params('Status', Status)
