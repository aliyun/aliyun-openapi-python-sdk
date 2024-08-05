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
from aliyunsdkarms.endpoint import endpoint_data
import json

class ListEnvironmentsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'ListEnvironments','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FilterRegionIds(self): # String
		return self.get_query_params().get('FilterRegionIds')

	def set_FilterRegionIds(self, FilterRegionIds):  # String
		self.add_query_param('FilterRegionIds', FilterRegionIds)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_AddonName(self): # String
		return self.get_query_params().get('AddonName')

	def set_AddonName(self, AddonName):  # String
		self.add_query_param('AddonName', AddonName)
	def get_EnvironmentType(self): # String
		return self.get_query_params().get('EnvironmentType')

	def set_EnvironmentType(self, EnvironmentType):  # String
		self.add_query_param('EnvironmentType', EnvironmentType)
	def get_Tag(self): # Array
		return self.get_query_params().get('Tag')

	def set_Tag(self, Tag):  # Array
		self.add_query_param("Tag", json.dumps(Tag))
	def get_BindResourceId(self): # String
		return self.get_query_params().get('BindResourceId')

	def set_BindResourceId(self, BindResourceId):  # String
		self.add_query_param('BindResourceId', BindResourceId)
	def get_FeePackage(self): # String
		return self.get_query_params().get('FeePackage')

	def set_FeePackage(self, FeePackage):  # String
		self.add_query_param('FeePackage', FeePackage)
