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
from aliyunsdknas.endpoint import endpoint_data

class CreateAccessPointRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'CreateAccessPoint','nas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_VswId(self): # String
		return self.get_query_params().get('VswId')

	def set_VswId(self, VswId):  # String
		self.add_query_param('VswId', VswId)
	def get_AccessPointName(self): # String
		return self.get_query_params().get('AccessPointName')

	def set_AccessPointName(self, AccessPointName):  # String
		self.add_query_param('AccessPointName', AccessPointName)
	def get_PosixGroupId(self): # Integer
		return self.get_query_params().get('PosixGroupId')

	def set_PosixGroupId(self, PosixGroupId):  # Integer
		self.add_query_param('PosixGroupId', PosixGroupId)
	def get_PosixSecondaryGroupIds(self): # String
		return self.get_query_params().get('PosixSecondaryGroupIds')

	def set_PosixSecondaryGroupIds(self, PosixSecondaryGroupIds):  # String
		self.add_query_param('PosixSecondaryGroupIds', PosixSecondaryGroupIds)
	def get_FileSystemId(self): # String
		return self.get_query_params().get('FileSystemId')

	def set_FileSystemId(self, FileSystemId):  # String
		self.add_query_param('FileSystemId', FileSystemId)
	def get_OwnerGroupId(self): # Integer
		return self.get_query_params().get('OwnerGroupId')

	def set_OwnerGroupId(self, OwnerGroupId):  # Integer
		self.add_query_param('OwnerGroupId', OwnerGroupId)
	def get_EnabledRam(self): # Boolean
		return self.get_query_params().get('EnabledRam')

	def set_EnabledRam(self, EnabledRam):  # Boolean
		self.add_query_param('EnabledRam', EnabledRam)
	def get_OwnerUserId(self): # Integer
		return self.get_query_params().get('OwnerUserId')

	def set_OwnerUserId(self, OwnerUserId):  # Integer
		self.add_query_param('OwnerUserId', OwnerUserId)
	def get_Permission(self): # String
		return self.get_query_params().get('Permission')

	def set_Permission(self, Permission):  # String
		self.add_query_param('Permission', Permission)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_RootDirectory(self): # String
		return self.get_query_params().get('RootDirectory')

	def set_RootDirectory(self, RootDirectory):  # String
		self.add_query_param('RootDirectory', RootDirectory)
	def get_AccessGroup(self): # String
		return self.get_query_params().get('AccessGroup')

	def set_AccessGroup(self, AccessGroup):  # String
		self.add_query_param('AccessGroup', AccessGroup)
	def get_PosixUserId(self): # Integer
		return self.get_query_params().get('PosixUserId')

	def set_PosixUserId(self, PosixUserId):  # Integer
		self.add_query_param('PosixUserId', PosixUserId)
