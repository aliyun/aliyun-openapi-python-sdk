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

class QueryContentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'QueryContent','GPDB')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TopK(self): # Integer
		return self.get_query_params().get('TopK')

	def set_TopK(self, TopK):  # Integer
		self.add_query_param('TopK', TopK)
	def get_HybridSearchArgs(self): # Map
		return self.get_query_params().get('HybridSearchArgs')

	def set_HybridSearchArgs(self, HybridSearchArgs):  # Map
		self.add_query_param("HybridSearchArgs", json.dumps(HybridSearchArgs))
	def get_RecallWindow(self): # Array
		return self.get_query_params().get('RecallWindow')

	def set_RecallWindow(self, RecallWindow):  # Array
		self.add_query_param("RecallWindow", json.dumps(RecallWindow))
	def get_GraphEnhance(self): # Boolean
		return self.get_query_params().get('GraphEnhance')

	def set_GraphEnhance(self, GraphEnhance):  # Boolean
		self.add_query_param('GraphEnhance', GraphEnhance)
	def get_Offset(self): # Integer
		return self.get_query_params().get('Offset')

	def set_Offset(self, Offset):  # Integer
		self.add_query_param('Offset', Offset)
	def get_OrderBy(self): # String
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self, OrderBy):  # String
		self.add_query_param('OrderBy', OrderBy)
	def get_Collection(self): # String
		return self.get_query_params().get('Collection')

	def set_Collection(self, Collection):  # String
		self.add_query_param('Collection', Collection)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_GraphSearchArgs(self): # Struct
		return self.get_query_params().get('GraphSearchArgs')

	def set_GraphSearchArgs(self, GraphSearchArgs):  # Struct
		self.add_query_param("GraphSearchArgs", json.dumps(GraphSearchArgs))
	def get_NamespacePassword(self): # String
		return self.get_query_params().get('NamespacePassword')

	def set_NamespacePassword(self, NamespacePassword):  # String
		self.add_query_param('NamespacePassword', NamespacePassword)
	def get_FileName(self): # String
		return self.get_query_params().get('FileName')

	def set_FileName(self, FileName):  # String
		self.add_query_param('FileName', FileName)
	def get_Metrics(self): # String
		return self.get_query_params().get('Metrics')

	def set_Metrics(self, Metrics):  # String
		self.add_query_param('Metrics', Metrics)
	def get_HybridSearch(self): # String
		return self.get_query_params().get('HybridSearch')

	def set_HybridSearch(self, HybridSearch):  # String
		self.add_query_param('HybridSearch', HybridSearch)
	def get_IncludeVector(self): # Boolean
		return self.get_query_params().get('IncludeVector')

	def set_IncludeVector(self, IncludeVector):  # Boolean
		self.add_query_param('IncludeVector', IncludeVector)
	def get_IncludeMetadataFields(self): # String
		return self.get_query_params().get('IncludeMetadataFields')

	def set_IncludeMetadataFields(self, IncludeMetadataFields):  # String
		self.add_query_param('IncludeMetadataFields', IncludeMetadataFields)
	def get_UseFullTextRetrieval(self): # Boolean
		return self.get_query_params().get('UseFullTextRetrieval')

	def set_UseFullTextRetrieval(self, UseFullTextRetrieval):  # Boolean
		self.add_query_param('UseFullTextRetrieval', UseFullTextRetrieval)
	def get_Content(self): # String
		return self.get_body_params().get('Content')

	def set_Content(self, Content):  # String
		self.add_body_params('Content', Content)
	def get_UrlExpiration(self): # String
		return self.get_query_params().get('UrlExpiration')

	def set_UrlExpiration(self, UrlExpiration):  # String
		self.add_query_param('UrlExpiration', UrlExpiration)
	def get_IncludeFileUrl(self): # Boolean
		return self.get_query_params().get('IncludeFileUrl')

	def set_IncludeFileUrl(self, IncludeFileUrl):  # Boolean
		self.add_query_param('IncludeFileUrl', IncludeFileUrl)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_RerankFactor(self): # Double
		return self.get_query_params().get('RerankFactor')

	def set_RerankFactor(self, RerankFactor):  # Double
		self.add_query_param('RerankFactor', RerankFactor)
	def get_Filter(self): # String
		return self.get_body_params().get('Filter')

	def set_Filter(self, Filter):  # String
		self.add_body_params('Filter', Filter)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
	def get_FileUrl(self): # String
		return self.get_query_params().get('FileUrl')

	def set_FileUrl(self, FileUrl):  # String
		self.add_query_param('FileUrl', FileUrl)
	def get_RerankModel(self): # Struct
		return self.get_query_params().get('RerankModel')

	def set_RerankModel(self, RerankModel):  # Struct
		self.add_query_param("RerankModel", json.dumps(RerankModel))
