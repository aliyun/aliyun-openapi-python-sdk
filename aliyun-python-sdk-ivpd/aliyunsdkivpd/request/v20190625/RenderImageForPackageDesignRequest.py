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
from aliyunsdkivpd.endpoint import endpoint_data

class RenderImageForPackageDesignRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ivpd', '2019-06-25', 'RenderImageForPackageDesign')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DisplayType(self):
		return self.get_body_params().get('DisplayType')

	def set_DisplayType(self,DisplayType):
		self.add_body_params('DisplayType', DisplayType)

	def get_MaterialName(self):
		return self.get_body_params().get('MaterialName')

	def set_MaterialName(self,MaterialName):
		self.add_body_params('MaterialName', MaterialName)

	def get_JobId(self):
		return self.get_body_params().get('JobId')

	def set_JobId(self,JobId):
		self.add_body_params('JobId', JobId)

	def get_MaterialType(self):
		return self.get_body_params().get('MaterialType')

	def set_MaterialType(self,MaterialType):
		self.add_body_params('MaterialType', MaterialType)

	def get_ModelType(self):
		return self.get_body_params().get('ModelType')

	def set_ModelType(self,ModelType):
		self.add_body_params('ModelType', ModelType)

	def get_TargetWidth(self):
		return self.get_body_params().get('TargetWidth')

	def set_TargetWidth(self,TargetWidth):
		self.add_body_params('TargetWidth', TargetWidth)

	def get_ElementLists(self):
		return self.get_body_params().get('ElementLists')

	def set_ElementLists(self,ElementLists):
		for i in range(len(ElementLists)):	
			if ElementLists[i].get('ImageUrl') is not None:
				self.add_body_params('ElementList.' + str(i + 1) + '.ImageUrl' , ElementLists[i].get('ImageUrl'))
			if ElementLists[i].get('SideName') is not None:
				self.add_body_params('ElementList.' + str(i + 1) + '.SideName' , ElementLists[i].get('SideName'))


	def get_Category(self):
		return self.get_body_params().get('Category')

	def set_Category(self,Category):
		self.add_body_params('Category', Category)

	def get_TargetHeight(self):
		return self.get_body_params().get('TargetHeight')

	def set_TargetHeight(self,TargetHeight):
		self.add_body_params('TargetHeight', TargetHeight)