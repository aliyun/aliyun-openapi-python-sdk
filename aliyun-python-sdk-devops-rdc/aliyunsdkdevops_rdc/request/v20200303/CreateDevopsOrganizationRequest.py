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

class CreateDevopsOrganizationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'devops-rdc', '2020-03-03', 'CreateDevopsOrganization')
		self.set_method('POST')

	def get_OrgName(self):
		return self.get_body_params().get('OrgName')

	def set_OrgName(self,OrgName):
		self.add_body_params('OrgName', OrgName)

	def get_Source(self):
		return self.get_body_params().get('Source')

	def set_Source(self,Source):
		self.add_body_params('Source', Source)

	def get_RealPk(self):
		return self.get_body_params().get('RealPk')

	def set_RealPk(self,RealPk):
		self.add_body_params('RealPk', RealPk)

	def get_DesiredMemberCount(self):
		return self.get_body_params().get('DesiredMemberCount')

	def set_DesiredMemberCount(self,DesiredMemberCount):
		self.add_body_params('DesiredMemberCount', DesiredMemberCount)