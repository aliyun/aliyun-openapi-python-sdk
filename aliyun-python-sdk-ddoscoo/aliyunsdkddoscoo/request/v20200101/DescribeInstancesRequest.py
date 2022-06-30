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
from aliyunsdkddoscoo.endpoint import endpoint_data

class DescribeInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ddoscoo', '2020-01-01', 'DescribeInstances')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Edition(self): # Integer
		return self.get_query_params().get('Edition')

	def set_Edition(self, Edition):  # Integer
		self.add_query_param('Edition', Edition)
	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_PageNumber(self): # String
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # String
		self.add_query_param('PageNumber', PageNumber)
	def get_Enabled(self): # Integer
		return self.get_query_params().get('Enabled')

	def set_Enabled(self, Enabled):  # Integer
		self.add_query_param('Enabled', Enabled)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_ExpireStartTime(self): # Long
		return self.get_query_params().get('ExpireStartTime')

	def set_ExpireStartTime(self, ExpireStartTime):  # Long
		self.add_query_param('ExpireStartTime', ExpireStartTime)
	def get_ExpireEndTime(self): # Long
		return self.get_query_params().get('ExpireEndTime')

	def set_ExpireEndTime(self, ExpireEndTime):  # Long
		self.add_query_param('ExpireEndTime', ExpireEndTime)
	def get_Ip(self): # String
		return self.get_query_params().get('Ip')

	def set_Ip(self, Ip):  # String
		self.add_query_param('Ip', Ip)
	def get_InstanceIdss(self): # RepeatList
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIdss(self, InstanceIds):  # RepeatList
		for depth1 in range(len(InstanceIds)):
			self.add_query_param('InstanceIds.' + str(depth1 + 1), InstanceIds[depth1])
	def get_Statuss(self): # RepeatList
		return self.get_query_params().get('Status')

	def set_Statuss(self, Status):  # RepeatList
		for depth1 in range(len(Status)):
			self.add_query_param('Status.' + str(depth1 + 1), Status[depth1])
