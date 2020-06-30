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
from aliyunsdkpts.endpoint import endpoint_data

class UploadPtsFileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'PTS', '2019-08-10', 'UploadPtsFile','1.0.0')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Extension(self):
		return self.get_query_params().get('Extension')

	def set_Extension(self,Extension):
		self.add_query_param('Extension',Extension)

	def get_FileName(self):
		return self.get_query_params().get('FileName')

	def set_FileName(self,FileName):
		self.add_query_param('FileName',FileName)

	def get_OssUrl(self):
		return self.get_query_params().get('OssUrl')

	def set_OssUrl(self,OssUrl):
		self.add_query_param('OssUrl',OssUrl)

	def get_UploadExtraInfo(self):
		return self.get_query_params().get('UploadExtraInfo')

	def set_UploadExtraInfo(self,UploadExtraInfo):
		self.add_query_param('UploadExtraInfo',UploadExtraInfo)

	def get_UploadType(self):
		return self.get_query_params().get('UploadType')

	def set_UploadType(self,UploadType):
		self.add_query_param('UploadType',UploadType)