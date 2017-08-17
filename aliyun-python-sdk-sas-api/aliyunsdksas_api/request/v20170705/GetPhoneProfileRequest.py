# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class GetPhoneProfileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas-api', '2017-07-05', 'GetPhoneProfile')

	def get_Phone(self):
		return self.get_query_params().get('Phone')

	def set_Phone(self,Phone):
		self.add_query_param('Phone',Phone)

	def get_SensType(self):
		return self.get_query_params().get('SensType')

	def set_SensType(self,SensType):
		self.add_query_param('SensType',SensType)

	def get_DataVersion(self):
		return self.get_query_params().get('DataVersion')

	def set_DataVersion(self,DataVersion):
		self.add_query_param('DataVersion',DataVersion)

	def get_BusinessType(self):
		return self.get_query_params().get('BusinessType')

	def set_BusinessType(self,BusinessType):
		self.add_query_param('BusinessType',BusinessType)