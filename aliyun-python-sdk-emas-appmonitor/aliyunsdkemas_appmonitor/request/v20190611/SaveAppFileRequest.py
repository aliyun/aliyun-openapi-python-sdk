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
from aliyunsdkemas_appmonitor.endpoint import endpoint_data

class SaveAppFileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'emas-appmonitor', '2019-06-11', 'SaveAppFile')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_FileType(self):
		return self.get_body_params().get('FileType')

	def set_FileType(self,FileType):
		self.add_body_params('FileType', FileType)

	def get_FilePath(self):
		return self.get_body_params().get('FilePath')

	def set_FilePath(self,FilePath):
		self.add_body_params('FilePath', FilePath)

	def get_UniqueAppId(self):
		return self.get_body_params().get('UniqueAppId')

	def set_UniqueAppId(self,UniqueAppId):
		self.add_body_params('UniqueAppId', UniqueAppId)

	def get_AppVersion(self):
		return self.get_body_params().get('AppVersion')

	def set_AppVersion(self,AppVersion):
		self.add_body_params('AppVersion', AppVersion)

	def get_FileName(self):
		return self.get_body_params().get('FileName')

	def set_FileName(self,FileName):
		self.add_body_params('FileName', FileName)