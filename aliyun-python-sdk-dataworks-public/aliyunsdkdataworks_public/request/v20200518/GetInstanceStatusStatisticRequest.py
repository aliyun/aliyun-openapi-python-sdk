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

class GetInstanceStatusStatisticRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'GetInstanceStatusStatistic')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProjectEnv(self): # String
		return self.get_body_params().get('ProjectEnv')

	def set_ProjectEnv(self, ProjectEnv):  # String
		self.add_body_params('ProjectEnv', ProjectEnv)
	def get_DagType(self): # String
		return self.get_body_params().get('DagType')

	def set_DagType(self, DagType):  # String
		self.add_body_params('DagType', DagType)
	def get_BizDate(self): # String
		return self.get_body_params().get('BizDate')

	def set_BizDate(self, BizDate):  # String
		self.add_body_params('BizDate', BizDate)
	def get_SchedulerType(self): # String
		return self.get_body_params().get('SchedulerType')

	def set_SchedulerType(self, SchedulerType):  # String
		self.add_body_params('SchedulerType', SchedulerType)
	def get_ProjectId(self): # Long
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_body_params('ProjectId', ProjectId)
