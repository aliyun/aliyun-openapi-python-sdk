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

class UploadImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'UploadImage')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EnableSecurityCheck(self): # Boolean
		return self.get_query_params().get('EnableSecurityCheck')

	def set_EnableSecurityCheck(self, EnableSecurityCheck):  # Boolean
		self.add_query_param('EnableSecurityCheck', EnableSecurityCheck)
	def get_GpuCategory(self): # Boolean
		return self.get_query_params().get('GpuCategory')

	def set_GpuCategory(self, GpuCategory):  # Boolean
		self.add_query_param('GpuCategory', GpuCategory)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_OssObjectPath(self): # String
		return self.get_query_params().get('OssObjectPath')

	def set_OssObjectPath(self, OssObjectPath):  # String
		self.add_query_param('OssObjectPath', OssObjectPath)
	def get_ImageName(self): # String
		return self.get_query_params().get('ImageName')

	def set_ImageName(self, ImageName):  # String
		self.add_query_param('ImageName', ImageName)
	def get_LicenseType(self): # String
		return self.get_query_params().get('LicenseType')

	def set_LicenseType(self, LicenseType):  # String
		self.add_query_param('LicenseType', LicenseType)
	def get_OsType(self): # String
		return self.get_query_params().get('OsType')

	def set_OsType(self, OsType):  # String
		self.add_query_param('OsType', OsType)
	def get_DataDiskSize(self): # Integer
		return self.get_query_params().get('DataDiskSize')

	def set_DataDiskSize(self, DataDiskSize):  # Integer
		self.add_query_param('DataDiskSize', DataDiskSize)
	def get_ProtocolType(self): # String
		return self.get_query_params().get('ProtocolType')

	def set_ProtocolType(self, ProtocolType):  # String
		self.add_query_param('ProtocolType', ProtocolType)
	def get_GpuDriverType(self): # String
		return self.get_query_params().get('GpuDriverType')

	def set_GpuDriverType(self, GpuDriverType):  # String
		self.add_query_param('GpuDriverType', GpuDriverType)
