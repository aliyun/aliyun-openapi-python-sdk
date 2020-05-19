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
from aliyunsdkaliyuncvc.endpoint import endpoint_data

class CreateEvaluationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aliyuncvc', '2019-10-30', 'CreateEvaluation','aliyuncvc')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CreateTime(self):
		return self.get_query_params().get('CreateTime')

	def set_CreateTime(self,CreateTime):
		self.add_query_param('CreateTime',CreateTime)

	def get_Memo(self):
		return self.get_query_params().get('Memo')

	def set_Memo(self,Memo):
		self.add_query_param('Memo',Memo)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_MemberUUID(self):
		return self.get_query_params().get('MemberUUID')

	def set_MemberUUID(self,MemberUUID):
		self.add_query_param('MemberUUID',MemberUUID)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_Evaluation(self):
		return self.get_query_params().get('Evaluation')

	def set_Evaluation(self,Evaluation):
		self.add_query_param('Evaluation',Evaluation)

	def get_Score(self):
		return self.get_query_params().get('Score')

	def set_Score(self,Score):
		self.add_query_param('Score',Score)

	def get_MeetingUUID(self):
		return self.get_query_params().get('MeetingUUID')

	def set_MeetingUUID(self,MeetingUUID):
		self.add_query_param('MeetingUUID',MeetingUUID)