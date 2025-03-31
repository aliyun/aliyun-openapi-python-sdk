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

class DescribeCloudSiemAssetsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'DescribeCloudSiemAssets','cloud-siem')
		self.set_method('POST')

	def get_RoleFor(self): # Long
		return self.get_body_params().get('RoleFor')

	def set_RoleFor(self, RoleFor):  # Long
		self.add_body_params('RoleFor', RoleFor)
	def get_AssetName(self): # String
		return self.get_body_params().get('AssetName')

	def set_AssetName(self, AssetName):  # String
		self.add_body_params('AssetName', AssetName)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_RoleType(self): # Integer
		return self.get_body_params().get('RoleType')

	def set_RoleType(self, RoleType):  # Integer
		self.add_body_params('RoleType', RoleType)
	def get_AssetType(self): # String
		return self.get_body_params().get('AssetType')

	def set_AssetType(self, AssetType):  # String
		self.add_body_params('AssetType', AssetType)
	def get_AssetUuid(self): # String
		return self.get_body_params().get('AssetUuid')

	def set_AssetUuid(self, AssetUuid):  # String
		self.add_body_params('AssetUuid', AssetUuid)
	def get_CurrentPage(self): # Integer
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_body_params('CurrentPage', CurrentPage)
	def get_IncidentUuid(self): # String
		return self.get_body_params().get('IncidentUuid')

	def set_IncidentUuid(self, IncidentUuid):  # String
		self.add_body_params('IncidentUuid', IncidentUuid)
