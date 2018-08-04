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
class CreateJobExecutionPlanParamRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'CreateJobExecutionPlanParam')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_RelateId(self):
		return self.get_query_params().get('RelateId')

	def set_RelateId(self,RelateId):
		self.add_query_param('RelateId',RelateId)

	def get_WorkParamPairs(self):
		return self.get_query_params().get('WorkParamPairs')

	def set_WorkParamPairs(self,WorkParamPairs):
		for i in range(len(WorkParamPairs)):	
			if WorkParamPairs[i].get('Name') is not None:
				self.add_query_param('WorkParamPair.' + str(i + 1) + '.Name' , WorkParamPairs[i].get('Name'))
			if WorkParamPairs[i].get('Value') is not None:
				self.add_query_param('WorkParamPair.' + str(i + 1) + '.Value' , WorkParamPairs[i].get('Value'))


	def get_ParamBizType(self):
		return self.get_query_params().get('ParamBizType')

	def set_ParamBizType(self,ParamBizType):
		self.add_query_param('ParamBizType',ParamBizType)