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

class GetPipelineStepLogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'devops-rdc', '2020-03-03', 'GetPipelineStepLog')
		self.set_method('POST')

	def get_Offset(self):
		return self.get_body_params().get('Offset')

	def set_Offset(self,Offset):
		self.add_body_params('Offset', Offset)

	def get_UserPk(self):
		return self.get_body_params().get('UserPk')

	def set_UserPk(self,UserPk):
		self.add_body_params('UserPk', UserPk)

	def get_OrgId(self):
		return self.get_body_params().get('OrgId')

	def set_OrgId(self,OrgId):
		self.add_body_params('OrgId', OrgId)

	def get_PipelineId(self):
		return self.get_body_params().get('PipelineId')

	def set_PipelineId(self,PipelineId):
		self.add_body_params('PipelineId', PipelineId)

	def get_JobId(self):
		return self.get_body_params().get('JobId')

	def set_JobId(self,JobId):
		self.add_body_params('JobId', JobId)

	def get_StepIndex(self):
		return self.get_body_params().get('StepIndex')

	def set_StepIndex(self,StepIndex):
		self.add_body_params('StepIndex', StepIndex)

	def get_Limit(self):
		return self.get_body_params().get('Limit')

	def set_Limit(self,Limit):
		self.add_body_params('Limit', Limit)