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

class DescribeAlertsWithEventRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'DescribeAlertsWithEvent','cloud-siem')
		self.set_method('POST')

	def get_Source(self): # String
		return self.get_body_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_body_params('Source', Source)
	def get_IsDefend(self): # String
		return self.get_body_params().get('IsDefend')

	def set_IsDefend(self, IsDefend):  # String
		self.add_body_params('IsDefend', IsDefend)
	def get_SubUserId(self): # Long
		return self.get_body_params().get('SubUserId')

	def set_SubUserId(self, SubUserId):  # Long
		self.add_body_params('SubUserId', SubUserId)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_Levels(self): # RepeatList
		return self.get_body_params().get('Level')

	def set_Levels(self, Level):  # RepeatList
		for depth1 in range(len(Level)):
			self.add_body_params('Level.' + str(depth1 + 1), Level[depth1])
	def get_AlertTitle(self): # String
		return self.get_body_params().get('AlertTitle')

	def set_AlertTitle(self, AlertTitle):  # String
		self.add_body_params('AlertTitle', AlertTitle)
	def get_CurrentPage(self): # Integer
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_body_params('CurrentPage', CurrentPage)
	def get_IncidentUuid(self): # String
		return self.get_body_params().get('IncidentUuid')

	def set_IncidentUuid(self, IncidentUuid):  # String
		self.add_body_params('IncidentUuid', IncidentUuid)
