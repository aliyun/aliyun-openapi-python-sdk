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
import json

class DetectPedestrianIntrusionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'facebody', '2019-12-30', 'DetectPedestrianIntrusion','facebody')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DetectRegion(self): # Array
		return self.get_body_params().get('DetectRegion')

	def set_DetectRegion(self, DetectRegion):  # Array
		self.add_body_params("DetectRegion", json.dumps(DetectRegion))
	def get_RegionType(self): # String
		return self.get_body_params().get('RegionType')

	def set_RegionType(self, RegionType):  # String
		self.add_body_params('RegionType', RegionType)
	def get_ImageURL(self): # String
		return self.get_body_params().get('ImageURL')

	def set_ImageURL(self, ImageURL):  # String
		self.add_body_params('ImageURL', ImageURL)
