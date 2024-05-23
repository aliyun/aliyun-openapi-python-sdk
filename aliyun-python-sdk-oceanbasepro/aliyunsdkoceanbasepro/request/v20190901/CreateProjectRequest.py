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

class CreateProjectRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'CreateProject','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SinkEndpointId(self): # String
		return self.get_body_params().get('SinkEndpointId')

	def set_SinkEndpointId(self, SinkEndpointId):  # String
		self.add_body_params('SinkEndpointId', SinkEndpointId)
	def get_UseOss(self): # Boolean
		return self.get_body_params().get('UseOss')

	def set_UseOss(self, UseOss):  # Boolean
		self.add_body_params('UseOss', UseOss)
	def get_OssKey(self): # String
		return self.get_body_params().get('OssKey')

	def set_OssKey(self, OssKey):  # String
		self.add_body_params('OssKey', OssKey)
	def get_SourceEndpointId(self): # String
		return self.get_body_params().get('SourceEndpointId')

	def set_SourceEndpointId(self, SourceEndpointId):  # String
		self.add_body_params('SourceEndpointId', SourceEndpointId)
	def get_Type(self): # String
		return self.get_body_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_body_params('Type', Type)
	def get_FullTransferConfig(self): # Struct
		return self.get_body_params().get('FullTransferConfig')

	def set_FullTransferConfig(self, FullTransferConfig):  # Struct
		self.add_body_params("FullTransferConfig", json.dumps(FullTransferConfig))
	def get_EnableStructTransfer(self): # Boolean
		return self.get_body_params().get('EnableStructTransfer')

	def set_EnableStructTransfer(self, EnableStructTransfer):  # Boolean
		self.add_body_params('EnableStructTransfer', EnableStructTransfer)
	def get_TransferMapping(self): # Struct
		return self.get_body_params().get('TransferMapping')

	def set_TransferMapping(self, TransferMapping):  # Struct
		self.add_body_params("TransferMapping", json.dumps(TransferMapping))
	def get_WorkerGradeId(self): # String
		return self.get_body_params().get('WorkerGradeId')

	def set_WorkerGradeId(self, WorkerGradeId):  # String
		self.add_body_params('WorkerGradeId', WorkerGradeId)
	def get_Id(self): # String
		return self.get_body_params().get('Id')

	def set_Id(self, Id):  # String
		self.add_body_params('Id', Id)
	def get_CommonTransferConfig(self): # Struct
		return self.get_body_params().get('CommonTransferConfig')

	def set_CommonTransferConfig(self, CommonTransferConfig):  # Struct
		self.add_body_params("CommonTransferConfig", json.dumps(CommonTransferConfig))
	def get_StructTransferConfig(self): # Struct
		return self.get_body_params().get('StructTransferConfig')

	def set_StructTransferConfig(self, StructTransferConfig):  # Struct
		self.add_body_params("StructTransferConfig", json.dumps(StructTransferConfig))
	def get_ReverseIncrTransferConfig(self): # Struct
		return self.get_body_params().get('ReverseIncrTransferConfig')

	def set_ReverseIncrTransferConfig(self, ReverseIncrTransferConfig):  # Struct
		self.add_body_params("ReverseIncrTransferConfig", json.dumps(ReverseIncrTransferConfig))
	def get_EnableIncrTransfer(self): # Boolean
		return self.get_body_params().get('EnableIncrTransfer')

	def set_EnableIncrTransfer(self, EnableIncrTransfer):  # Boolean
		self.add_body_params('EnableIncrTransfer', EnableIncrTransfer)
	def get_EnableFullTransfer(self): # Boolean
		return self.get_body_params().get('EnableFullTransfer')

	def set_EnableFullTransfer(self, EnableFullTransfer):  # Boolean
		self.add_body_params('EnableFullTransfer', EnableFullTransfer)
	def get_EnableFullVerify(self): # Boolean
		return self.get_body_params().get('EnableFullVerify')

	def set_EnableFullVerify(self, EnableFullVerify):  # Boolean
		self.add_body_params('EnableFullVerify', EnableFullVerify)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_LabelIds(self): # Array
		return self.get_body_params().get('LabelIds')

	def set_LabelIds(self, LabelIds):  # Array
		self.add_body_params("LabelIds", json.dumps(LabelIds))
	def get_IncrTransferConfig(self): # Struct
		return self.get_body_params().get('IncrTransferConfig')

	def set_IncrTransferConfig(self, IncrTransferConfig):  # Struct
		self.add_body_params("IncrTransferConfig", json.dumps(IncrTransferConfig))
	def get_EnableReverseIncrTransfer(self): # Boolean
		return self.get_body_params().get('EnableReverseIncrTransfer')

	def set_EnableReverseIncrTransfer(self, EnableReverseIncrTransfer):  # Boolean
		self.add_body_params('EnableReverseIncrTransfer', EnableReverseIncrTransfer)
