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
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'ListConnectionPools','IoTCC')
		self.set_method('POST')

	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_ConnectionPoolStatuss(self): # RepeatList
		return self.get_query_params().get('ConnectionPoolStatus')

	def set_ConnectionPoolStatuss(self, ConnectionPoolStatus):  # RepeatList
		for depth1 in range(len(ConnectionPoolStatus)):
			self.add_query_param('ConnectionPoolStatus.' + str(depth1 + 1), ConnectionPoolStatus[depth1])
	def get_ConnectionPoolNames(self): # RepeatList
		return self.get_query_params().get('ConnectionPoolName')

	def set_ConnectionPoolNames(self, ConnectionPoolName):  # RepeatList
		for depth1 in range(len(ConnectionPoolName)):
			self.add_query_param('ConnectionPoolName.' + str(depth1 + 1), ConnectionPoolName[depth1])
	def get_IoTCloudConnectorId(self): # String
		return self.get_query_params().get('IoTCloudConnectorId')

	def set_IoTCloudConnectorId(self, IoTCloudConnectorId):  # String
		self.add_query_param('IoTCloudConnectorId', IoTCloudConnectorId)
	def get_ConnectionPoolIdss(self): # RepeatList
		return self.get_query_params().get('ConnectionPoolIds')

	def set_ConnectionPoolIdss(self, ConnectionPoolIds):  # RepeatList
		for depth1 in range(len(ConnectionPoolIds)):
			self.add_query_param('ConnectionPoolIds.' + str(depth1 + 1), ConnectionPoolIds[depth1])
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
