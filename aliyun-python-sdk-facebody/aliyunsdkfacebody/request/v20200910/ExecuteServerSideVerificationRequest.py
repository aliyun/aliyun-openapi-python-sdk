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

class ExecuteServerSideVerificationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'facebody', '2020-09-10', 'ExecuteServerSideVerification','facebody')
		self.set_uri_pattern('/viapi/thirdparty/realperson/execServerSideVerification')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_facialPictureData(self): # String
		return self.get_body_params().get('facialPictureData')

	def set_facialPictureData(self, facialPictureData):  # String
		self.add_body_params('facialPictureData', facialPictureData)
	def get_sceneType(self): # String
		return self.get_body_params().get('sceneType')

	def set_sceneType(self, sceneType):  # String
		self.add_body_params('sceneType', sceneType)
	def get_certificateNumber(self): # String
		return self.get_body_params().get('certificateNumber')

	def set_certificateNumber(self, certificateNumber):  # String
		self.add_body_params('certificateNumber', certificateNumber)
	def get_certificateName(self): # String
		return self.get_body_params().get('certificateName')

	def set_certificateName(self, certificateName):  # String
		self.add_body_params('certificateName', certificateName)
	def get_facialPictureUrl(self): # String
		return self.get_body_params().get('facialPictureUrl')

	def set_facialPictureUrl(self, facialPictureUrl):  # String
		self.add_body_params('facialPictureUrl', facialPictureUrl)
