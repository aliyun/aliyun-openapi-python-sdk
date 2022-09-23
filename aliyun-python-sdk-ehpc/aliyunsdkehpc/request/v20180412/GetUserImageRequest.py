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
from aliyunsdkehpc.endpoint import endpoint_data

class GetUserImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'GetUserImage')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OSSBucket(self): # String
		return self.get_query_params().get('OSSBucket')

	def set_OSSBucket(self, OSSBucket):  # String
		self.add_query_param('OSSBucket', OSSBucket)
	def get_OSSEndPoint(self): # String
		return self.get_query_params().get('OSSEndPoint')

	def set_OSSEndPoint(self, OSSEndPoint):  # String
		self.add_query_param('OSSEndPoint', OSSEndPoint)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_ContainerType(self): # String
		return self.get_query_params().get('ContainerType')

	def set_ContainerType(self, ContainerType):  # String
		self.add_query_param('ContainerType', ContainerType)
	def get_ImagePath(self): # String
		return self.get_query_params().get('ImagePath')

	def set_ImagePath(self, ImagePath):  # String
		self.add_query_param('ImagePath', ImagePath)
	def get_ImageName(self): # String
		return self.get_query_params().get('ImageName')

	def set_ImageName(self, ImageName):  # String
		self.add_query_param('ImageName', ImageName)
