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

class CompareFaceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'facebody', '2019-12-30', 'CompareFace','facebody')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ImageDataA(self): # String
		return self.get_body_params().get('ImageDataA')

	def set_ImageDataA(self, ImageDataA):  # String
		self.add_body_params('ImageDataA', ImageDataA)
	def get_ImageDataB(self): # String
		return self.get_body_params().get('ImageDataB')

	def set_ImageDataB(self, ImageDataB):  # String
		self.add_body_params('ImageDataB', ImageDataB)
	def get_QualityScoreThreshold(self): # Float
		return self.get_body_params().get('QualityScoreThreshold')

	def set_QualityScoreThreshold(self, QualityScoreThreshold):  # Float
		self.add_body_params('QualityScoreThreshold', QualityScoreThreshold)
	def get_ImageURLB(self): # String
		return self.get_body_params().get('ImageURLB')

	def set_ImageURLB(self, ImageURLB):  # String
		self.add_body_params('ImageURLB', ImageURLB)
	def get_ImageURLA(self): # String
		return self.get_body_params().get('ImageURLA')

	def set_ImageURLA(self, ImageURLA):  # String
		self.add_body_params('ImageURLA', ImageURLA)
