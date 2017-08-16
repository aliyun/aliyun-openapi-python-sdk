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
class QueryContactTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2016-05-11', 'QueryContactTemplate')

	def get_CCompany(self):
		return self.get_query_params().get('CCompany')

	def set_CCompany(self,CCompany):
		self.add_query_param('CCompany',CCompany)

	def get_AuditStatus(self):
		return self.get_query_params().get('AuditStatus')

	def set_AuditStatus(self,AuditStatus):
		self.add_query_param('AuditStatus',AuditStatus)

	def get_DefaultTemplate(self):
		return self.get_query_params().get('DefaultTemplate')

	def set_DefaultTemplate(self,DefaultTemplate):
		self.add_query_param('DefaultTemplate',DefaultTemplate)

	def get_ECompany(self):
		return self.get_query_params().get('ECompany')

	def set_ECompany(self,ECompany):
		self.add_query_param('ECompany',ECompany)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_ContactTemplateId(self):
		return self.get_query_params().get('ContactTemplateId')

	def set_ContactTemplateId(self,ContactTemplateId):
		self.add_query_param('ContactTemplateId',ContactTemplateId)

	def get_RegType(self):
		return self.get_query_params().get('RegType')

	def set_RegType(self,RegType):
		self.add_query_param('RegType',RegType)