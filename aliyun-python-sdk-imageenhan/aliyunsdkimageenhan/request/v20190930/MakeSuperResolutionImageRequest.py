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
from aliyunsdkimageenhan.endpoint import endpoint_data

class MakeSuperResolutionImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imageenhan', '2019-09-30', 'MakeSuperResolutionImage','imageenhan')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UpscaleFactor(self): # Long
		return self.get_body_params().get('UpscaleFactor')

	def set_UpscaleFactor(self, UpscaleFactor):  # Long
		self.add_body_params('UpscaleFactor', UpscaleFactor)
	def get_Mode(self): # String
		return self.get_body_params().get('Mode')

	def set_Mode(self, Mode):  # String
		self.add_body_params('Mode', Mode)
	def get_OutputFormat(self): # String
		return self.get_body_params().get('OutputFormat')

	def set_OutputFormat(self, OutputFormat):  # String
		self.add_body_params('OutputFormat', OutputFormat)
	def get_Url(self): # String
		return self.get_body_params().get('Url')

	def set_Url(self, Url):  # String
		self.add_body_params('Url', Url)
	def get_OutputQuality(self): # Long
		return self.get_body_params().get('OutputQuality')

	def set_OutputQuality(self, OutputQuality):  # Long
		self.add_body_params('OutputQuality', OutputQuality)
