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

class ListJobRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'foas', '2018-11-11', 'ListJob','foas')
		self.set_protocol_type('https')
		self.set_uri_pattern('/api/v2/projects/[projectName]/jobs')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_queueName(self):
		return self.get_query_params().get('queueName')

	def set_queueName(self,queueName):
		self.add_query_param('queueName',queueName)

	def get_projectName(self):
		return self.get_path_params().get('projectName')

	def set_projectName(self,projectName):
		self.add_path_param('projectName',projectName)

	def get_pageSize(self):
		return self.get_query_params().get('pageSize')

	def set_pageSize(self,pageSize):
		self.add_query_param('pageSize',pageSize)

	def get_isShowFullField(self):
		return self.get_query_params().get('isShowFullField')

	def set_isShowFullField(self,isShowFullField):
		self.add_query_param('isShowFullField',isShowFullField)

	def get_pageIndex(self):
		return self.get_query_params().get('pageIndex')

	def set_pageIndex(self,pageIndex):
		self.add_query_param('pageIndex',pageIndex)

	def get_engineVersion(self):
		return self.get_query_params().get('engineVersion')

	def set_engineVersion(self,engineVersion):
		self.add_query_param('engineVersion',engineVersion)

	def get_clusterId(self):
		return self.get_query_params().get('clusterId')

	def set_clusterId(self,clusterId):
		self.add_query_param('clusterId',clusterId)

	def get_jobType(self):
		return self.get_query_params().get('jobType')

	def set_jobType(self,jobType):
		self.add_query_param('jobType',jobType)

	def get_apiType(self):
		return self.get_query_params().get('apiType')

	def set_apiType(self,apiType):
		self.add_query_param('apiType',apiType)

	def get_jobName(self):
		return self.get_query_params().get('jobName')

	def set_jobName(self,jobName):
		self.add_query_param('jobName',jobName)

	def get_folderId(self):
		return self.get_query_params().get('folderId')

	def set_folderId(self,folderId):
		self.add_query_param('folderId',folderId)