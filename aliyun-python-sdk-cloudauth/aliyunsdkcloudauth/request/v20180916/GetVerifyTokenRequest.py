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
class GetVerifyTokenRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2018-09-16', 'GetVerifyToken','cloudauth')
		self.set_protocol_type('https');

	def get_UserData(self):
		return self.get_query_params().get('UserData')

	def set_UserData(self,UserData):
		self.add_query_param('UserData',UserData)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Biz(self):
		return self.get_query_params().get('Biz')

	def set_Biz(self,Biz):
		self.add_query_param('Biz',Biz)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_Binding(self):
		return self.get_body_params().get('Binding')

	def set_Binding(self,Binding):
		self.add_body_params('Binding', Binding)

	def get_VerifyConfigs(self):
		return self.get_query_params().get('VerifyConfigs')

	def set_VerifyConfigs(self,VerifyConfigs):
		self.add_query_param('VerifyConfigs',VerifyConfigs)

	def get_TicketId(self):
		return self.get_query_params().get('TicketId')

	def set_TicketId(self,TicketId):
		self.add_query_param('TicketId',TicketId)