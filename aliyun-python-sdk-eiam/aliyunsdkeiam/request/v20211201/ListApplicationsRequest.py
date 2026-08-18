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

class ListApplicationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'ListApplications','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_ResourceServerStatus(self): # String
		return self.get_query_params().get('ResourceServerStatus')

	def set_ResourceServerStatus(self, ResourceServerStatus):  # String
		self.add_query_param('ResourceServerStatus', ResourceServerStatus)
	def get_PageNumber(self): # Long
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Long
		self.add_query_param('PageNumber', PageNumber)
	def get_M2MClientStatus(self): # String
		return self.get_query_params().get('M2MClientStatus')

	def set_M2MClientStatus(self, M2MClientStatus):  # String
		self.add_query_param('M2MClientStatus', M2MClientStatus)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_AuthorizationType(self): # String
		return self.get_query_params().get('AuthorizationType')

	def set_AuthorizationType(self, AuthorizationType):  # String
		self.add_query_param('AuthorizationType', AuthorizationType)
	def get_ApplicationName(self): # String
		return self.get_query_params().get('ApplicationName')

	def set_ApplicationName(self, ApplicationName):  # String
		self.add_query_param('ApplicationName', ApplicationName)
	def get_ApplicationIds(self): # Array
		return self.get_query_params().get('ApplicationIds')

	def set_ApplicationIds(self, ApplicationIds):  # Array
		for index1, value1 in enumerate(ApplicationIds):
			self.add_query_param('ApplicationIds.' + str(index1 + 1), value1)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_SsoType(self): # String
		return self.get_query_params().get('SsoType')

	def set_SsoType(self, SsoType):  # String
		self.add_query_param('SsoType', SsoType)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
