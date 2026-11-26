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

class QueryKnowledgeBasesContentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'QueryKnowledgeBasesContent','GPDB')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TopK(self): # Long
		return self.get_query_params().get('TopK')

	def set_TopK(self, TopK):  # Long
		self.add_query_param('TopK', TopK)
	def get_Content(self): # String
		return self.get_query_params().get('Content')

	def set_Content(self, Content):  # String
		self.add_query_param('Content', Content)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_MergeMethod(self): # String
		return self.get_query_params().get('MergeMethod')

	def set_MergeMethod(self, MergeMethod):  # String
		self.add_query_param('MergeMethod', MergeMethod)
	def get_MergeMethodArgs(self): # Struct
		return self.get_query_params().get('MergeMethodArgs')

	def set_MergeMethodArgs(self, MergeMethodArgs):  # Struct
		self.add_query_param("MergeMethodArgs", json.dumps(MergeMethodArgs))
	def get_RerankFactor(self): # Double
		return self.get_query_params().get('RerankFactor')

	def set_RerankFactor(self, RerankFactor):  # Double
		self.add_query_param('RerankFactor', RerankFactor)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SourceCollection(self): # Array
		return self.get_query_params().get('SourceCollection')

	def set_SourceCollection(self, SourceCollection):  # Array
		self.add_query_param("SourceCollection", json.dumps(SourceCollection))
	def get_RerankModel(self): # Struct
		return self.get_query_params().get('RerankModel')

	def set_RerankModel(self, RerankModel):  # Struct
		self.add_query_param("RerankModel", json.dumps(RerankModel))
