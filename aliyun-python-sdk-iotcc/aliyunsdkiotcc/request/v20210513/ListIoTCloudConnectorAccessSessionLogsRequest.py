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

class ListIoTCloudConnectorAccessSessionLogsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'ListIoTCloudConnectorAccessSessionLogs','IoTCC')
		self.set_method('POST')

	def get_StartTime(self): # Long
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_query_param('StartTime', StartTime)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_Destinationss(self): # RepeatList
		return self.get_query_params().get('Destinations')

	def set_Destinationss(self, Destinations):  # RepeatList
		for depth1 in range(len(Destinations)):
			self.add_query_param('Destinations.' + str(depth1 + 1), Destinations[depth1])
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_IoTCloudConnectorId(self): # String
		return self.get_query_params().get('IoTCloudConnectorId')

	def set_IoTCloudConnectorId(self, IoTCloudConnectorId):  # String
		self.add_query_param('IoTCloudConnectorId', IoTCloudConnectorId)
	def get_SourceIpss(self): # RepeatList
		return self.get_query_params().get('SourceIps')

	def set_SourceIpss(self, SourceIps):  # RepeatList
		for depth1 in range(len(SourceIps)):
			self.add_query_param('SourceIps.' + str(depth1 + 1), SourceIps[depth1])
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
