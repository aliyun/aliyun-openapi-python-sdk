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
from aliyunsdkcloudauth.endpoint import endpoint_data

class DeepfakeDetectRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2019-03-07', 'DeepfakeDetect','cloudauth')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FaceBase64(self): # String
		return self.get_body_params().get('FaceBase64')

	def set_FaceBase64(self, FaceBase64):  # String
		self.add_body_params('FaceBase64', FaceBase64)
	def get_OuterOrderNo(self): # String
		return self.get_query_params().get('OuterOrderNo')

	def set_OuterOrderNo(self, OuterOrderNo):  # String
		self.add_query_param('OuterOrderNo', OuterOrderNo)
	def get_FaceUrl(self): # String
		return self.get_query_params().get('FaceUrl')

	def set_FaceUrl(self, FaceUrl):  # String
		self.add_query_param('FaceUrl', FaceUrl)
	def get_FaceInputType(self): # String
		return self.get_query_params().get('FaceInputType')

	def set_FaceInputType(self, FaceInputType):  # String
		self.add_query_param('FaceInputType', FaceInputType)
