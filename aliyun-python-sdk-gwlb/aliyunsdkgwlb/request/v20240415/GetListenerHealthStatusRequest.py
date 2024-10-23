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
from aliyunsdkgwlb.endpoint import endpoint_data

class GetListenerHealthStatusRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Gwlb', '2024-04-15', 'GetListenerHealthStatus','gwlb')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Skip(self): # Integer
		return self.get_body_params().get('Skip')

	def set_Skip(self, Skip):  # Integer
		self.add_body_params('Skip', Skip)
	def get_ListenerId(self): # String
		return self.get_body_params().get('ListenerId')

	def set_ListenerId(self, ListenerId):  # String
		self.add_body_params('ListenerId', ListenerId)
	def get_NextToken(self): # String
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_body_params('NextToken', NextToken)
	def get_Filter(self): # Array
		return self.get_body_params().get('Filter')

	def set_Filter(self, Filter):  # Array
		for index1, value1 in enumerate(Filter):
			if value1.get('Name') is not None:
				self.add_body_params('Filter.' + str(index1 + 1) + '.Name', value1.get('Name'))
			if value1.get('Values') is not None:
				for index2, value2 in enumerate(value1.get('Values')):
					self.add_body_params('Filter.' + str(index1 + 1) + '.Values.' + str(index2 + 1), value2)
	def get_MaxResults(self): # Integer
		return self.get_body_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_body_params('MaxResults', MaxResults)
