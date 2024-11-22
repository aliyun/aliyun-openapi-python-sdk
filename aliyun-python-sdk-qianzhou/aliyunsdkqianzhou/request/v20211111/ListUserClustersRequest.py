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

class ListUserClustersRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'qianzhou', '2021-11-11', 'ListUserClusters')
		self.set_uri_pattern('/popapi/listUserClusters')
		self.set_method('GET')

	def get_current(self): # String
		return self.get_query_params().get('current')

	def set_current(self, current):  # String
		self.add_query_param('current', current)
	def get_pageSize(self): # String
		return self.get_query_params().get('pageSize')

	def set_pageSize(self, pageSize):  # String
		self.add_query_param('pageSize', pageSize)
	def get_userID(self): # String
		return self.get_query_params().get('userID')

	def set_userID(self, userID):  # String
		self.add_query_param('userID', userID)
