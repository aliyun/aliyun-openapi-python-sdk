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
from aliyunsdkimm.endpoint import endpoint_data

class FindSimilarFacesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'FindSimilarFaces','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Project(self): # String
		return self.get_query_params().get('Project')

	def set_Project(self, Project):  # String
		self.add_query_param('Project', Project)
	def get_MinSimilarity(self): # Float
		return self.get_query_params().get('MinSimilarity')

	def set_MinSimilarity(self, MinSimilarity):  # Float
		self.add_query_param('MinSimilarity', MinSimilarity)
	def get_ResponseFormat(self): # String
		return self.get_query_params().get('ResponseFormat')

	def set_ResponseFormat(self, ResponseFormat):  # String
		self.add_query_param('ResponseFormat', ResponseFormat)
	def get_Limit(self): # Integer
		return self.get_query_params().get('Limit')

	def set_Limit(self, Limit):  # Integer
		self.add_query_param('Limit', Limit)
	def get_FaceId(self): # String
		return self.get_query_params().get('FaceId')

	def set_FaceId(self, FaceId):  # String
		self.add_query_param('FaceId', FaceId)
	def get_ImageUri(self): # String
		return self.get_query_params().get('ImageUri')

	def set_ImageUri(self, ImageUri):  # String
		self.add_query_param('ImageUri', ImageUri)
	def get_SetId(self): # String
		return self.get_query_params().get('SetId')

	def set_SetId(self, SetId):  # String
		self.add_query_param('SetId', SetId)
