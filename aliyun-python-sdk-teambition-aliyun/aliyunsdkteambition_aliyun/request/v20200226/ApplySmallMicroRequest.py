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

class ApplySmallMicroRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'teambition-aliyun', '2020-02-26', 'ApplySmallMicro')
		self.set_method('POST')

	def get_ApplicantEmail(self):
		return self.get_body_params().get('ApplicantEmail')

	def set_ApplicantEmail(self,ApplicantEmail):
		self.add_body_params('ApplicantEmail', ApplicantEmail)

	def get_DevelopScale(self):
		return self.get_query_params().get('DevelopScale')

	def set_DevelopScale(self,DevelopScale):
		self.add_query_param('DevelopScale',DevelopScale)

	def get_Type(self):
		return self.get_body_params().get('Type')

	def set_Type(self,Type):
		self.add_body_params('Type', Type)

	def get_OrgId(self):
		return self.get_body_params().get('OrgId')

	def set_OrgId(self,OrgId):
		self.add_body_params('OrgId', OrgId)

	def get_ApplicantPosition(self):
		return self.get_body_params().get('ApplicantPosition')

	def set_ApplicantPosition(self,ApplicantPosition):
		self.add_body_params('ApplicantPosition', ApplicantPosition)

	def get_DevelopLanguage(self):
		return self.get_body_params().get('DevelopLanguage')

	def set_DevelopLanguage(self,DevelopLanguage):
		self.add_body_params('DevelopLanguage', DevelopLanguage)

	def get_OrgName(self):
		return self.get_body_params().get('OrgName')

	def set_OrgName(self,OrgName):
		self.add_body_params('OrgName', OrgName)

	def get_ApplicantTel(self):
		return self.get_body_params().get('ApplicantTel')

	def set_ApplicantTel(self,ApplicantTel):
		self.add_body_params('ApplicantTel', ApplicantTel)

	def get_Solution(self):
		return self.get_body_params().get('Solution')

	def set_Solution(self,Solution):
		self.add_body_params('Solution', Solution)

	def get_ForHelp(self):
		return self.get_body_params().get('ForHelp')

	def set_ForHelp(self,ForHelp):
		self.add_body_params('ForHelp', ForHelp)

	def get_ApplicantName(self):
		return self.get_body_params().get('ApplicantName')

	def set_ApplicantName(self,ApplicantName):
		self.add_body_params('ApplicantName', ApplicantName)

	def get_BusinessModel(self):
		return self.get_body_params().get('BusinessModel')

	def set_BusinessModel(self,BusinessModel):
		self.add_body_params('BusinessModel', BusinessModel)