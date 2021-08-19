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

class BeautifyBodyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'facebody', '2019-12-30', 'BeautifyBody','facebody')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_BodyBoxes(self):
		return self.get_body_params().get('BodyBoxes')

	def set_BodyBoxes(self,BodyBoxes):
		self.add_body_params('BodyBoxes', BodyBoxes)

	def get_LengthenDegree(self):
		return self.get_body_params().get('LengthenDegree')

	def set_LengthenDegree(self,LengthenDegree):
		self.add_body_params('LengthenDegree', LengthenDegree)

	def get_MaleLiquifyDegree(self):
		return self.get_body_params().get('MaleLiquifyDegree')

	def set_MaleLiquifyDegree(self,MaleLiquifyDegree):
		self.add_body_params('MaleLiquifyDegree', MaleLiquifyDegree)

	def get_OriginalWidth(self):
		return self.get_body_params().get('OriginalWidth')

	def set_OriginalWidth(self,OriginalWidth):
		self.add_body_params('OriginalWidth', OriginalWidth)

	def get_FaceList(self):
		return self.get_body_params().get('FaceList')

	def set_FaceList(self,FaceList):
		self.add_body_params('FaceList', FaceList)

	def get_AgeRange(self):
		return self.get_body_params().get('AgeRange')

	def set_AgeRange(self,AgeRange):
		self.add_body_params('AgeRange', AgeRange)

	def get_Custom(self):
		return self.get_body_params().get('Custom')

	def set_Custom(self,Custom):
		self.add_body_params('Custom', Custom)

	def get_OriginalHeight(self):
		return self.get_body_params().get('OriginalHeight')

	def set_OriginalHeight(self,OriginalHeight):
		self.add_body_params('OriginalHeight', OriginalHeight)

	def get_ImageURL(self):
		return self.get_body_params().get('ImageURL')

	def set_ImageURL(self,ImageURL):
		self.add_body_params('ImageURL', ImageURL)

	def get_FemaleLiquifyDegree(self):
		return self.get_body_params().get('FemaleLiquifyDegree')

	def set_FemaleLiquifyDegree(self,FemaleLiquifyDegree):
		self.add_body_params('FemaleLiquifyDegree', FemaleLiquifyDegree)

	def get_PoseList(self):
		return self.get_body_params().get('PoseList')

	def set_PoseList(self,PoseList):
		self.add_body_params('PoseList', PoseList)