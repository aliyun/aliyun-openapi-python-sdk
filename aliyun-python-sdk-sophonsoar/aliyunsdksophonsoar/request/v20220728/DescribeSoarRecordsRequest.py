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

class DescribeSoarRecordsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sophonsoar', '2022-07-28', 'DescribeSoarRecords')
		self.set_protocol_type('https')
		self.set_method('GET')

	def get_TaskflowMd5(self): # String
		return self.get_query_params().get('TaskflowMd5')

	def set_TaskflowMd5(self, TaskflowMd5):  # String
		self.add_query_param('TaskflowMd5', TaskflowMd5)
	def get_EndMillis(self): # Long
		return self.get_query_params().get('EndMillis')

	def set_EndMillis(self, EndMillis):  # Long
		self.add_query_param('EndMillis', EndMillis)
	def get_StartMillis(self): # Long
		return self.get_query_params().get('StartMillis')

	def set_StartMillis(self, StartMillis):  # Long
		self.add_query_param('StartMillis', StartMillis)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_TaskStatus(self): # String
		return self.get_query_params().get('TaskStatus')

	def set_TaskStatus(self, TaskStatus):  # String
		self.add_query_param('TaskStatus', TaskStatus)
	def get_PlaybookUuid(self): # String
		return self.get_query_params().get('PlaybookUuid')

	def set_PlaybookUuid(self, PlaybookUuid):  # String
		self.add_query_param('PlaybookUuid', PlaybookUuid)
	def get_RequestUuid(self): # String
		return self.get_query_params().get('RequestUuid')

	def set_RequestUuid(self, RequestUuid):  # String
		self.add_query_param('RequestUuid', RequestUuid)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_TriggerUser(self): # String
		return self.get_query_params().get('TriggerUser')

	def set_TriggerUser(self, TriggerUser):  # String
		self.add_query_param('TriggerUser', TriggerUser)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
