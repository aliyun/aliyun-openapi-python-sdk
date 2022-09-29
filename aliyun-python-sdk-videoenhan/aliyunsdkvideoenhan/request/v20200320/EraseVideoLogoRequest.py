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

class EraseVideoLogoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'videoenhan', '2020-03-20', 'EraseVideoLogo','videoenhan')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Boxess(self): # RepeatList
		return self.get_body_params().get('Boxes')

	def set_Boxess(self, Boxes):  # RepeatList
		for depth1 in range(len(Boxes)):
			if Boxes[depth1].get('W') is not None:
				self.add_body_params('Boxes.' + str(depth1 + 1) + '.W', Boxes[depth1].get('W'))
			if Boxes[depth1].get('H') is not None:
				self.add_body_params('Boxes.' + str(depth1 + 1) + '.H', Boxes[depth1].get('H'))
			if Boxes[depth1].get('X') is not None:
				self.add_body_params('Boxes.' + str(depth1 + 1) + '.X', Boxes[depth1].get('X'))
			if Boxes[depth1].get('Y') is not None:
				self.add_body_params('Boxes.' + str(depth1 + 1) + '.Y', Boxes[depth1].get('Y'))
	def get_VideoUrl(self): # String
		return self.get_body_params().get('VideoUrl')

	def set_VideoUrl(self, VideoUrl):  # String
		self.add_body_params('VideoUrl', VideoUrl)
