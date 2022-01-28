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

class ListApplicationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'ListApplications','ens')
		self.set_method('POST')

	def get_ClusterNames(self): # String
		return self.get_query_params().get('ClusterNames')

	def set_ClusterNames(self, ClusterNames):  # String
		self.add_query_param('ClusterNames', ClusterNames)
	def get_Level(self): # String
		return self.get_query_params().get('Level')

	def set_Level(self, Level):  # String
		self.add_query_param('Level', Level)
	def get_OutAppInfoParams(self): # String
		return self.get_query_params().get('OutAppInfoParams')

	def set_OutAppInfoParams(self, OutAppInfoParams):  # String
		self.add_query_param('OutAppInfoParams', OutAppInfoParams)
	def get_MaxDate(self): # String
		return self.get_query_params().get('MaxDate')

	def set_MaxDate(self, MaxDate):  # String
		self.add_query_param('MaxDate', MaxDate)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_AppVersions(self): # String
		return self.get_query_params().get('AppVersions')

	def set_AppVersions(self, AppVersions):  # String
		self.add_query_param('AppVersions', AppVersions)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_MinDate(self): # String
		return self.get_query_params().get('MinDate')

	def set_MinDate(self, MinDate):  # String
		self.add_query_param('MinDate', MinDate)
