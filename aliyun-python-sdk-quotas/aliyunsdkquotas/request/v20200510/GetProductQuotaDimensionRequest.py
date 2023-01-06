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
from aliyunsdkquotas.endpoint import endpoint_data

class GetProductQuotaDimensionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quotas', '2020-05-10', 'GetProductQuotaDimension','quotas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProductCode(self): # String
		return self.get_body_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_body_params('ProductCode', ProductCode)
	def get_DependentDimensionss(self): # RepeatList
		return self.get_body_params().get('DependentDimensions')

	def set_DependentDimensionss(self, DependentDimensions):  # RepeatList
		for depth1 in range(len(DependentDimensions)):
			if DependentDimensions[depth1].get('Key') is not None:
				self.add_body_params('DependentDimensions.' + str(depth1 + 1) + '.Key', DependentDimensions[depth1].get('Key'))
			if DependentDimensions[depth1].get('Value') is not None:
				self.add_body_params('DependentDimensions.' + str(depth1 + 1) + '.Value', DependentDimensions[depth1].get('Value'))
	def get_DimensionKey(self): # String
		return self.get_body_params().get('DimensionKey')

	def set_DimensionKey(self, DimensionKey):  # String
		self.add_body_params('DimensionKey', DimensionKey)
