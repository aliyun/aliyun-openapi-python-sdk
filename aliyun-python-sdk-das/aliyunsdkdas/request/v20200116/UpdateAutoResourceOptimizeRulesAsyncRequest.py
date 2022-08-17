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
from aliyunsdkdas.endpoint import endpoint_data

class UpdateAutoResourceOptimizeRulesAsyncRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'UpdateAutoResourceOptimizeRulesAsync')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResultId(self): # String
		return self.get_query_params().get('ResultId')

	def set_ResultId(self, ResultId):  # String
		self.add_query_param('ResultId', ResultId)
	def get_ConsoleContext(self): # String
		return self.get_query_params().get('ConsoleContext')

	def set_ConsoleContext(self, ConsoleContext):  # String
		self.add_query_param('ConsoleContext', ConsoleContext)
	def get_InstanceIds(self): # String
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self, InstanceIds):  # String
		self.add_query_param('InstanceIds', InstanceIds)
	def get_TableSpaceSize(self): # Double
		return self.get_query_params().get('TableSpaceSize')

	def set_TableSpaceSize(self, TableSpaceSize):  # Double
		self.add_query_param('TableSpaceSize', TableSpaceSize)
	def get_TableFragmentationRatio(self): # Double
		return self.get_query_params().get('TableFragmentationRatio')

	def set_TableFragmentationRatio(self, TableFragmentationRatio):  # Double
		self.add_query_param('TableFragmentationRatio', TableFragmentationRatio)
