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
from aliyunsdksas.endpoint import endpoint_data
import json

class DescribeImageListBySensitiveFileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeImageListBySensitiveFile','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SensitiveFileKey(self): # String
		return self.get_query_params().get('SensitiveFileKey')

	def set_SensitiveFileKey(self, SensitiveFileKey):  # String
		self.add_query_param('SensitiveFileKey', SensitiveFileKey)
	def get_RepoNamespace(self): # String
		return self.get_query_params().get('RepoNamespace')

	def set_RepoNamespace(self, RepoNamespace):  # String
		self.add_query_param('RepoNamespace', RepoNamespace)
	def get_ImageDigest(self): # String
		return self.get_query_params().get('ImageDigest')

	def set_ImageDigest(self, ImageDigest):  # String
		self.add_query_param('ImageDigest', ImageDigest)
	def get_ScanRange(self): # Array
		return self.get_query_params().get('ScanRange')

	def set_ScanRange(self, ScanRange):  # Array
		self.add_query_param("ScanRange", json.dumps(ScanRange))
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_RiskLevel(self): # String
		return self.get_query_params().get('RiskLevel')

	def set_RiskLevel(self, RiskLevel):  # String
		self.add_query_param('RiskLevel', RiskLevel)
	def get_RepoName(self): # String
		return self.get_query_params().get('RepoName')

	def set_RepoName(self, RepoName):  # String
		self.add_query_param('RepoName', RepoName)
	def get_RepoInstanceId(self): # String
		return self.get_query_params().get('RepoInstanceId')

	def set_RepoInstanceId(self, RepoInstanceId):  # String
		self.add_query_param('RepoInstanceId', RepoInstanceId)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
