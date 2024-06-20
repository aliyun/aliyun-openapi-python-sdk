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

class CreateWmExtractTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'CreateWmExtractTask')
		self.set_method('POST')

	def get_VideoIsLong(self): # Boolean
		return self.get_body_params().get('VideoIsLong')

	def set_VideoIsLong(self, VideoIsLong):  # Boolean
		self.add_body_params('VideoIsLong', VideoIsLong)
	def get_DocumentIsCapture(self): # Boolean
		return self.get_body_params().get('DocumentIsCapture')

	def set_DocumentIsCapture(self, DocumentIsCapture):  # Boolean
		self.add_body_params('DocumentIsCapture', DocumentIsCapture)
	def get_VideoSpeed(self): # String
		return self.get_body_params().get('VideoSpeed')

	def set_VideoSpeed(self, VideoSpeed):  # String
		self.add_body_params('VideoSpeed', VideoSpeed)
	def get_WmType(self): # String
		return self.get_body_params().get('WmType')

	def set_WmType(self, WmType):  # String
		self.add_body_params('WmType', WmType)
	def get_Filename(self): # String
		return self.get_body_params().get('Filename')

	def set_Filename(self, Filename):  # String
		self.add_body_params('Filename', Filename)
	def get_WmInfoSize(self): # Long
		return self.get_body_params().get('WmInfoSize')

	def set_WmInfoSize(self, WmInfoSize):  # Long
		self.add_body_params('WmInfoSize', WmInfoSize)
	def get_FileUrl(self): # String
		return self.get_body_params().get('FileUrl')

	def set_FileUrl(self, FileUrl):  # String
		self.add_body_params('FileUrl', FileUrl)
