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

class DeleteUnbeianIpCheckTypeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Beian', '2016-08-10', 'DeleteUnbeianIpCheckType')
		self.set_method('POST')

	def get_Ip(self): # String
		return self.get_query_params().get('Ip')

	def set_Ip(self, Ip):  # String
		self.add_query_param('Ip', Ip)
	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_CheckType(self): # Integer
		return self.get_query_params().get('CheckType')

	def set_CheckType(self, CheckType):  # Integer
		self.add_query_param('CheckType', CheckType)
	def get_Caller(self): # String
		return self.get_query_params().get('Caller')

	def set_Caller(self, Caller):  # String
		self.add_query_param('Caller', Caller)
