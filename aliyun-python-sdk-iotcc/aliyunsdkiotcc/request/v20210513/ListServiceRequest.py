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

class ListServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'ListService','IoTCC')
		self.set_method('POST')

	def get_ServiceIdss(self): # RepeatList
		return self.get_query_params().get('ServiceIds')

	def set_ServiceIdss(self, ServiceIds):  # RepeatList
		for depth1 in range(len(ServiceIds)):
			self.add_query_param('ServiceIds.' + str(depth1 + 1), ServiceIds[depth1])
	def get_ResourceStatusess(self): # RepeatList
		return self.get_query_params().get('ResourceStatuses')

	def set_ResourceStatusess(self, ResourceStatuses):  # RepeatList
		for depth1 in range(len(ResourceStatuses)):
			self.add_query_param('ResourceStatuses.' + str(depth1 + 1), ResourceStatuses[depth1])
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_ServiceNamess(self): # RepeatList
		return self.get_query_params().get('ServiceNames')

	def set_ServiceNamess(self, ServiceNames):  # RepeatList
		for depth1 in range(len(ServiceNames)):
			self.add_query_param('ServiceNames.' + str(depth1 + 1), ServiceNames[depth1])
	def get_IoTCloudConnectorId(self): # String
		return self.get_query_params().get('IoTCloudConnectorId')

	def set_IoTCloudConnectorId(self, IoTCloudConnectorId):  # String
		self.add_query_param('IoTCloudConnectorId', IoTCloudConnectorId)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
