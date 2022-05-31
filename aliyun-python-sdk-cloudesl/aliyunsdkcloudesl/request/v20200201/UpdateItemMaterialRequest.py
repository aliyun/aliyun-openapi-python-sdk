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
from aliyunsdkcloudesl.endpoint import endpoint_data

class UpdateItemMaterialRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2020-02-01', 'UpdateItemMaterial')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MaterialId(self):
		return self.get_body_params().get('MaterialId')

	def set_MaterialId(self,MaterialId):
		self.add_body_params('MaterialId', MaterialId)

	def get_BarCode(self):
		return self.get_body_params().get('BarCode')

	def set_BarCode(self,BarCode):
		self.add_body_params('BarCode', BarCode)

	def get_ItemName(self):
		return self.get_body_params().get('ItemName')

	def set_ItemName(self,ItemName):
		self.add_body_params('ItemName', ItemName)

	def get_MaterialFeatureA(self):
		return self.get_body_params().get('MaterialFeatureA')

	def set_MaterialFeatureA(self,MaterialFeatureA):
		self.add_body_params('MaterialFeatureA', MaterialFeatureA)

	def get_MaterialFeatureB(self):
		return self.get_body_params().get('MaterialFeatureB')

	def set_MaterialFeatureB(self,MaterialFeatureB):
		self.add_body_params('MaterialFeatureB', MaterialFeatureB)

	def get_MaterialFeatureC(self):
		return self.get_body_params().get('MaterialFeatureC')

	def set_MaterialFeatureC(self,MaterialFeatureC):
		self.add_body_params('MaterialFeatureC', MaterialFeatureC)

	def get_MaterialFeatureD(self):
		return self.get_body_params().get('MaterialFeatureD')

	def set_MaterialFeatureD(self,MaterialFeatureD):
		self.add_body_params('MaterialFeatureD', MaterialFeatureD)