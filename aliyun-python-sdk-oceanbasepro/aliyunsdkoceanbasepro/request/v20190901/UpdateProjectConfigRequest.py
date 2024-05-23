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

class UpdateProjectConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'UpdateProjectConfig','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ReverseIncrTransferConfig(self): # Struct
		return self.get_body_params().get('ReverseIncrTransferConfig')

	def set_ReverseIncrTransferConfig(self, ReverseIncrTransferConfig):  # Struct
		self.add_body_params("ReverseIncrTransferConfig", json.dumps(ReverseIncrTransferConfig))
	def get_FullTransferConfig(self): # Struct
		return self.get_body_params().get('FullTransferConfig')

	def set_FullTransferConfig(self, FullTransferConfig):  # Struct
		self.add_body_params("FullTransferConfig", json.dumps(FullTransferConfig))
	def get_Id(self): # String
		return self.get_body_params().get('Id')

	def set_Id(self, Id):  # String
		self.add_body_params('Id', Id)
	def get_IncrTransferConfig(self): # Struct
		return self.get_body_params().get('IncrTransferConfig')

	def set_IncrTransferConfig(self, IncrTransferConfig):  # Struct
		self.add_body_params("IncrTransferConfig", json.dumps(IncrTransferConfig))
