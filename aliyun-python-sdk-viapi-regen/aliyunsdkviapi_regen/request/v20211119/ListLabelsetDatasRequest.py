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

class ListLabelsetDatasRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'viapi-regen', '2021-11-19', 'ListLabelsetDatas','selflearning')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PageSize(self): # Long
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_body_params('PageSize', PageSize)
	def get_Value(self): # String
		return self.get_body_params().get('Value')

	def set_Value(self, Value):  # String
		self.add_body_params('Value', Value)
	def get_CurrentPage(self): # Long
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Long
		self.add_body_params('CurrentPage', CurrentPage)
	def get_IsAbandon(self): # Boolean
		return self.get_body_params().get('IsAbandon')

	def set_IsAbandon(self, IsAbandon):  # Boolean
		self.add_body_params('IsAbandon', IsAbandon)
	def get_LabelId(self): # Long
		return self.get_body_params().get('LabelId')

	def set_LabelId(self, LabelId):  # Long
		self.add_body_params('LabelId', LabelId)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_Operation(self): # String
		return self.get_body_params().get('Operation')

	def set_Operation(self, Operation):  # String
		self.add_body_params('Operation', Operation)
