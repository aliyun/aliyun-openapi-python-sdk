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
from aliyunsdkobjectdet.endpoint import endpoint_data

class DetectWorkwearRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'objectdet', '2019-12-30', 'DetectWorkwear','objectdet')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Clothes(self):
		return self.get_body_params().get('Clothes')

	def set_Clothes(self,Clothes):
		self.add_body_params('Clothes', Clothes)

	def get_Labelss(self):
		return self.get_body_params().get('Labels')

	def set_Labelss(self, Labelss):
		for depth1 in range(len(Labelss)):
			if Labelss[depth1] is not None:
				self.add_body_params('Labels.' + str(depth1 + 1) , Labelss[depth1])

	def get_ImageUrl(self):
		return self.get_body_params().get('ImageUrl')

	def set_ImageUrl(self,ImageUrl):
		self.add_body_params('ImageUrl', ImageUrl)