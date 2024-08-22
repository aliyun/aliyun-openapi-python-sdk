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

class CreateUserInvestigationInfoQueryTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Buss', '2022-08-22', 'CreateUserInvestigationInfoQueryTask')
		self.set_method('GET')

	def get_dataType(self): # String
		return self.get_query_params().get('dataType')

	def set_dataType(self, dataType):  # String
		self.add_query_param('dataType', dataType)
	def get_endTime(self): # Long
		return self.get_query_params().get('endTime')

	def set_endTime(self, endTime):  # Long
		self.add_query_param('endTime', endTime)
	def get_startTime(self): # Long
		return self.get_query_params().get('startTime')

	def set_startTime(self, startTime):  # Long
		self.add_query_param('startTime', startTime)
	def get_userId(self): # String
		return self.get_query_params().get('userId')

	def set_userId(self, userId):  # String
		self.add_query_param('userId', userId)
	def get_employeeId(self): # String
		return self.get_query_params().get('employeeId')

	def set_employeeId(self, employeeId):  # String
		self.add_query_param('employeeId', employeeId)
	def get_ossFileName(self): # String
		return self.get_query_params().get('ossFileName')

	def set_ossFileName(self, ossFileName):  # String
		self.add_query_param('ossFileName', ossFileName)
