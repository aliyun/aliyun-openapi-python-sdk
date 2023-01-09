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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkedas.endpoint import endpoint_data

class InsertOrUpdateRegionRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'InsertOrUpdateRegion','Edas')
		self.set_uri_pattern('/pop/v5/user_region_def')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RegistryType(self): # String
		return self.get_query_params().get('RegistryType')

	def set_RegistryType(self, RegistryType):  # String
		self.add_query_param('RegistryType', RegistryType)
	def get_DebugEnable(self): # Boolean
		return self.get_query_params().get('DebugEnable')

	def set_DebugEnable(self, DebugEnable):  # Boolean
		self.add_query_param('DebugEnable', DebugEnable)
	def get_RegionTag(self): # String
		return self.get_query_params().get('RegionTag')

	def set_RegionTag(self, RegionTag):  # String
		self.add_query_param('RegionTag', RegionTag)
	def get_RegionName(self): # String
		return self.get_query_params().get('RegionName')

	def set_RegionName(self, RegionName):  # String
		self.add_query_param('RegionName', RegionName)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_MseInstanceId(self): # String
		return self.get_query_params().get('MseInstanceId')

	def set_MseInstanceId(self, MseInstanceId):  # String
		self.add_query_param('MseInstanceId', MseInstanceId)
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
