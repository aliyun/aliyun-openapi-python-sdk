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

class UpdateDynamicRouteRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'UpdateDynamicRoute')
		self.set_method('POST')

	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_DynamicRouteId(self): # String
		return self.get_body_params().get('DynamicRouteId')

	def set_DynamicRouteId(self, DynamicRouteId):  # String
		self.add_body_params('DynamicRouteId', DynamicRouteId)
	def get_DynamicRouteType(self): # String
		return self.get_body_params().get('DynamicRouteType')

	def set_DynamicRouteType(self, DynamicRouteType):  # String
		self.add_body_params('DynamicRouteType', DynamicRouteType)
	def get_TagIds(self): # Array
		return self.get_body_params().get('TagIds')

	def set_TagIds(self, TagIds):  # Array
		for index1, value1 in enumerate(TagIds):
			self.add_body_params('TagIds.' + str(index1 + 1), value1)
	def get_RegionIds(self): # Array
		return self.get_body_params().get('RegionIds')

	def set_RegionIds(self, RegionIds):  # Array
		for index1, value1 in enumerate(RegionIds):
			self.add_body_params('RegionIds.' + str(index1 + 1), value1)
	def get_Priority(self): # Integer
		return self.get_body_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_body_params('Priority', Priority)
	def get_NextHop(self): # String
		return self.get_body_params().get('NextHop')

	def set_NextHop(self, NextHop):  # String
		self.add_body_params('NextHop', NextHop)
	def get_ApplicationIds(self): # Array
		return self.get_body_params().get('ApplicationIds')

	def set_ApplicationIds(self, ApplicationIds):  # Array
		for index1, value1 in enumerate(ApplicationIds):
			self.add_body_params('ApplicationIds.' + str(index1 + 1), value1)
	def get_ModifyType(self): # String
		return self.get_body_params().get('ModifyType')

	def set_ModifyType(self, ModifyType):  # String
		self.add_body_params('ModifyType', ModifyType)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_ApplicationType(self): # String
		return self.get_body_params().get('ApplicationType')

	def set_ApplicationType(self, ApplicationType):  # String
		self.add_body_params('ApplicationType', ApplicationType)
	def get_Status(self): # String
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_body_params('Status', Status)
