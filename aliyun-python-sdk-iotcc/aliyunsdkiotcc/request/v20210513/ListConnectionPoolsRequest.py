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

class ListConnectionPoolsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'ListConnectionPools','cciot')
		self.set_method('POST')

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_ConnectionPoolStatuss(self):
		return self.get_query_params().get('ConnectionPoolStatus')

	def set_ConnectionPoolStatuss(self, ConnectionPoolStatuss):
		for depth1 in range(len(ConnectionPoolStatuss)):
			if ConnectionPoolStatuss[depth1] is not None:
				self.add_query_param('ConnectionPoolStatus.' + str(depth1 + 1) , ConnectionPoolStatuss[depth1])

	def get_ConnectionPoolNames(self):
		return self.get_query_params().get('ConnectionPoolName')

	def set_ConnectionPoolNames(self, ConnectionPoolNames):
		for depth1 in range(len(ConnectionPoolNames)):
			if ConnectionPoolNames[depth1] is not None:
				self.add_query_param('ConnectionPoolName.' + str(depth1 + 1) , ConnectionPoolNames[depth1])

	def get_IoTCloudConnectorId(self):
		return self.get_query_params().get('IoTCloudConnectorId')

	def set_IoTCloudConnectorId(self,IoTCloudConnectorId):
		self.add_query_param('IoTCloudConnectorId',IoTCloudConnectorId)

	def get_ConnectionPoolIdss(self):
		return self.get_query_params().get('ConnectionPoolIds')

	def set_ConnectionPoolIdss(self, ConnectionPoolIdss):
		for depth1 in range(len(ConnectionPoolIdss)):
			if ConnectionPoolIdss[depth1] is not None:
				self.add_query_param('ConnectionPoolIds.' + str(depth1 + 1) , ConnectionPoolIdss[depth1])

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)