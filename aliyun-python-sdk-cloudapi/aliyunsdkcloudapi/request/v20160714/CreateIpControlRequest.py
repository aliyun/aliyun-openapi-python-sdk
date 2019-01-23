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
class CreateIpControlRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'CreateIpControl','apigateway')

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_IpControlName(self):
		return self.get_query_params().get('IpControlName')

	def set_IpControlName(self,IpControlName):
		self.add_query_param('IpControlName',IpControlName)

	def get_IpControlType(self):
		return self.get_query_params().get('IpControlType')

	def set_IpControlType(self,IpControlType):
		self.add_query_param('IpControlType',IpControlType)

	def get_IpControlPolicyss(self):
		return self.get_query_params().get('IpControlPolicyss')

	def set_IpControlPolicyss(self,IpControlPolicyss):
		for i in range(len(IpControlPolicyss)):	
			if IpControlPolicyss[i].get('AppId') is not None:
				self.add_query_param('IpControlPolicys.' + str(i + 1) + '.AppId' , IpControlPolicyss[i].get('AppId'))
			if IpControlPolicyss[i].get('CidrIp') is not None:
				self.add_query_param('IpControlPolicys.' + str(i + 1) + '.CidrIp' , IpControlPolicyss[i].get('CidrIp'))


	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)