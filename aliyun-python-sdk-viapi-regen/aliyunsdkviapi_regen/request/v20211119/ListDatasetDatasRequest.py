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

class ListDatasetDatasRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'viapi-regen', '2021-11-19', 'ListDatasetDatas','selflearning')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Identity(self): # String
		return self.get_body_params().get('Identity')

	def set_Identity(self, Identity):  # String
		self.add_body_params('Identity', Identity)
	def get_PageSize(self): # Long
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_body_params('PageSize', PageSize)
	def get_CurrentPage(self): # Long
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Long
		self.add_body_params('CurrentPage', CurrentPage)
	def get_DatasetId(self): # Long
		return self.get_body_params().get('DatasetId')

	def set_DatasetId(self, DatasetId):  # Long
		self.add_body_params('DatasetId', DatasetId)
