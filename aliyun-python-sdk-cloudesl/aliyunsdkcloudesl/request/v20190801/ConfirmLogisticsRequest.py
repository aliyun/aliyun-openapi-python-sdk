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
from aliyunsdkcloudesl.endpoint import endpoint_data

class ConfirmLogisticsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2019-08-01', 'ConfirmLogistics','cloudesl')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PrNumber(self):
		return self.get_body_params().get('PrNumber')

	def set_PrNumber(self,PrNumber):
		self.add_body_params('PrNumber', PrNumber)

	def get_LogisticsDocuments(self):
		return self.get_body_params().get('LogisticsDocuments')

	def set_LogisticsDocuments(self,LogisticsDocuments):
		self.add_body_params('LogisticsDocuments', LogisticsDocuments)

	def get_PoNumber(self):
		return self.get_body_params().get('PoNumber')

	def set_PoNumber(self,PoNumber):
		self.add_body_params('PoNumber', PoNumber)

	def get_Status(self):
		return self.get_body_params().get('Status')

	def set_Status(self,Status):
		self.add_body_params('Status', Status)