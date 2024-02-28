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

class ListNodesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'ListNodes')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Owner(self): # String
		return self.get_body_params().get('Owner')

	def set_Owner(self, Owner):  # String
		self.add_body_params('Owner', Owner)
	def get_ProjectEnv(self): # String
		return self.get_body_params().get('ProjectEnv')

	def set_ProjectEnv(self, ProjectEnv):  # String
		self.add_body_params('ProjectEnv', ProjectEnv)
	def get_BizName(self): # String
		return self.get_body_params().get('BizName')

	def set_BizName(self, BizName):  # String
		self.add_body_params('BizName', BizName)
	def get_PageNumber(self): # Integer
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_body_params('PageNumber', PageNumber)
	def get_NodeName(self): # String
		return self.get_body_params().get('NodeName')

	def set_NodeName(self, NodeName):  # String
		self.add_body_params('NodeName', NodeName)
	def get_ProgramType(self): # String
		return self.get_body_params().get('ProgramType')

	def set_ProgramType(self, ProgramType):  # String
		self.add_body_params('ProgramType', ProgramType)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_SchedulerType(self): # String
		return self.get_body_params().get('SchedulerType')

	def set_SchedulerType(self, SchedulerType):  # String
		self.add_body_params('SchedulerType', SchedulerType)
	def get_ProjectId(self): # Long
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_body_params('ProjectId', ProjectId)
