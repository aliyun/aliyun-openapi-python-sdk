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
from aliyunsdkmts.endpoint import endpoint_data

class CreateInferenceServerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'CreateInferenceServer','mts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PipelineId(self): # String
		return self.get_query_params().get('PipelineId')

	def set_PipelineId(self, PipelineId):  # String
		self.add_query_param('PipelineId', PipelineId)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_ModelType(self): # String
		return self.get_query_params().get('ModelType')

	def set_ModelType(self, ModelType):  # String
		self.add_query_param('ModelType', ModelType)
	def get_FunctionName(self): # String
		return self.get_query_params().get('FunctionName')

	def set_FunctionName(self, FunctionName):  # String
		self.add_query_param('FunctionName', FunctionName)
	def get_TestId(self): # String
		return self.get_query_params().get('TestId')

	def set_TestId(self, TestId):  # String
		self.add_query_param('TestId', TestId)
	def get_ModelPath(self): # String
		return self.get_query_params().get('ModelPath')

	def set_ModelPath(self, ModelPath):  # String
		self.add_query_param('ModelPath', ModelPath)
