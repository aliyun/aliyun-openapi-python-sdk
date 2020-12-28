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
from aliyunsdknlp_automl.endpoint import endpoint_data

class CreateModelRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'nlp-automl', '2019-11-11', 'CreateModel','nlpautoml')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IsIncrementalTrain(self):
		return self.get_body_params().get('IsIncrementalTrain')

	def set_IsIncrementalTrain(self,IsIncrementalTrain):
		self.add_body_params('IsIncrementalTrain', IsIncrementalTrain)

	def get_ModelName(self):
		return self.get_body_params().get('ModelName')

	def set_ModelName(self,ModelName):
		self.add_body_params('ModelName', ModelName)

	def get_DatasetIdList(self):
		return self.get_body_params().get('DatasetIdList')

	def set_DatasetIdList(self,DatasetIdList):
		self.add_body_params('DatasetIdList', DatasetIdList)

	def get_TestDatasetIdList(self):
		return self.get_body_params().get('TestDatasetIdList')

	def set_TestDatasetIdList(self,TestDatasetIdList):
		self.add_body_params('TestDatasetIdList', TestDatasetIdList)

	def get_ModelType(self):
		return self.get_body_params().get('ModelType')

	def set_ModelType(self,ModelType):
		self.add_body_params('ModelType', ModelType)

	def get_ProjectId(self):
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_body_params('ProjectId', ProjectId)

	def get_ModelId(self):
		return self.get_body_params().get('ModelId')

	def set_ModelId(self,ModelId):
		self.add_body_params('ModelId', ModelId)