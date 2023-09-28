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
from aliyunsdkmaxcompute.endpoint import endpoint_data

class ListUsersRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'MaxCompute', '2022-01-04', 'ListUsers')
		self.set_uri_pattern('/api/v1/users')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_pageSize(self): # Integer
		return self.get_query_params().get('pageSize')

	def set_pageSize(self, pageSize):  # Integer
		self.add_query_param('pageSize', pageSize)
	def get_pageNumber(self): # Integer
		return self.get_query_params().get('pageNumber')

	def set_pageNumber(self, pageNumber):  # Integer
		self.add_query_param('pageNumber', pageNumber)
