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
from aliyunsdkmns_open.endpoint import endpoint_data

class CreateQueueRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mns-open', '2022-01-19', 'CreateQueue','mns')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_QueueName(self): # String
		return self.get_query_params().get('QueueName')

	def set_QueueName(self, QueueName):  # String
		self.add_query_param('QueueName', QueueName)
	def get_MessageRetentionPeriod(self): # Long
		return self.get_query_params().get('MessageRetentionPeriod')

	def set_MessageRetentionPeriod(self, MessageRetentionPeriod):  # Long
		self.add_query_param('MessageRetentionPeriod', MessageRetentionPeriod)
	def get_EnableLogging(self): # Boolean
		return self.get_query_params().get('EnableLogging')

	def set_EnableLogging(self, EnableLogging):  # Boolean
		self.add_query_param('EnableLogging', EnableLogging)
	def get_VisibilityTimeout(self): # Long
		return self.get_query_params().get('VisibilityTimeout')

	def set_VisibilityTimeout(self, VisibilityTimeout):  # Long
		self.add_query_param('VisibilityTimeout', VisibilityTimeout)
	def get_MaximumMessageSize(self): # Long
		return self.get_query_params().get('MaximumMessageSize')

	def set_MaximumMessageSize(self, MaximumMessageSize):  # Long
		self.add_query_param('MaximumMessageSize', MaximumMessageSize)
	def get_DelaySeconds(self): # Long
		return self.get_query_params().get('DelaySeconds')

	def set_DelaySeconds(self, DelaySeconds):  # Long
		self.add_query_param('DelaySeconds', DelaySeconds)
	def get_PollingWaitSeconds(self): # Long
		return self.get_query_params().get('PollingWaitSeconds')

	def set_PollingWaitSeconds(self, PollingWaitSeconds):  # Long
		self.add_query_param('PollingWaitSeconds', PollingWaitSeconds)
