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

class RollbackApplicationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'RollbackApplication','ens')
		self.set_method('POST')

	def get_Timeout(self): # Integer
		return self.get_query_params().get('Timeout')

	def set_Timeout(self, Timeout):  # Integer
		self.add_query_param('Timeout', Timeout)
	def get_FromAppVersion(self): # String
		return self.get_query_params().get('FromAppVersion')

	def set_FromAppVersion(self, FromAppVersion):  # String
		self.add_query_param('FromAppVersion', FromAppVersion)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_ToAppVersion(self): # String
		return self.get_query_params().get('ToAppVersion')

	def set_ToAppVersion(self, ToAppVersion):  # String
		self.add_query_param('ToAppVersion', ToAppVersion)
