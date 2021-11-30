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
from aliyunsdkalb.endpoint import endpoint_data

class ListListenersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'ListListeners','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_LoadBalancerIds(self): # Array
		return self.get_query_params().get('LoadBalancerIds')

	def set_LoadBalancerIds(self, LoadBalancerIds):  # Array
		for index1, value1 in enumerate(LoadBalancerIds):
			self.add_query_param('LoadBalancerIds.' + str(index1 + 1), value1)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_ListenerProtocol(self): # String
		return self.get_query_params().get('ListenerProtocol')

	def set_ListenerProtocol(self, ListenerProtocol):  # String
		self.add_query_param('ListenerProtocol', ListenerProtocol)
	def get_ListenerIds(self): # Array
		return self.get_query_params().get('ListenerIds')

	def set_ListenerIds(self, ListenerIds):  # Array
		for index1, value1 in enumerate(ListenerIds):
			self.add_query_param('ListenerIds.' + str(index1 + 1), value1)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
