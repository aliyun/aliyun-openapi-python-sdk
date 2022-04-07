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

class ListDeploymentsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'ListDeployments')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Creator(self): # String
		return self.get_body_params().get('Creator')

	def set_Creator(self, Creator):  # String
		self.add_body_params('Creator', Creator)
	def get_EndCreateTime(self): # Long
		return self.get_body_params().get('EndCreateTime')

	def set_EndCreateTime(self, EndCreateTime):  # Long
		self.add_body_params('EndCreateTime', EndCreateTime)
	def get_ProjectIdentifier(self): # String
		return self.get_body_params().get('ProjectIdentifier')

	def set_ProjectIdentifier(self, ProjectIdentifier):  # String
		self.add_body_params('ProjectIdentifier', ProjectIdentifier)
	def get_PageNumber(self): # Integer
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_body_params('PageNumber', PageNumber)
	def get_Executor(self): # String
		return self.get_body_params().get('Executor')

	def set_Executor(self, Executor):  # String
		self.add_body_params('Executor', Executor)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_EndExecuteTime(self): # Long
		return self.get_body_params().get('EndExecuteTime')

	def set_EndExecuteTime(self, EndExecuteTime):  # Long
		self.add_body_params('EndExecuteTime', EndExecuteTime)
	def get_Keyword(self): # String
		return self.get_body_params().get('Keyword')

	def set_Keyword(self, Keyword):  # String
		self.add_body_params('Keyword', Keyword)
	def get_ProjectId(self): # Long
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_body_params('ProjectId', ProjectId)
	def get_Status(self): # Integer
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_body_params('Status', Status)
