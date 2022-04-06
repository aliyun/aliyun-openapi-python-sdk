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
from aliyunsdkimageprocess.endpoint import endpoint_data

class RunMedQARequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imageprocess', '2020-03-20', 'RunMedQA','imageprocess')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SessionId(self): # String
		return self.get_body_params().get('SessionId')

	def set_SessionId(self, SessionId):  # String
		self.add_body_params('SessionId', SessionId)
	def get_OrgName(self): # String
		return self.get_body_params().get('OrgName')

	def set_OrgName(self, OrgName):  # String
		self.add_body_params('OrgName', OrgName)
	def get_AnswerImageDataLists(self): # RepeatList
		return self.get_body_params().get('AnswerImageDataList')

	def set_AnswerImageDataLists(self, AnswerImageDataList):  # RepeatList
		for depth1 in range(len(AnswerImageDataList)):
			if AnswerImageDataList[depth1].get('AnswerImageData') is not None:
				self.add_body_params('AnswerImageDataList.' + str(depth1 + 1) + '.AnswerImageData', AnswerImageDataList[depth1].get('AnswerImageData'))
	def get_AnswerTextLists(self): # RepeatList
		return self.get_body_params().get('AnswerTextList')

	def set_AnswerTextLists(self, AnswerTextList):  # RepeatList
		for depth1 in range(len(AnswerTextList)):
			if AnswerTextList[depth1].get('AnswerText') is not None:
				self.add_body_params('AnswerTextList.' + str(depth1 + 1) + '.AnswerText', AnswerTextList[depth1].get('AnswerText'))
	def get_Department(self): # String
		return self.get_body_params().get('Department')

	def set_Department(self, Department):  # String
		self.add_body_params('Department', Department)
	def get_AnswerImageURLLists(self): # RepeatList
		return self.get_body_params().get('AnswerImageURLList')

	def set_AnswerImageURLLists(self, AnswerImageURLList):  # RepeatList
		for depth1 in range(len(AnswerImageURLList)):
			if AnswerImageURLList[depth1].get('AnswerImageURL') is not None:
				self.add_body_params('AnswerImageURLList.' + str(depth1 + 1) + '.AnswerImageURL', AnswerImageURLList[depth1].get('AnswerImageURL'))
	def get_QuestionType(self): # String
		return self.get_body_params().get('QuestionType')

	def set_QuestionType(self, QuestionType):  # String
		self.add_body_params('QuestionType', QuestionType)
	def get_OrgId(self): # String
		return self.get_body_params().get('OrgId')

	def set_OrgId(self, OrgId):  # String
		self.add_body_params('OrgId', OrgId)
