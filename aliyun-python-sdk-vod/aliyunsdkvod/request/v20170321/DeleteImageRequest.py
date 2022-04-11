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

class DeleteImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'DeleteImage','vod')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ImageURLs(self): # String
		return self.get_query_params().get('ImageURLs')

	def set_ImageURLs(self, ImageURLs):  # String
		self.add_query_param('ImageURLs', ImageURLs)
	def get_ImageType(self): # String
		return self.get_query_params().get('ImageType')

	def set_ImageType(self, ImageType):  # String
		self.add_query_param('ImageType', ImageType)
	def get_VideoId(self): # String
		return self.get_query_params().get('VideoId')

	def set_VideoId(self, VideoId):  # String
		self.add_query_param('VideoId', VideoId)
	def get_DeleteImageType(self): # String
		return self.get_query_params().get('DeleteImageType')

	def set_DeleteImageType(self, DeleteImageType):  # String
		self.add_query_param('DeleteImageType', DeleteImageType)
	def get_ImageIds(self): # String
		return self.get_query_params().get('ImageIds')

	def set_ImageIds(self, ImageIds):  # String
		self.add_query_param('ImageIds', ImageIds)
