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

class ListNetworkAccessEndpointsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'ListNetworkAccessEndpoints','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_NetworkAccessEndpointType(self): # String
		return self.get_query_params().get('NetworkAccessEndpointType')

	def set_NetworkAccessEndpointType(self, NetworkAccessEndpointType):  # String
		self.add_query_param('NetworkAccessEndpointType', NetworkAccessEndpointType)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_VpcRegionId(self): # String
		return self.get_query_params().get('VpcRegionId')

	def set_VpcRegionId(self, VpcRegionId):  # String
		self.add_query_param('VpcRegionId', VpcRegionId)
	def get_NetworkAccessEndpointStatus(self): # String
		return self.get_query_params().get('NetworkAccessEndpointStatus')

	def set_NetworkAccessEndpointStatus(self, NetworkAccessEndpointStatus):  # String
		self.add_query_param('NetworkAccessEndpointStatus', NetworkAccessEndpointStatus)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_MaxResults(self): # Long
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_query_param('MaxResults', MaxResults)
