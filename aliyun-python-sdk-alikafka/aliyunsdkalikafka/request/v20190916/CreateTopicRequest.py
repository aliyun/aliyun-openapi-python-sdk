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
from aliyunsdkalikafka.endpoint import endpoint_data

class CreateTopicRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'alikafka', '2019-09-16', 'CreateTopic','alikafka')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_ReplicationFactor(self): # Long
		return self.get_query_params().get('ReplicationFactor')

	def set_ReplicationFactor(self, ReplicationFactor):  # Long
		self.add_query_param('ReplicationFactor', ReplicationFactor)
	def get_MinInsyncReplicas(self): # Long
		return self.get_query_params().get('MinInsyncReplicas')

	def set_MinInsyncReplicas(self, MinInsyncReplicas):  # Long
		self.add_query_param('MinInsyncReplicas', MinInsyncReplicas)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_Topic(self): # String
		return self.get_query_params().get('Topic')

	def set_Topic(self, Topic):  # String
		self.add_query_param('Topic', Topic)
	def get_CompactTopic(self): # Boolean
		return self.get_query_params().get('CompactTopic')

	def set_CompactTopic(self, CompactTopic):  # Boolean
		self.add_query_param('CompactTopic', CompactTopic)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_PartitionNum(self): # String
		return self.get_query_params().get('PartitionNum')

	def set_PartitionNum(self, PartitionNum):  # String
		self.add_query_param('PartitionNum', PartitionNum)
	def get_Config(self): # String
		return self.get_query_params().get('Config')

	def set_Config(self, Config):  # String
		self.add_query_param('Config', Config)
	def get_LocalTopic(self): # Boolean
		return self.get_query_params().get('LocalTopic')

	def set_LocalTopic(self, LocalTopic):  # Boolean
		self.add_query_param('LocalTopic', LocalTopic)
