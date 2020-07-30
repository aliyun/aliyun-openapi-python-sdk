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
from aliyunsdkvideoenhan.endpoint import endpoint_data

class ChangeVideoSizeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'videoenhan', '2020-03-20', 'ChangeVideoSize','videoenhan')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Height(self):
		return self.get_body_params().get('Height')

	def set_Height(self,Height):
		self.add_body_params('Height', Height)

	def get_B(self):
		return self.get_body_params().get('B')

	def set_B(self,B):
		self.add_body_params('B', B)

	def get_FillType(self):
		return self.get_body_params().get('FillType')

	def set_FillType(self,FillType):
		self.add_body_params('FillType', FillType)

	def get_G(self):
		return self.get_body_params().get('G')

	def set_G(self,G):
		self.add_body_params('G', G)

	def get_CropType(self):
		return self.get_body_params().get('CropType')

	def set_CropType(self,CropType):
		self.add_body_params('CropType', CropType)

	def get_R(self):
		return self.get_body_params().get('R')

	def set_R(self,R):
		self.add_body_params('R', R)

	def get_VideoUrl(self):
		return self.get_body_params().get('VideoUrl')

	def set_VideoUrl(self,VideoUrl):
		self.add_body_params('VideoUrl', VideoUrl)

	def get_Width(self):
		return self.get_body_params().get('Width')

	def set_Width(self,Width):
		self.add_body_params('Width', Width)

	def get_Tightness(self):
		return self.get_body_params().get('Tightness')

	def set_Tightness(self,Tightness):
		self.add_body_params('Tightness', Tightness)