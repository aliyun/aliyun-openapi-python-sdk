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

class QueryAsyncJobListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'viapi', '2023-01-17', 'QueryAsyncJobList','viapi')
		self.set_method('POST')

	def get_StartTime(self): # String
		return self.get_body_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_body_params('StartTime', StartTime)
	def get_PageNum(self): # String
		return self.get_body_params().get('PageNum')

	def set_PageNum(self, PageNum):  # String
		self.add_body_params('PageNum', PageNum)
	def get_JobId(self): # String
		return self.get_body_params().get('JobId')

	def set_JobId(self, JobId):  # String
		self.add_body_params('JobId', JobId)
	def get_PopApiName(self): # String
		return self.get_body_params().get('PopApiName')

	def set_PopApiName(self, PopApiName):  # String
		self.add_body_params('PopApiName', PopApiName)
	def get_PageSize(self): # String
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_body_params('PageSize', PageSize)
	def get_PopProduct(self): # String
		return self.get_body_params().get('PopProduct')

	def set_PopProduct(self, PopProduct):  # String
		self.add_body_params('PopProduct', PopProduct)
	def get_EndTime(self): # String
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_body_params('EndTime', EndTime)
	def get_Status(self): # String
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_body_params('Status', Status)
