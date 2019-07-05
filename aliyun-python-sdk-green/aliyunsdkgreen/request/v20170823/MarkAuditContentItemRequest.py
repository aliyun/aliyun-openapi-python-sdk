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
class MarkAuditContentItemRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2017-08-23', 'MarkAuditContentItem','green')

	def get_AuditIllegalReasons(self):
		return self.get_query_params().get('AuditIllegalReasons')

	def set_AuditIllegalReasons(self,AuditIllegalReasons):
		self.add_query_param('AuditIllegalReasons',AuditIllegalReasons)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_AuditResult(self):
		return self.get_query_params().get('AuditResult')

	def set_AuditResult(self,AuditResult):
		self.add_query_param('AuditResult',AuditResult)

	def get_Ids(self):
		return self.get_query_params().get('Ids')

	def set_Ids(self,Ids):
		self.add_query_param('Ids',Ids)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)