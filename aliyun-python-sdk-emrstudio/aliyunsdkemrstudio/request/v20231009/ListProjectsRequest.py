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

class ListProjectsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'EmrStudio', '2023-10-09', 'ListProjects')
		self.set_protocol_type('https')
		self.set_uri_pattern('/dolphinscheduler/v3/projects')
		self.set_method('GET')

	def get_searchVal(self): # String
		return self.get_query_params().get('searchVal')

	def set_searchVal(self, searchVal):  # String
		self.add_query_param('searchVal', searchVal)
	def get_nextToken(self): # String
		return self.get_query_params().get('nextToken')

	def set_nextToken(self, nextToken):  # String
		self.add_query_param('nextToken', nextToken)
	def get_maxResults(self): # Integer
		return self.get_query_params().get('maxResults')

	def set_maxResults(self, maxResults):  # Integer
		self.add_query_param('maxResults', maxResults)
	def get_workspaceId(self): # Long
		return self.get_query_params().get('workspaceId')

	def set_workspaceId(self, workspaceId):  # Long
		self.add_query_param('workspaceId', workspaceId)
