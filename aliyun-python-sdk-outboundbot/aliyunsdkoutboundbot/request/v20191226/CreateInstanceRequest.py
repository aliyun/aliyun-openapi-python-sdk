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
from aliyunsdkoutboundbot.endpoint import endpoint_data

class CreateInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'CreateInstance')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MaxConcurrentConversation(self): # Integer
		return self.get_query_params().get('MaxConcurrentConversation')

	def set_MaxConcurrentConversation(self, MaxConcurrentConversation):  # Integer
		self.add_query_param('MaxConcurrentConversation', MaxConcurrentConversation)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_CallingNumbers(self): # RepeatList
		return self.get_query_params().get('CallingNumber')

	def set_CallingNumbers(self, CallingNumber):  # RepeatList
		for depth1 in range(len(CallingNumber)):
			self.add_query_param('CallingNumber.' + str(depth1 + 1), CallingNumber[depth1])
	def get_InstanceName(self): # String
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_query_param('InstanceName', InstanceName)
	def get_InstanceDescription(self): # String
		return self.get_query_params().get('InstanceDescription')

	def set_InstanceDescription(self, InstanceDescription):  # String
		self.add_query_param('InstanceDescription', InstanceDescription)
	def get_NluServiceType(self): # String
		return self.get_query_params().get('NluServiceType')

	def set_NluServiceType(self, NluServiceType):  # String
		self.add_query_param('NluServiceType', NluServiceType)
