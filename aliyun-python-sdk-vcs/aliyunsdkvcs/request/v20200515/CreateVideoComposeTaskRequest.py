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
from aliyunsdkvcs.endpoint import endpoint_data

class CreateVideoComposeTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vcs', '2020-05-15', 'CreateVideoComposeTask','vcs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CorpId(self):
		return self.get_body_params().get('CorpId')

	def set_CorpId(self,CorpId):
		self.add_body_params('CorpId', CorpId)

	def get_DomainName(self):
		return self.get_body_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_body_params('DomainName', DomainName)

	def get_VideoFrameRate(self):
		return self.get_body_params().get('VideoFrameRate')

	def set_VideoFrameRate(self,VideoFrameRate):
		self.add_body_params('VideoFrameRate', VideoFrameRate)

	def get_ImageFileNames(self):
		return self.get_body_params().get('ImageFileNames')

	def set_ImageFileNames(self,ImageFileNames):
		self.add_body_params('ImageFileNames', ImageFileNames)

	def get_AudioFileName(self):
		return self.get_body_params().get('AudioFileName')

	def set_AudioFileName(self,AudioFileName):
		self.add_body_params('AudioFileName', AudioFileName)

	def get_BucketName(self):
		return self.get_body_params().get('BucketName')

	def set_BucketName(self,BucketName):
		self.add_body_params('BucketName', BucketName)

	def get_ImageParameters(self):
		return self.get_body_params().get('ImageParameters')

	def set_ImageParameters(self,ImageParameters):
		self.add_body_params('ImageParameters', ImageParameters)

	def get_VideoFormat(self):
		return self.get_body_params().get('VideoFormat')

	def set_VideoFormat(self,VideoFormat):
		self.add_body_params('VideoFormat', VideoFormat)