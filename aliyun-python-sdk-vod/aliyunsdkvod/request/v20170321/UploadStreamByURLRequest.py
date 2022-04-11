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
from aliyunsdkvod.endpoint import endpoint_data

class UploadStreamByURLRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'UploadStreamByURL','vod')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FileExtension(self): # String
		return self.get_query_params().get('FileExtension')

	def set_FileExtension(self, FileExtension):  # String
		self.add_query_param('FileExtension', FileExtension)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_HDRType(self): # String
		return self.get_query_params().get('HDRType')

	def set_HDRType(self, HDRType):  # String
		self.add_query_param('HDRType', HDRType)
	def get_Definition(self): # String
		return self.get_query_params().get('Definition')

	def set_Definition(self, Definition):  # String
		self.add_query_param('Definition', Definition)
	def get_StreamURL(self): # String
		return self.get_query_params().get('StreamURL')

	def set_StreamURL(self, StreamURL):  # String
		self.add_query_param('StreamURL', StreamURL)
	def get_MediaId(self): # String
		return self.get_query_params().get('MediaId')

	def set_MediaId(self, MediaId):  # String
		self.add_query_param('MediaId', MediaId)
