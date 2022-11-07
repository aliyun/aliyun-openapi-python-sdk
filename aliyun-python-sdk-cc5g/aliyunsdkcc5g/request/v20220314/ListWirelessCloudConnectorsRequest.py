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

class ListWirelessCloudConnectorsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CC5G', '2022-03-14', 'ListWirelessCloudConnectors','fivegcc')
		self.set_method('GET')

	def get_WirelessCloudConnectorGroupId(self): # String
		return self.get_query_params().get('WirelessCloudConnectorGroupId')

	def set_WirelessCloudConnectorGroupId(self, WirelessCloudConnectorGroupId):  # String
		self.add_query_param('WirelessCloudConnectorGroupId', WirelessCloudConnectorGroupId)
	def get_BusinessType(self): # String
		return self.get_query_params().get('BusinessType')

	def set_BusinessType(self, BusinessType):  # String
		self.add_query_param('BusinessType', BusinessType)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_WirelessCloudConnectorIds(self): # Array
		return self.get_query_params().get('WirelessCloudConnectorIds')

	def set_WirelessCloudConnectorIds(self, WirelessCloudConnectorIds):  # Array
		for index1, value1 in enumerate(WirelessCloudConnectorIds):
			self.add_query_param('WirelessCloudConnectorIds.' + str(index1 + 1), value1)
	def get_IsInGroup(self): # String
		return self.get_query_params().get('IsInGroup')

	def set_IsInGroup(self, IsInGroup):  # String
		self.add_query_param('IsInGroup', IsInGroup)
	def get_Names(self): # Array
		return self.get_query_params().get('Names')

	def set_Names(self, Names):  # Array
		for index1, value1 in enumerate(Names):
			self.add_query_param('Names.' + str(index1 + 1), value1)
	def get_MaxResults(self): # Long
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_query_param('MaxResults', MaxResults)
	def get_Statuses(self): # Array
		return self.get_query_params().get('Statuses')

	def set_Statuses(self, Statuses):  # Array
		for index1, value1 in enumerate(Statuses):
			self.add_query_param('Statuses.' + str(index1 + 1), value1)
