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

class CreateNodeTestRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateNodeTest','dide')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProjectEnv(self):
		return self.get_body_params().get('ProjectEnv')

	def set_ProjectEnv(self,ProjectEnv):
		self.add_body_params('ProjectEnv', ProjectEnv)

	def get_Parallelism(self):
		return self.get_body_params().get('Parallelism')

	def set_Parallelism(self,Parallelism):
		self.add_body_params('Parallelism', Parallelism)

	def get_BizBeginTime(self):
		return self.get_body_params().get('BizBeginTime')

	def set_BizBeginTime(self,BizBeginTime):
		self.add_body_params('BizBeginTime', BizBeginTime)

	def get_IncludeNodeIds(self):
		return self.get_body_params().get('IncludeNodeIds')

	def set_IncludeNodeIds(self,IncludeNodeIds):
		self.add_body_params('IncludeNodeIds', IncludeNodeIds)

	def get_Bizdate(self):
		return self.get_body_params().get('Bizdate')

	def set_Bizdate(self,Bizdate):
		self.add_body_params('Bizdate', Bizdate)

	def get_BizEndTime(self):
		return self.get_body_params().get('BizEndTime')

	def set_BizEndTime(self,BizEndTime):
		self.add_body_params('BizEndTime', BizEndTime)

	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)

	def get_ExcludeNodeIds(self):
		return self.get_body_params().get('ExcludeNodeIds')

	def set_ExcludeNodeIds(self,ExcludeNodeIds):
		self.add_body_params('ExcludeNodeIds', ExcludeNodeIds)

	def get_NodeId(self):
		return self.get_body_params().get('NodeId')

	def set_NodeId(self,NodeId):
		self.add_body_params('NodeId', NodeId)

	def get_NodeProjectId(self):
		return self.get_body_params().get('NodeProjectId')

	def set_NodeProjectId(self,NodeProjectId):
		self.add_body_params('NodeProjectId', NodeProjectId)