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
import json

class UpgradePostPayOrderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'alikafka', '2019-09-16', 'UpgradePostPayOrder','alikafka')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ServerlessConfig(self): # Struct
		return self.get_query_params().get('ServerlessConfig')

	def set_ServerlessConfig(self, ServerlessConfig):  # Struct
		self.add_query_param("ServerlessConfig", json.dumps(ServerlessConfig))
	def get_DiskSize(self): # Integer
		return self.get_query_params().get('DiskSize')

	def set_DiskSize(self, DiskSize):  # Integer
		self.add_query_param('DiskSize', DiskSize)
	def get_IoMax(self): # Integer
		return self.get_query_params().get('IoMax')

	def set_IoMax(self, IoMax):  # Integer
		self.add_query_param('IoMax', IoMax)
	def get_EipModel(self): # Boolean
		return self.get_query_params().get('EipModel')

	def set_EipModel(self, EipModel):  # Boolean
		self.add_query_param('EipModel', EipModel)
	def get_IoMaxSpec(self): # String
		return self.get_query_params().get('IoMaxSpec')

	def set_IoMaxSpec(self, IoMaxSpec):  # String
		self.add_query_param('IoMaxSpec', IoMaxSpec)
	def get_TopicQuota(self): # Integer
		return self.get_query_params().get('TopicQuota')

	def set_TopicQuota(self, TopicQuota):  # Integer
		self.add_query_param('TopicQuota', TopicQuota)
	def get_EipMax(self): # Integer
		return self.get_query_params().get('EipMax')

	def set_EipMax(self, EipMax):  # Integer
		self.add_query_param('EipMax', EipMax)
	def get_SpecType(self): # String
		return self.get_query_params().get('SpecType')

	def set_SpecType(self, SpecType):  # String
		self.add_query_param('SpecType', SpecType)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_PartitionNum(self): # Integer
		return self.get_query_params().get('PartitionNum')

	def set_PartitionNum(self, PartitionNum):  # Integer
		self.add_query_param('PartitionNum', PartitionNum)
