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
from aliyunsdkoos.endpoint import endpoint_data

class ListInventoryEntriesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'ListInventoryEntries')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Filters(self):
		return self.get_query_params().get('Filter')

	def set_Filters(self, Filters):
		for depth1 in range(len(Filters)):
			if Filters[depth1].get('Name') is not None:
				self.add_query_param('Filter.' + str(depth1 + 1) + '.Name', Filters[depth1].get('Name'))
			if Filters[depth1].get('Value') is not None:
				for depth2 in range(len(Filters[depth1].get('Value'))):
					if Filters[depth1].get('Value')[depth2] is not None:
						self.add_query_param('Filter.' + str(depth1 + 1) + '.Value.' + str(depth2 + 1) , Filters[depth1].get('Value')[depth2])
			if Filters[depth1].get('Operator') is not None:
				self.add_query_param('Filter.' + str(depth1 + 1) + '.Operator', Filters[depth1].get('Operator'))

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)

	def get_TypeName(self):
		return self.get_query_params().get('TypeName')

	def set_TypeName(self,TypeName):
		self.add_query_param('TypeName',TypeName)