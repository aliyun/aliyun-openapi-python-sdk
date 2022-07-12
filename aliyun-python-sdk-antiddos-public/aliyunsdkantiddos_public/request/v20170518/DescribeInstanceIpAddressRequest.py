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

class DescribeInstanceIpAddressRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'antiddos-public', '2017-05-18', 'DescribeInstanceIpAddress')
		self.set_method('POST')

	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_DdosRegionId(self): # String
		return self.get_query_params().get('DdosRegionId')

	def set_DdosRegionId(self, DdosRegionId):  # String
		self.add_query_param('DdosRegionId', DdosRegionId)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_DdosStatus(self): # String
		return self.get_query_params().get('DdosStatus')

	def set_DdosStatus(self, DdosStatus):  # String
		self.add_query_param('DdosStatus', DdosStatus)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_InstanceName(self): # String
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_query_param('InstanceName', InstanceName)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_InstanceIp(self): # String
		return self.get_query_params().get('InstanceIp')

	def set_InstanceIp(self, InstanceIp):  # String
		self.add_query_param('InstanceIp', InstanceIp)
