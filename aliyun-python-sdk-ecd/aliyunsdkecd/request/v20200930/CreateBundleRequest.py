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
from aliyunsdkecd.endpoint import endpoint_data

class CreateBundleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'CreateBundle')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RootDiskPerformanceLevel(self): # String
		return self.get_query_params().get('RootDiskPerformanceLevel')

	def set_RootDiskPerformanceLevel(self, RootDiskPerformanceLevel):  # String
		self.add_query_param('RootDiskPerformanceLevel', RootDiskPerformanceLevel)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Language(self): # String
		return self.get_query_params().get('Language')

	def set_Language(self, Language):  # String
		self.add_query_param('Language', Language)
	def get_UserDiskPerformanceLevel(self): # String
		return self.get_query_params().get('UserDiskPerformanceLevel')

	def set_UserDiskPerformanceLevel(self, UserDiskPerformanceLevel):  # String
		self.add_query_param('UserDiskPerformanceLevel', UserDiskPerformanceLevel)
	def get_DesktopType(self): # String
		return self.get_query_params().get('DesktopType')

	def set_DesktopType(self, DesktopType):  # String
		self.add_query_param('DesktopType', DesktopType)
	def get_BundleName(self): # String
		return self.get_query_params().get('BundleName')

	def set_BundleName(self, BundleName):  # String
		self.add_query_param('BundleName', BundleName)
	def get_UserDiskSizeGibs(self): # RepeatList
		return self.get_query_params().get('UserDiskSizeGib')

	def set_UserDiskSizeGibs(self, UserDiskSizeGib):  # RepeatList
		for depth1 in range(len(UserDiskSizeGib)):
			self.add_query_param('UserDiskSizeGib.' + str(depth1 + 1), UserDiskSizeGib[depth1])
	def get_RootDiskSizeGib(self): # Integer
		return self.get_query_params().get('RootDiskSizeGib')

	def set_RootDiskSizeGib(self, RootDiskSizeGib):  # Integer
		self.add_query_param('RootDiskSizeGib', RootDiskSizeGib)
