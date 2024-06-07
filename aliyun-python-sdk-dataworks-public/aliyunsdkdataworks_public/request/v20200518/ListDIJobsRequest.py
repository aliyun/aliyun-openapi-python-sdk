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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class ListDIJobsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'ListDIJobs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SourceDataSourceType(self): # String
		return self.get_body_params().get('SourceDataSourceType')

	def set_SourceDataSourceType(self, SourceDataSourceType):  # String
		self.add_body_params('SourceDataSourceType', SourceDataSourceType)
	def get_PageNumber(self): # Integer
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_body_params('PageNumber', PageNumber)
	def get_DestinationDataSourceType(self): # String
		return self.get_body_params().get('DestinationDataSourceType')

	def set_DestinationDataSourceType(self, DestinationDataSourceType):  # String
		self.add_body_params('DestinationDataSourceType', DestinationDataSourceType)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_ProjectId(self): # Long
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_body_params('ProjectId', ProjectId)
	def get_JobName(self): # String
		return self.get_body_params().get('JobName')

	def set_JobName(self, JobName):  # String
		self.add_body_params('JobName', JobName)
