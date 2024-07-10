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

class ActivateLicenseRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mseap', '2021-01-18', 'ActivateLicense')
		self.set_method('POST')

	def get_LicenseNo(self): # String
		return self.get_query_params().get('LicenseNo')

	def set_LicenseNo(self, LicenseNo):  # String
		self.add_query_param('LicenseNo', LicenseNo)
	def get_BizType(self): # String
		return self.get_query_params().get('BizType')

	def set_BizType(self, BizType):  # String
		self.add_query_param('BizType', BizType)
	def get_LicensePublisher(self): # String
		return self.get_query_params().get('LicensePublisher')

	def set_LicensePublisher(self, LicensePublisher):  # String
		self.add_query_param('LicensePublisher', LicensePublisher)
	def get_BizId(self): # String
		return self.get_query_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_query_param('BizId', BizId)
	def get_LicenseCode(self): # String
		return self.get_query_params().get('LicenseCode')

	def set_LicenseCode(self, LicenseCode):  # String
		self.add_query_param('LicenseCode', LicenseCode)
