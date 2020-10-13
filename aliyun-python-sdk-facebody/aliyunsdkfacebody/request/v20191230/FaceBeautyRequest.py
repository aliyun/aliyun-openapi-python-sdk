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

class FaceBeautyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'facebody', '2019-12-30', 'FaceBeauty','facebody')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Sharp(self):
		return self.get_body_params().get('Sharp')

	def set_Sharp(self,Sharp):
		self.add_body_params('Sharp', Sharp)

	def get_White(self):
		return self.get_body_params().get('White')

	def set_White(self,White):
		self.add_body_params('White', White)

	def get_ImageURL(self):
		return self.get_body_params().get('ImageURL')

	def set_ImageURL(self,ImageURL):
		self.add_body_params('ImageURL', ImageURL)

	def get_Smooth(self):
		return self.get_body_params().get('Smooth')

	def set_Smooth(self,Smooth):
		self.add_body_params('Smooth', Smooth)