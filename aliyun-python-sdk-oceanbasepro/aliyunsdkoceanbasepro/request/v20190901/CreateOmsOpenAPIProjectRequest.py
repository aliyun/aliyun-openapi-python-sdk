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
from aliyunsdkoceanbasepro.endpoint import endpoint_data
import json

class CreateOmsOpenAPIProjectRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'CreateOmsOpenAPIProject','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DestConfig(self): # Struct
		return self.get_body_params().get('DestConfig')

	def set_DestConfig(self, DestConfig):  # Struct
		self.add_body_params("DestConfig", json.dumps(DestConfig))
	def get_PageNumber(self): # Integer
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_body_params('PageNumber', PageNumber)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_TransferMapping(self): # Struct
		return self.get_body_params().get('TransferMapping')

	def set_TransferMapping(self, TransferMapping):  # Struct
		self.add_body_params("TransferMapping", json.dumps(TransferMapping))
	def get_TransferStepConfig(self): # Struct
		return self.get_body_params().get('TransferStepConfig')

	def set_TransferStepConfig(self, TransferStepConfig):  # Struct
		self.add_body_params("TransferStepConfig", json.dumps(TransferStepConfig))
	def get_WorkerGradeId(self): # String
		return self.get_body_params().get('WorkerGradeId')

	def set_WorkerGradeId(self, WorkerGradeId):  # String
		self.add_body_params('WorkerGradeId', WorkerGradeId)
	def get_ProjectName(self): # String
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_body_params('ProjectName', ProjectName)
	def get_SourceConfig(self): # Struct
		return self.get_body_params().get('SourceConfig')

	def set_SourceConfig(self, SourceConfig):  # Struct
		self.add_body_params("SourceConfig", json.dumps(SourceConfig))
	def get_BusinessName(self): # String
		return self.get_body_params().get('BusinessName')

	def set_BusinessName(self, BusinessName):  # String
		self.add_body_params('BusinessName', BusinessName)
	def get_LabelIds(self): # Array
		return self.get_body_params().get('LabelIds')

	def set_LabelIds(self, LabelIds):  # Array
		self.add_body_params("LabelIds", json.dumps(LabelIds))
