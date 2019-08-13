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
from aliyunsdkemr.endpoint import endpoint_data

class MetastoreUpdateKafkaTopicRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'MetastoreUpdateKafkaTopic','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_TopicId(self):
		return self.get_query_params().get('TopicId')

	def set_TopicId(self,TopicId):
		self.add_query_param('TopicId',TopicId)

	def get_AdvancedConfigs(self):
		return self.get_query_params().get('AdvancedConfigs')

	def set_AdvancedConfigs(self,AdvancedConfigs):
		for i in range(len(AdvancedConfigs)):	
			if AdvancedConfigs[i].get('Value') is not None:
				self.add_query_param('AdvancedConfig.' + str(i + 1) + '.Value' , AdvancedConfigs[i].get('Value'))
			if AdvancedConfigs[i].get('Key') is not None:
				self.add_query_param('AdvancedConfig.' + str(i + 1) + '.Key' , AdvancedConfigs[i].get('Key'))


	def get_NumPartitions(self):
		return self.get_query_params().get('NumPartitions')

	def set_NumPartitions(self,NumPartitions):
		self.add_query_param('NumPartitions',NumPartitions)