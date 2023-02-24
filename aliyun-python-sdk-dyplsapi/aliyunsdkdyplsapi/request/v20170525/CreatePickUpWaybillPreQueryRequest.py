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
from aliyunsdkdyplsapi.endpoint import endpoint_data
import json

class CreatePickUpWaybillPreQueryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyplsapi', '2017-05-25', 'CreatePickUpWaybillPreQuery')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PreWeight(self): # String
		return self.get_query_params().get('PreWeight')

	def set_PreWeight(self, PreWeight):  # String
		self.add_query_param('PreWeight', PreWeight)
	def get_OrderChannels(self): # String
		return self.get_query_params().get('OrderChannels')

	def set_OrderChannels(self, OrderChannels):  # String
		self.add_query_param('OrderChannels', OrderChannels)
	def get_OuterOrderCode(self): # String
		return self.get_query_params().get('OuterOrderCode')

	def set_OuterOrderCode(self, OuterOrderCode):  # String
		self.add_query_param('OuterOrderCode', OuterOrderCode)
	def get_ConsigneeInfo(self): # Struct
		return self.get_query_params().get('ConsigneeInfo')

	def set_ConsigneeInfo(self, ConsigneeInfo):  # Struct
		self.add_query_param("ConsigneeInfo", json.dumps(ConsigneeInfo))
	def get_CpCode(self): # String
		return self.get_query_params().get('CpCode')

	def set_CpCode(self, CpCode):  # String
		self.add_query_param('CpCode', CpCode)
	def get_ContentType(self): # String
		return self.get_headers().get('Content-Type')

	def set_ContentType(self, ContentType):  # String
		self.add_header('Content-Type', ContentType)
	def get_SenderInfo(self): # Struct
		return self.get_query_params().get('SenderInfo')

	def set_SenderInfo(self, SenderInfo):  # Struct
		self.add_query_param("SenderInfo", json.dumps(SenderInfo))
