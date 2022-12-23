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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkfacebody.endpoint import endpoint_data

class DetectIPCPedestrianOptimizedRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'facebody', '2020-09-10', 'DetectIPCPedestrianOptimized','facebody')
		self.set_uri_pattern('/viapi/k8s/facebody/detect-ipc-pedestrian-optimized')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_height(self): # Long
		return self.get_body_params().get('height')

	def set_height(self, height):  # Long
		self.add_body_params('height', height)
	def get_imageData(self): # String
		return self.get_body_params().get('imageData')

	def set_imageData(self, imageData):  # String
		self.add_body_params('imageData', imageData)
	def get_width(self): # Long
		return self.get_body_params().get('width')

	def set_width(self, width):  # Long
		self.add_body_params('width', width)
