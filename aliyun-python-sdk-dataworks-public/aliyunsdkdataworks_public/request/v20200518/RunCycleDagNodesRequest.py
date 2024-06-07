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

class RunCycleDagNodesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'RunCycleDagNodes')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProjectEnv(self): # String
		return self.get_body_params().get('ProjectEnv')

	def set_ProjectEnv(self, ProjectEnv):  # String
		self.add_body_params('ProjectEnv', ProjectEnv)
	def get_StartBizDate(self): # String
		return self.get_body_params().get('StartBizDate')

	def set_StartBizDate(self, StartBizDate):  # String
		self.add_body_params('StartBizDate', StartBizDate)
	def get_Parallelism(self): # Boolean
		return self.get_body_params().get('Parallelism')

	def set_Parallelism(self, Parallelism):  # Boolean
		self.add_body_params('Parallelism', Parallelism)
	def get_AlertNoticeType(self): # String
		return self.get_body_params().get('AlertNoticeType')

	def set_AlertNoticeType(self, AlertNoticeType):  # String
		self.add_body_params('AlertNoticeType', AlertNoticeType)
	def get_RootNodeId(self): # Long
		return self.get_body_params().get('RootNodeId')

	def set_RootNodeId(self, RootNodeId):  # Long
		self.add_body_params('RootNodeId', RootNodeId)
	def get_BizBeginTime(self): # String
		return self.get_body_params().get('BizBeginTime')

	def set_BizBeginTime(self, BizBeginTime):  # String
		self.add_body_params('BizBeginTime', BizBeginTime)
	def get_EndBizDate(self): # String
		return self.get_body_params().get('EndBizDate')

	def set_EndBizDate(self, EndBizDate):  # String
		self.add_body_params('EndBizDate', EndBizDate)
	def get_StartFutureInstanceImmediately(self): # Boolean
		return self.get_body_params().get('StartFutureInstanceImmediately')

	def set_StartFutureInstanceImmediately(self, StartFutureInstanceImmediately):  # Boolean
		self.add_body_params('StartFutureInstanceImmediately', StartFutureInstanceImmediately)
	def get_ConcurrentRuns(self): # Integer
		return self.get_body_params().get('ConcurrentRuns')

	def set_ConcurrentRuns(self, ConcurrentRuns):  # Integer
		self.add_body_params('ConcurrentRuns', ConcurrentRuns)
	def get_AlertType(self): # String
		return self.get_body_params().get('AlertType')

	def set_AlertType(self, AlertType):  # String
		self.add_body_params('AlertType', AlertType)
	def get_IncludeNodeIds(self): # String
		return self.get_body_params().get('IncludeNodeIds')

	def set_IncludeNodeIds(self, IncludeNodeIds):  # String
		self.add_body_params('IncludeNodeIds', IncludeNodeIds)
	def get_BizEndTime(self): # String
		return self.get_body_params().get('BizEndTime')

	def set_BizEndTime(self, BizEndTime):  # String
		self.add_body_params('BizEndTime', BizEndTime)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_ExcludeNodeIds(self): # String
		return self.get_body_params().get('ExcludeNodeIds')

	def set_ExcludeNodeIds(self, ExcludeNodeIds):  # String
		self.add_body_params('ExcludeNodeIds', ExcludeNodeIds)
	def get_NodeParams(self): # String
		return self.get_body_params().get('NodeParams')

	def set_NodeParams(self, NodeParams):  # String
		self.add_body_params('NodeParams', NodeParams)
