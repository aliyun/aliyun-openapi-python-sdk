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
from aliyunsdkfoas.endpoint import endpoint_data

class ListInstanceRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'foas', '2018-11-11', 'ListInstance','foas')
		self.set_protocol_type('https')
		self.set_uri_pattern('/api/v2/projects/[projectName]/instances')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_projectName(self):
		return self.get_path_params().get('projectName')

	def set_projectName(self,projectName):
		self.add_path_param('projectName',projectName)

	def get_endBeginTs(self):
		return self.get_query_params().get('endBeginTs')

	def set_endBeginTs(self,endBeginTs):
		self.add_query_param('endBeginTs',endBeginTs)

	def get_expectState(self):
		return self.get_query_params().get('expectState')

	def set_expectState(self,expectState):
		self.add_query_param('expectState',expectState)

	def get_jobType(self):
		return self.get_query_params().get('jobType')

	def set_jobType(self,jobType):
		self.add_query_param('jobType',jobType)

	def get_apiType(self):
		return self.get_query_params().get('apiType')

	def set_apiType(self,apiType):
		self.add_query_param('apiType',apiType)

	def get_actualState(self):
		return self.get_query_params().get('actualState')

	def set_actualState(self,actualState):
		self.add_query_param('actualState',actualState)

	def get_endEndTs(self):
		return self.get_query_params().get('endEndTs')

	def set_endEndTs(self,endEndTs):
		self.add_query_param('endEndTs',endEndTs)

	def get_startEndTs(self):
		return self.get_query_params().get('startEndTs')

	def set_startEndTs(self,startEndTs):
		self.add_query_param('startEndTs',startEndTs)

	def get_pageSize(self):
		return self.get_query_params().get('pageSize')

	def set_pageSize(self,pageSize):
		self.add_query_param('pageSize',pageSize)

	def get_startBeginTs(self):
		return self.get_query_params().get('startBeginTs')

	def set_startBeginTs(self,startBeginTs):
		self.add_query_param('startBeginTs',startBeginTs)

	def get_pageIndex(self):
		return self.get_query_params().get('pageIndex')

	def set_pageIndex(self,pageIndex):
		self.add_query_param('pageIndex',pageIndex)

	def get_isArchived(self):
		return self.get_query_params().get('isArchived')

	def set_isArchived(self,isArchived):
		self.add_query_param('isArchived',isArchived)

	def get_jobName(self):
		return self.get_query_params().get('jobName')

	def set_jobName(self,jobName):
		self.add_query_param('jobName',jobName)