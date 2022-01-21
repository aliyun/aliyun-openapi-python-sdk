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
from aliyunsdkdts.endpoint import endpoint_data

class SkipPreCheckRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'SkipPreCheck','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SkipPreCheckItems(self): # String
		return self.get_query_params().get('SkipPreCheckItems')

	def set_SkipPreCheckItems(self, SkipPreCheckItems):  # String
		self.add_query_param('SkipPreCheckItems', SkipPreCheckItems)
	def get_Skip(self): # Boolean
		return self.get_query_params().get('Skip')

	def set_Skip(self, Skip):  # Boolean
		self.add_query_param('Skip', Skip)
	def get_JobId(self): # String
		return self.get_query_params().get('JobId')

	def set_JobId(self, JobId):  # String
		self.add_query_param('JobId', JobId)
	def get_SkipPreCheckNames(self): # String
		return self.get_query_params().get('SkipPreCheckNames')

	def set_SkipPreCheckNames(self, SkipPreCheckNames):  # String
		self.add_query_param('SkipPreCheckNames', SkipPreCheckNames)
	def get_DtsJobId(self): # String
		return self.get_query_params().get('DtsJobId')

	def set_DtsJobId(self, DtsJobId):  # String
		self.add_query_param('DtsJobId', DtsJobId)
