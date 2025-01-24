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

class CreateConversationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'AIMath', '2024-11-14', 'CreateConversation')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_OuterBizId(self): # String
		return self.get_body_params().get('OuterBizId')

	def set_OuterBizId(self, OuterBizId):  # String
		self.add_body_params('OuterBizId', OuterBizId)
	def get_UserId(self): # String
		return self.get_body_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_body_params('UserId', UserId)
	def get_ExerciseAnswer(self): # String
		return self.get_body_params().get('ExerciseAnswer')

	def set_ExerciseAnswer(self, ExerciseAnswer):  # String
		self.add_body_params('ExerciseAnswer', ExerciseAnswer)
	def get_ExerciseType(self): # String
		return self.get_body_params().get('ExerciseType')

	def set_ExerciseType(self, ExerciseType):  # String
		self.add_body_params('ExerciseType', ExerciseType)
	def get_ExerciseContent(self): # String
		return self.get_body_params().get('ExerciseContent')

	def set_ExerciseContent(self, ExerciseContent):  # String
		self.add_body_params('ExerciseContent', ExerciseContent)
	def get_ExerciseAnalysis(self): # String
		return self.get_body_params().get('ExerciseAnalysis')

	def set_ExerciseAnalysis(self, ExerciseAnalysis):  # String
		self.add_body_params('ExerciseAnalysis', ExerciseAnalysis)
