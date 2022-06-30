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
from aliyunsdkfacebody.endpoint import endpoint_data

class AddFaceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'facebody', '2019-12-30', 'AddFace','facebody')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EntityId(self): # String
		return self.get_body_params().get('EntityId')

	def set_EntityId(self, EntityId):  # String
		self.add_body_params('EntityId', EntityId)
	def get_QualityScoreThreshold(self): # Float
		return self.get_body_params().get('QualityScoreThreshold')

	def set_QualityScoreThreshold(self, QualityScoreThreshold):  # Float
		self.add_body_params('QualityScoreThreshold', QualityScoreThreshold)
	def get_SimilarityScoreThresholdBetweenEntity(self): # Float
		return self.get_body_params().get('SimilarityScoreThresholdBetweenEntity')

	def set_SimilarityScoreThresholdBetweenEntity(self, SimilarityScoreThresholdBetweenEntity):  # Float
		self.add_body_params('SimilarityScoreThresholdBetweenEntity', SimilarityScoreThresholdBetweenEntity)
	def get_ExtraData(self): # String
		return self.get_body_params().get('ExtraData')

	def set_ExtraData(self, ExtraData):  # String
		self.add_body_params('ExtraData', ExtraData)
	def get_SimilarityScoreThresholdInEntity(self): # Float
		return self.get_body_params().get('SimilarityScoreThresholdInEntity')

	def set_SimilarityScoreThresholdInEntity(self, SimilarityScoreThresholdInEntity):  # Float
		self.add_body_params('SimilarityScoreThresholdInEntity', SimilarityScoreThresholdInEntity)
	def get_DbName(self): # String
		return self.get_body_params().get('DbName')

	def set_DbName(self, DbName):  # String
		self.add_body_params('DbName', DbName)
	def get_ImageUrl(self): # String
		return self.get_body_params().get('ImageUrl')

	def set_ImageUrl(self, ImageUrl):  # String
		self.add_body_params('ImageUrl', ImageUrl)
