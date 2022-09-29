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
import json

class DetectVideoFrameRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'objectdet', '2019-12-30', 'DetectVideoFrame')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Features(self): # Array
		return self.get_body_params().get('Features')

	def set_Features(self, Features):  # Array
		self.add_body_params("Features", json.dumps(Features))
	def get_Height(self): # Long
		return self.get_body_params().get('Height')

	def set_Height(self, Height):  # Long
		self.add_body_params('Height', Height)
	def get_CreateTime(self): # Long
		return self.get_body_params().get('CreateTime')

	def set_CreateTime(self, CreateTime):  # Long
		self.add_body_params('CreateTime', CreateTime)
	def get_FeatureConfig(self): # String
		return self.get_body_params().get('FeatureConfig')

	def set_FeatureConfig(self, FeatureConfig):  # String
		self.add_body_params('FeatureConfig', FeatureConfig)
	def get_OwnerId(self): # Long
		return self.get_body_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_body_params('OwnerId', OwnerId)
	def get_StreamArn(self): # String
		return self.get_body_params().get('StreamArn')

	def set_StreamArn(self, StreamArn):  # String
		self.add_body_params('StreamArn', StreamArn)
	def get_ImageURL(self): # String
		return self.get_body_params().get('ImageURL')

	def set_ImageURL(self, ImageURL):  # String
		self.add_body_params('ImageURL', ImageURL)
	def get_Width(self): # Long
		return self.get_body_params().get('Width')

	def set_Width(self, Width):  # Long
		self.add_body_params('Width', Width)
