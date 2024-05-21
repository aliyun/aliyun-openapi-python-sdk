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
class SetWelcomePageURIRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ITaaS', '2017-05-05', 'SetWelcomePageURI','itaas')

	def get_Clientappid(self):
		return self.get_query_params().get('Clientappid')

	def set_Clientappid(self,Clientappid):
		self.add_query_param('Clientappid',Clientappid)

	def get_Sysfrom(self):
		return self.get_query_params().get('Sysfrom')

	def set_Sysfrom(self,Sysfrom):
		self.add_query_param('Sysfrom',Sysfrom)

	def get_Operator(self):
		return self.get_query_params().get('Operator')

	def set_Operator(self,Operator):
		self.add_query_param('Operator',Operator)

	def get_Welcomeuri(self):
		return self.get_query_params().get('Welcomeuri')

	def set_Welcomeuri(self,Welcomeuri):
		self.add_query_param('Welcomeuri',Welcomeuri)