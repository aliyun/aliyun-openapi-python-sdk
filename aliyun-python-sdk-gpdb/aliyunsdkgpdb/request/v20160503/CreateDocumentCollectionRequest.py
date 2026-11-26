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

class CreateDocumentCollectionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'CreateDocumentCollection','GPDB')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Metadata(self): # String
		return self.get_query_params().get('Metadata')

	def set_Metadata(self, Metadata):  # String
		self.add_query_param('Metadata', Metadata)
	def get_EmbeddingModel(self): # String
		return self.get_query_params().get('EmbeddingModel')

	def set_EmbeddingModel(self, EmbeddingModel):  # String
		self.add_query_param('EmbeddingModel', EmbeddingModel)
	def get_LLMModel(self): # String
		return self.get_query_params().get('LLMModel')

	def set_LLMModel(self, LLMModel):  # String
		self.add_query_param('LLMModel', LLMModel)
	def get_Language(self): # String
		return self.get_query_params().get('Language')

	def set_Language(self, Language):  # String
		self.add_query_param('Language', Language)
	def get_FullTextRetrievalFields(self): # String
		return self.get_query_params().get('FullTextRetrievalFields')

	def set_FullTextRetrievalFields(self, FullTextRetrievalFields):  # String
		self.add_query_param('FullTextRetrievalFields', FullTextRetrievalFields)
	def get_ManagerAccountPassword(self): # String
		return self.get_query_params().get('ManagerAccountPassword')

	def set_ManagerAccountPassword(self, ManagerAccountPassword):  # String
		self.add_query_param('ManagerAccountPassword', ManagerAccountPassword)
	def get_Algorithm(self): # String
		return self.get_query_params().get('Algorithm')

	def set_Algorithm(self, Algorithm):  # String
		self.add_query_param('Algorithm', Algorithm)
	def get_Collection(self): # String
		return self.get_query_params().get('Collection')

	def set_Collection(self, Collection):  # String
		self.add_query_param('Collection', Collection)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SparseRetrievalFields(self): # String
		return self.get_query_params().get('SparseRetrievalFields')

	def set_SparseRetrievalFields(self, SparseRetrievalFields):  # String
		self.add_query_param('SparseRetrievalFields', SparseRetrievalFields)
	def get_HnswM(self): # Integer
		return self.get_query_params().get('HnswM')

	def set_HnswM(self, HnswM):  # Integer
		self.add_query_param('HnswM', HnswM)
	def get_Parser(self): # String
		return self.get_query_params().get('Parser')

	def set_Parser(self, Parser):  # String
		self.add_query_param('Parser', Parser)
	def get_SupportSparse(self): # Boolean
		return self.get_query_params().get('SupportSparse')

	def set_SupportSparse(self, SupportSparse):  # Boolean
		self.add_query_param('SupportSparse', SupportSparse)
	def get_Metrics(self): # String
		return self.get_query_params().get('Metrics')

	def set_Metrics(self, Metrics):  # String
		self.add_query_param('Metrics', Metrics)
	def get_VectorIndexConfig(self): # Struct
		return self.get_query_params().get('VectorIndexConfig')

	def set_VectorIndexConfig(self, VectorIndexConfig):  # Struct
		self.add_query_param("VectorIndexConfig", json.dumps(VectorIndexConfig))
	def get_SparseVectorIndexConfig(self): # Struct
		return self.get_query_params().get('SparseVectorIndexConfig')

	def set_SparseVectorIndexConfig(self, SparseVectorIndexConfig):  # Struct
		self.add_query_param("SparseVectorIndexConfig", json.dumps(SparseVectorIndexConfig))
	def get_ExternalStorage(self): # Integer
		return self.get_query_params().get('ExternalStorage')

	def set_ExternalStorage(self, ExternalStorage):  # Integer
		self.add_query_param('ExternalStorage', ExternalStorage)
	def get_ManagerAccount(self): # String
		return self.get_query_params().get('ManagerAccount')

	def set_ManagerAccount(self, ManagerAccount):  # String
		self.add_query_param('ManagerAccount', ManagerAccount)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_Dimension(self): # Integer
		return self.get_query_params().get('Dimension')

	def set_Dimension(self, Dimension):  # Integer
		self.add_query_param('Dimension', Dimension)
	def get_HnswEfConstruction(self): # String
		return self.get_query_params().get('HnswEfConstruction')

	def set_HnswEfConstruction(self, HnswEfConstruction):  # String
		self.add_query_param('HnswEfConstruction', HnswEfConstruction)
	def get_RelationshipTypes(self): # Array
		return self.get_query_params().get('RelationshipTypes')

	def set_RelationshipTypes(self, RelationshipTypes):  # Array
		self.add_query_param("RelationshipTypes", json.dumps(RelationshipTypes))
	def get_EnableGraph(self): # Boolean
		return self.get_query_params().get('EnableGraph')

	def set_EnableGraph(self, EnableGraph):  # Boolean
		self.add_query_param('EnableGraph', EnableGraph)
	def get_MetadataIndices(self): # String
		return self.get_query_params().get('MetadataIndices')

	def set_MetadataIndices(self, MetadataIndices):  # String
		self.add_query_param('MetadataIndices', MetadataIndices)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
	def get_EntityTypes(self): # Array
		return self.get_query_params().get('EntityTypes')

	def set_EntityTypes(self, EntityTypes):  # Array
		self.add_query_param("EntityTypes", json.dumps(EntityTypes))
	def get_PqEnable(self): # Integer
		return self.get_query_params().get('PqEnable')

	def set_PqEnable(self, PqEnable):  # Integer
		self.add_query_param('PqEnable', PqEnable)
