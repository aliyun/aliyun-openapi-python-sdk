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
from aliyunsdkopensearch.endpoint import endpoint_data

class ListAppGroupErrorsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'OpenSearch', '2017-12-25', 'ListAppGroupErrors','opensearch')
		self.set_uri_pattern('/v4/openapi/app-groups/[appGroupIdentity]/errors')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_appId(self):
		return self.get_query_params().get('appId')

	def set_appId(self,appId):
		self.add_query_param('appId',appId)

	def get_pageSize(self):
		return self.get_query_params().get('pageSize')

	def set_pageSize(self,pageSize):
		self.add_query_param('pageSize',pageSize)

	def get_startTime(self):
		return self.get_query_params().get('startTime')

	def set_startTime(self,startTime):
		self.add_query_param('startTime',startTime)

	def get_stopTime(self):
		return self.get_query_params().get('stopTime')

	def set_stopTime(self,stopTime):
		self.add_query_param('stopTime',stopTime)

	def get_appGroupIdentity(self):
		return self.get_path_params().get('appGroupIdentity')

	def set_appGroupIdentity(self,appGroupIdentity):
		self.add_path_param('appGroupIdentity',appGroupIdentity)

	def get_pageNumber(self):
		return self.get_query_params().get('pageNumber')

	def set_pageNumber(self,pageNumber):
		self.add_query_param('pageNumber',pageNumber)