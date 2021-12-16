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

class ListServiceEntriesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'ListServiceEntries','IoTCC')
		self.set_method('POST')

	def get_ServiceEntryStatuss(self): # RepeatList
		return self.get_query_params().get('ServiceEntryStatus')

	def set_ServiceEntryStatuss(self, ServiceEntryStatus):  # RepeatList
		for depth1 in range(len(ServiceEntryStatus)):
			self.add_query_param('ServiceEntryStatus.' + str(depth1 + 1), ServiceEntryStatus[depth1])
	def get_TargetTypes(self): # RepeatList
		return self.get_query_params().get('TargetType')

	def set_TargetTypes(self, TargetType):  # RepeatList
		for depth1 in range(len(TargetType)):
			self.add_query_param('TargetType.' + str(depth1 + 1), TargetType[depth1])
	def get_ServiceEntryIdss(self): # RepeatList
		return self.get_query_params().get('ServiceEntryIds')

	def set_ServiceEntryIdss(self, ServiceEntryIds):  # RepeatList
		for depth1 in range(len(ServiceEntryIds)):
			self.add_query_param('ServiceEntryIds.' + str(depth1 + 1), ServiceEntryIds[depth1])
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_ServiceEntryNames(self): # RepeatList
		return self.get_query_params().get('ServiceEntryName')

	def set_ServiceEntryNames(self, ServiceEntryName):  # RepeatList
		for depth1 in range(len(ServiceEntryName)):
			self.add_query_param('ServiceEntryName.' + str(depth1 + 1), ServiceEntryName[depth1])
	def get_Targets(self): # RepeatList
		return self.get_query_params().get('Target')

	def set_Targets(self, Target):  # RepeatList
		for depth1 in range(len(Target)):
			self.add_query_param('Target.' + str(depth1 + 1), Target[depth1])
	def get_IoTCloudConnectorId(self): # String
		return self.get_query_params().get('IoTCloudConnectorId')

	def set_IoTCloudConnectorId(self, IoTCloudConnectorId):  # String
		self.add_query_param('IoTCloudConnectorId', IoTCloudConnectorId)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_ServiceId(self): # String
		return self.get_query_params().get('ServiceId')

	def set_ServiceId(self, ServiceId):  # String
		self.add_query_param('ServiceId', ServiceId)
