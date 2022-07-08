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
from aliyunsdkactiontrail.endpoint import endpoint_data

class DescribeTrailsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Actiontrail', '2020-07-06', 'DescribeTrails')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IncludeOrganizationTrail(self): # Boolean
		return self.get_query_params().get('IncludeOrganizationTrail')

	def set_IncludeOrganizationTrail(self, IncludeOrganizationTrail):  # Boolean
		self.add_query_param('IncludeOrganizationTrail', IncludeOrganizationTrail)
	def get_IncludeShadowTrails(self): # Boolean
		return self.get_query_params().get('IncludeShadowTrails')

	def set_IncludeShadowTrails(self, IncludeShadowTrails):  # Boolean
		self.add_query_param('IncludeShadowTrails', IncludeShadowTrails)
	def get_NameList(self): # String
		return self.get_query_params().get('NameList')

	def set_NameList(self, NameList):  # String
		self.add_query_param('NameList', NameList)
