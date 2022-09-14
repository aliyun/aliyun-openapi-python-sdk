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
from aliyunsdkehpc.endpoint import endpoint_data

class AddNodesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2017-07-14', 'AddNodes')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_Count(self): # Integer
		return self.get_query_params().get('Count')

	def set_Count(self, Count):  # Integer
		self.add_query_param('Count', Count)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_ComputeSpotStrategy(self): # String
		return self.get_query_params().get('ComputeSpotStrategy')

	def set_ComputeSpotStrategy(self, ComputeSpotStrategy):  # String
		self.add_query_param('ComputeSpotStrategy', ComputeSpotStrategy)
	def get_ImageOwnerAlias(self): # String
		return self.get_query_params().get('ImageOwnerAlias')

	def set_ImageOwnerAlias(self, ImageOwnerAlias):  # String
		self.add_query_param('ImageOwnerAlias', ImageOwnerAlias)
	def get_ComputeSpotPriceLimit(self): # String
		return self.get_query_params().get('ComputeSpotPriceLimit')

	def set_ComputeSpotPriceLimit(self, ComputeSpotPriceLimit):  # String
		self.add_query_param('ComputeSpotPriceLimit', ComputeSpotPriceLimit)
