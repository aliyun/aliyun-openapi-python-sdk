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
class CreateLoginProfileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ram', '2015-05-01', 'CreateLoginProfile')
		self.set_protocol_type('https');

	def get_UserName(self):
		return self.get_query_params().get('UserName')

	def set_UserName(self,UserName):
		self.add_query_param('UserName',UserName)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_PasswordResetRequired(self):
		return self.get_query_params().get('PasswordResetRequired')

	def set_PasswordResetRequired(self,PasswordResetRequired):
		self.add_query_param('PasswordResetRequired',PasswordResetRequired)

	def get_MFABindRequired(self):
		return self.get_query_params().get('MFABindRequired')

	def set_MFABindRequired(self,MFABindRequired):
		self.add_query_param('MFABindRequired',MFABindRequired)