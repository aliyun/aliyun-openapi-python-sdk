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
from aliyunsdkviapi_regen.endpoint import endpoint_data

class CreateTrainTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'viapi-regen', '2021-11-19', 'CreateTrainTask','selflearning')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_TrainMode(self): # String
		return self.get_body_params().get('TrainMode')

	def set_TrainMode(self, TrainMode):  # String
		self.add_body_params('TrainMode', TrainMode)
	def get_DatasetIds(self): # String
		return self.get_body_params().get('DatasetIds')

	def set_DatasetIds(self, DatasetIds):  # String
		self.add_body_params('DatasetIds', DatasetIds)
	def get_PreTrainTaskId(self): # Long
		return self.get_body_params().get('PreTrainTaskId')

	def set_PreTrainTaskId(self, PreTrainTaskId):  # Long
		self.add_body_params('PreTrainTaskId', PreTrainTaskId)
	def get_AdvancedParameters(self): # String
		return self.get_body_params().get('AdvancedParameters')

	def set_AdvancedParameters(self, AdvancedParameters):  # String
		self.add_body_params('AdvancedParameters', AdvancedParameters)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_LabelIds(self): # String
		return self.get_body_params().get('LabelIds')

	def set_LabelIds(self, LabelIds):  # String
		self.add_body_params('LabelIds', LabelIds)
	def get_WorkspaceId(self): # Long
		return self.get_body_params().get('WorkspaceId')

	def set_WorkspaceId(self, WorkspaceId):  # Long
		self.add_body_params('WorkspaceId', WorkspaceId)
