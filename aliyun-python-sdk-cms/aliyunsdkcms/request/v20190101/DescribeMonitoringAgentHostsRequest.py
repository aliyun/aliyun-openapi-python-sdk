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

class DescribeMonitoringAgentHostsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'DescribeMonitoringAgentHosts','cms')
		self.set_method('POST')

	def get_SerialNumbers(self): # String
		return self.get_query_params().get('SerialNumbers')

	def set_SerialNumbers(self, SerialNumbers):  # String
		self.add_query_param('SerialNumbers', SerialNumbers)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_HostName(self): # String
		return self.get_query_params().get('HostName')

	def set_HostName(self, HostName):  # String
		self.add_query_param('HostName', HostName)
	def get_InstanceRegionId(self): # String
		return self.get_query_params().get('InstanceRegionId')

	def set_InstanceRegionId(self, InstanceRegionId):  # String
		self.add_query_param('InstanceRegionId', InstanceRegionId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_AliyunHost(self): # Boolean
		return self.get_query_params().get('AliyunHost')

	def set_AliyunHost(self, AliyunHost):  # Boolean
		self.add_query_param('AliyunHost', AliyunHost)
	def get_KeyWord(self): # String
		return self.get_query_params().get('KeyWord')

	def set_KeyWord(self, KeyWord):  # String
		self.add_query_param('KeyWord', KeyWord)
	def get_InstanceIds(self): # String
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self, InstanceIds):  # String
		self.add_query_param('InstanceIds', InstanceIds)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
