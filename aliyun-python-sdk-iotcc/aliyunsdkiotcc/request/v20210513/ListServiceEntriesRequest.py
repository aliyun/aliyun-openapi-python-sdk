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
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'ListServiceEntries','cciot')
		self.set_method('POST')

	def get_ServiceEntryStatuss(self):
		return self.get_query_params().get('ServiceEntryStatus')

	def set_ServiceEntryStatuss(self, ServiceEntryStatuss):
		for depth1 in range(len(ServiceEntryStatuss)):
			if ServiceEntryStatuss[depth1] is not None:
				self.add_query_param('ServiceEntryStatus.' + str(depth1 + 1) , ServiceEntryStatuss[depth1])

	def get_TargetTypes(self):
		return self.get_query_params().get('TargetType')

	def set_TargetTypes(self, TargetTypes):
		for depth1 in range(len(TargetTypes)):
			if TargetTypes[depth1] is not None:
				self.add_query_param('TargetType.' + str(depth1 + 1) , TargetTypes[depth1])

	def get_ServiceEntryIdss(self):
		return self.get_query_params().get('ServiceEntryIds')

	def set_ServiceEntryIdss(self, ServiceEntryIdss):
		for depth1 in range(len(ServiceEntryIdss)):
			if ServiceEntryIdss[depth1] is not None:
				self.add_query_param('ServiceEntryIds.' + str(depth1 + 1) , ServiceEntryIdss[depth1])

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_ServiceEntryNames(self):
		return self.get_query_params().get('ServiceEntryName')

	def set_ServiceEntryNames(self, ServiceEntryNames):
		for depth1 in range(len(ServiceEntryNames)):
			if ServiceEntryNames[depth1] is not None:
				self.add_query_param('ServiceEntryName.' + str(depth1 + 1) , ServiceEntryNames[depth1])

	def get_Targets(self):
		return self.get_query_params().get('Target')

	def set_Targets(self, Targets):
		for depth1 in range(len(Targets)):
			if Targets[depth1] is not None:
				self.add_query_param('Target.' + str(depth1 + 1) , Targets[depth1])

	def get_IoTCloudConnectorId(self):
		return self.get_query_params().get('IoTCloudConnectorId')

	def set_IoTCloudConnectorId(self,IoTCloudConnectorId):
		self.add_query_param('IoTCloudConnectorId',IoTCloudConnectorId)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)

	def get_ServiceId(self):
		return self.get_query_params().get('ServiceId')

	def set_ServiceId(self,ServiceId):
		self.add_query_param('ServiceId',ServiceId)