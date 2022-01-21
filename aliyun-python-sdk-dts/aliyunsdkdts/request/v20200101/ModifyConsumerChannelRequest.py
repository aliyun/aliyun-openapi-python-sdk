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
from aliyunsdkdts.endpoint import endpoint_data

class ModifyConsumerChannelRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'ModifyConsumerChannel','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ConsumerGroupName(self): # String
		return self.get_query_params().get('ConsumerGroupName')

	def set_ConsumerGroupName(self, ConsumerGroupName):  # String
		self.add_query_param('ConsumerGroupName', ConsumerGroupName)
	def get_ConsumerGroupId(self): # String
		return self.get_query_params().get('ConsumerGroupId')

	def set_ConsumerGroupId(self, ConsumerGroupId):  # String
		self.add_query_param('ConsumerGroupId', ConsumerGroupId)
	def get_ConsumerGroupPassword(self): # String
		return self.get_query_params().get('ConsumerGroupPassword')

	def set_ConsumerGroupPassword(self, ConsumerGroupPassword):  # String
		self.add_query_param('ConsumerGroupPassword', ConsumerGroupPassword)
	def get_ConsumerGroupUserName(self): # String
		return self.get_query_params().get('ConsumerGroupUserName')

	def set_ConsumerGroupUserName(self, ConsumerGroupUserName):  # String
		self.add_query_param('ConsumerGroupUserName', ConsumerGroupUserName)
	def get_DtsJobId(self): # String
		return self.get_query_params().get('DtsJobId')

	def set_DtsJobId(self, DtsJobId):  # String
		self.add_query_param('DtsJobId', DtsJobId)
	def get_DtsInstanceId(self): # String
		return self.get_query_params().get('DtsInstanceId')

	def set_DtsInstanceId(self, DtsInstanceId):  # String
		self.add_query_param('DtsInstanceId', DtsInstanceId)
