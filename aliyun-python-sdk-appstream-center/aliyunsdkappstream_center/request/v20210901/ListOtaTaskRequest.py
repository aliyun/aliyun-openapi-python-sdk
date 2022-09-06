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

class ListOtaTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'appstream-center', '2021-09-01', 'ListOtaTask')
		self.set_method('POST')

	def get_OtaType(self): # String
		return self.get_body_params().get('OtaType')

	def set_OtaType(self, OtaType):  # String
		self.add_body_params('OtaType', OtaType)
	def get_PageNumber(self): # Integer
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_body_params('PageNumber', PageNumber)
	def get_AppInstanceGroupId(self): # String
		return self.get_body_params().get('AppInstanceGroupId')

	def set_AppInstanceGroupId(self, AppInstanceGroupId):  # String
		self.add_body_params('AppInstanceGroupId', AppInstanceGroupId)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
