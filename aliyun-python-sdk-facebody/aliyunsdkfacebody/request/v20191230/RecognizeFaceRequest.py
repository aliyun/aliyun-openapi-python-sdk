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

class RecognizeFaceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'facebody', '2019-12-30', 'RecognizeFace')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Gender(self):
		return self.get_body_params().get('Gender')

	def set_Gender(self,Gender):
		self.add_body_params('Gender', Gender)

	def get_Beauty(self):
		return self.get_body_params().get('Beauty')

	def set_Beauty(self,Beauty):
		self.add_body_params('Beauty', Beauty)

	def get_MaxFaceNumber(self):
		return self.get_body_params().get('MaxFaceNumber')

	def set_MaxFaceNumber(self,MaxFaceNumber):
		self.add_body_params('MaxFaceNumber', MaxFaceNumber)

	def get_Hat(self):
		return self.get_body_params().get('Hat')

	def set_Hat(self,Hat):
		self.add_body_params('Hat', Hat)

	def get_Mask(self):
		return self.get_body_params().get('Mask')

	def set_Mask(self,Mask):
		self.add_body_params('Mask', Mask)

	def get_Glass(self):
		return self.get_body_params().get('Glass')

	def set_Glass(self,Glass):
		self.add_body_params('Glass', Glass)

	def get_Expression(self):
		return self.get_body_params().get('Expression')

	def set_Expression(self,Expression):
		self.add_body_params('Expression', Expression)

	def get_Quality(self):
		return self.get_body_params().get('Quality')

	def set_Quality(self,Quality):
		self.add_body_params('Quality', Quality)

	def get_ImageURL(self):
		return self.get_body_params().get('ImageURL')

	def set_ImageURL(self,ImageURL):
		self.add_body_params('ImageURL', ImageURL)

	def get_Age(self):
		return self.get_body_params().get('Age')

	def set_Age(self,Age):
		self.add_body_params('Age', Age)