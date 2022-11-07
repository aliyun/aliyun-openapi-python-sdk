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

class ListWirelessCloudConnectorGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CC5G', '2022-03-14', 'ListWirelessCloudConnectorGroups','fivegcc')
		self.set_method('GET')

	def get_WirelessCloudConnectorGroupStatus(self): # Array
		return self.get_query_params().get('WirelessCloudConnectorGroupStatus')

	def set_WirelessCloudConnectorGroupStatus(self, WirelessCloudConnectorGroupStatus):  # Array
		for index1, value1 in enumerate(WirelessCloudConnectorGroupStatus):
			self.add_query_param('WirelessCloudConnectorGroupStatus.' + str(index1 + 1), value1)
	def get_WirelessCloudConnectorGroupIds(self): # Array
		return self.get_query_params().get('WirelessCloudConnectorGroupIds')

	def set_WirelessCloudConnectorGroupIds(self, WirelessCloudConnectorGroupIds):  # Array
		for index1, value1 in enumerate(WirelessCloudConnectorGroupIds):
			self.add_query_param('WirelessCloudConnectorGroupIds.' + str(index1 + 1), value1)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_WirelessCloudConnectorGroupNames(self): # Array
		return self.get_query_params().get('WirelessCloudConnectorGroupNames')

	def set_WirelessCloudConnectorGroupNames(self, WirelessCloudConnectorGroupNames):  # Array
		for index1, value1 in enumerate(WirelessCloudConnectorGroupNames):
			self.add_query_param('WirelessCloudConnectorGroupNames.' + str(index1 + 1), value1)
	def get_MaxResults(self): # Long
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_query_param('MaxResults', MaxResults)
