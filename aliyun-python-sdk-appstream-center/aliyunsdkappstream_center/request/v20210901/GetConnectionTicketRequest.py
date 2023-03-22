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

class GetConnectionTicketRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'appstream-center', '2021-09-01', 'GetConnectionTicket')
		self.set_method('POST')

	def get_BizRegionId(self): # String
		return self.get_body_params().get('BizRegionId')

	def set_BizRegionId(self, BizRegionId):  # String
		self.add_body_params('BizRegionId', BizRegionId)
	def get_AppStartParam(self): # String
		return self.get_body_params().get('AppStartParam')

	def set_AppStartParam(self, AppStartParam):  # String
		self.add_body_params('AppStartParam', AppStartParam)
	def get_ProductType(self): # String
		return self.get_body_params().get('ProductType')

	def set_ProductType(self, ProductType):  # String
		self.add_body_params('ProductType', ProductType)
	def get_EndUserId(self): # String
		return self.get_body_params().get('EndUserId')

	def set_EndUserId(self, EndUserId):  # String
		self.add_body_params('EndUserId', EndUserId)
	def get_TaskId(self): # String
		return self.get_body_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_body_params('TaskId', TaskId)
	def get_AppVersion(self): # String
		return self.get_body_params().get('AppVersion')

	def set_AppVersion(self, AppVersion):  # String
		self.add_body_params('AppVersion', AppVersion)
	def get_AppInstanceGroupIdLists(self): # RepeatList
		return self.get_body_params().get('AppInstanceGroupIdList')

	def set_AppInstanceGroupIdLists(self, AppInstanceGroupIdList):  # RepeatList
		for depth1 in range(len(AppInstanceGroupIdList)):
			self.add_body_params('AppInstanceGroupIdList.' + str(depth1 + 1), AppInstanceGroupIdList[depth1])
	def get_AppId(self): # String
		return self.get_body_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_body_params('AppId', AppId)
	def get_AppInstanceId(self): # String
		return self.get_body_params().get('AppInstanceId')

	def set_AppInstanceId(self, AppInstanceId):  # String
		self.add_body_params('AppInstanceId', AppInstanceId)
