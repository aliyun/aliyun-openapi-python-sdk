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
class InsertRenewInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Trademark', '2018-07-24', 'InsertRenewInfo','trademark')

	def get_EngName(self):
		return self.get_query_params().get('EngName')

	def set_EngName(self,EngName):
		self.add_query_param('EngName',EngName)

	def get_Address(self):
		return self.get_query_params().get('Address')

	def set_Address(self,Address):
		self.add_query_param('Address',Address)

	def get_RegisterTime(self):
		return self.get_query_params().get('RegisterTime')

	def set_RegisterTime(self,RegisterTime):
		self.add_query_param('RegisterTime',RegisterTime)

	def get_EngAddress(self):
		return self.get_query_params().get('EngAddress')

	def set_EngAddress(self,EngAddress):
		self.add_query_param('EngAddress',EngAddress)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)