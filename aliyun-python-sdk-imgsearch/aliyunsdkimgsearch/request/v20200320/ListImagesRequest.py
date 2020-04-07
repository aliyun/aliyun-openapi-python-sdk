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
from aliyunsdkimgsearch.endpoint import endpoint_data

class ListImagesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imgsearch', '2020-03-20', 'ListImages','imgsearch')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_EntityIdPrefix(self):
		return self.get_body_params().get('EntityIdPrefix')

	def set_EntityIdPrefix(self,EntityIdPrefix):
		self.add_body_params('EntityIdPrefix', EntityIdPrefix)

	def get_Limit(self):
		return self.get_body_params().get('Limit')

	def set_Limit(self,Limit):
		self.add_body_params('Limit', Limit)

	def get_Order(self):
		return self.get_body_params().get('Order')

	def set_Order(self,Order):
		self.add_body_params('Order', Order)

	def get_Offset(self):
		return self.get_body_params().get('Offset')

	def set_Offset(self,Offset):
		self.add_body_params('Offset', Offset)

	def get_Token(self):
		return self.get_body_params().get('Token')

	def set_Token(self,Token):
		self.add_body_params('Token', Token)

	def get_DbName(self):
		return self.get_body_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_body_params('DbName', DbName)