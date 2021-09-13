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
from aliyunsdklinkwan.endpoint import endpoint_data

class ListNodeTupleOrdersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2019-03-01', 'ListNodeTupleOrders','linkwan')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IsKpm(self):
		return self.get_query_params().get('IsKpm')

	def set_IsKpm(self,IsKpm):
		self.add_query_param('IsKpm',IsKpm)

	def get_Limit(self):
		return self.get_query_params().get('Limit')

	def set_Limit(self,Limit):
		self.add_query_param('Limit',Limit)

	def get_States(self):
		return self.get_query_params().get('State')

	def set_States(self, States):
		for depth1 in range(len(States)):
			if States[depth1] is not None:
				self.add_query_param('State.' + str(depth1 + 1) , States[depth1])

	def get_Offset(self):
		return self.get_query_params().get('Offset')

	def set_Offset(self,Offset):
		self.add_query_param('Offset',Offset)

	def get_Ascending(self):
		return self.get_query_params().get('Ascending')

	def set_Ascending(self,Ascending):
		self.add_query_param('Ascending',Ascending)

	def get_SortingField(self):
		return self.get_query_params().get('SortingField')

	def set_SortingField(self,SortingField):
		self.add_query_param('SortingField',SortingField)