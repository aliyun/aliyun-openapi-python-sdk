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

class ImportImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'ImportImage','ens')
		self.set_method('POST')

	def get_ComputeType(self): # String
		return self.get_query_params().get('ComputeType')

	def set_ComputeType(self, ComputeType):  # String
		self.add_query_param('ComputeType', ComputeType)
	def get_OSSBucket(self): # String
		return self.get_query_params().get('OSSBucket')

	def set_OSSBucket(self, OSSBucket):  # String
		self.add_query_param('OSSBucket', OSSBucket)
	def get_OSVersion(self): # String
		return self.get_query_params().get('OSVersion')

	def set_OSVersion(self, OSVersion):  # String
		self.add_query_param('OSVersion', OSVersion)
	def get_DiskDeviceMapping(self): # String
		return self.get_query_params().get('DiskDeviceMapping')

	def set_DiskDeviceMapping(self, DiskDeviceMapping):  # String
		self.add_query_param('DiskDeviceMapping', DiskDeviceMapping)
	def get_OSSRegion(self): # String
		return self.get_query_params().get('OSSRegion')

	def set_OSSRegion(self, OSSRegion):  # String
		self.add_query_param('OSSRegion', OSSRegion)
	def get_OSSObject(self): # String
		return self.get_query_params().get('OSSObject')

	def set_OSSObject(self, OSSObject):  # String
		self.add_query_param('OSSObject', OSSObject)
	def get_Platform(self): # String
		return self.get_query_params().get('Platform')

	def set_Platform(self, Platform):  # String
		self.add_query_param('Platform', Platform)
	def get_ImageName(self): # String
		return self.get_query_params().get('ImageName')

	def set_ImageName(self, ImageName):  # String
		self.add_query_param('ImageName', ImageName)
	def get_ImageFormat(self): # String
		return self.get_query_params().get('ImageFormat')

	def set_ImageFormat(self, ImageFormat):  # String
		self.add_query_param('ImageFormat', ImageFormat)
	def get_Architecture(self): # String
		return self.get_query_params().get('Architecture')

	def set_Architecture(self, Architecture):  # String
		self.add_query_param('Architecture', Architecture)
	def get_OSType(self): # String
		return self.get_query_params().get('OSType')

	def set_OSType(self, OSType):  # String
		self.add_query_param('OSType', OSType)
	def get_TargetOSSRegionId(self): # String
		return self.get_query_params().get('TargetOSSRegionId')

	def set_TargetOSSRegionId(self, TargetOSSRegionId):  # String
		self.add_query_param('TargetOSSRegionId', TargetOSSRegionId)
