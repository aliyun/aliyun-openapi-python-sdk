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
from aliyunsdkgpdb.endpoint import endpoint_data
import json

class ChatWithKnowledgeBaseRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'ChatWithKnowledgeBase','GPDB')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_IncludeKnowledgeBaseResults(self): # Boolean
		return self.get_query_params().get('IncludeKnowledgeBaseResults')

	def set_IncludeKnowledgeBaseResults(self, IncludeKnowledgeBaseResults):  # Boolean
		self.add_query_param('IncludeKnowledgeBaseResults', IncludeKnowledgeBaseResults)
	def get_PromptParams(self): # String
		return self.get_query_params().get('PromptParams')

	def set_PromptParams(self, PromptParams):  # String
		self.add_query_param('PromptParams', PromptParams)
	def get_KnowledgeParams(self): # Struct
		return self.get_query_params().get('KnowledgeParams')

	def set_KnowledgeParams(self, KnowledgeParams):  # Struct
		self.add_query_param("KnowledgeParams", json.dumps(KnowledgeParams))
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ModelParams(self): # Struct
		return self.get_query_params().get('ModelParams')

	def set_ModelParams(self, ModelParams):  # Struct
		self.add_query_param("ModelParams", json.dumps(ModelParams))
