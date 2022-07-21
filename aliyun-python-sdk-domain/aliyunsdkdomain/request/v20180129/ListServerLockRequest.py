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
from aliyunsdkdomain.endpoint import endpoint_data

class ListServerLockRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'ListServerLock')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_LockProductId(self): # String
		return self.get_query_params().get('LockProductId')

	def set_LockProductId(self, LockProductId):  # String
		self.add_query_param('LockProductId', LockProductId)
	def get_EndExpireDate(self): # Long
		return self.get_query_params().get('EndExpireDate')

	def set_EndExpireDate(self, EndExpireDate):  # Long
		self.add_query_param('EndExpireDate', EndExpireDate)
	def get_PageNum(self): # Integer
		return self.get_query_params().get('PageNum')

	def set_PageNum(self, PageNum):  # Integer
		self.add_query_param('PageNum', PageNum)
	def get_BeginStartDate(self): # Long
		return self.get_query_params().get('BeginStartDate')

	def set_BeginStartDate(self, BeginStartDate):  # Long
		self.add_query_param('BeginStartDate', BeginStartDate)
	def get_ServerLockStatus(self): # Integer
		return self.get_query_params().get('ServerLockStatus')

	def set_ServerLockStatus(self, ServerLockStatus):  # Integer
		self.add_query_param('ServerLockStatus', ServerLockStatus)
	def get_StartExpireDate(self): # Long
		return self.get_query_params().get('StartExpireDate')

	def set_StartExpireDate(self, StartExpireDate):  # Long
		self.add_query_param('StartExpireDate', StartExpireDate)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_EndStartDate(self): # Long
		return self.get_query_params().get('EndStartDate')

	def set_EndStartDate(self, EndStartDate):  # Long
		self.add_query_param('EndStartDate', EndStartDate)
	def get_UserClientIp(self): # String
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self, UserClientIp):  # String
		self.add_query_param('UserClientIp', UserClientIp)
