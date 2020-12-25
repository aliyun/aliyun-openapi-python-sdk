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
from aliyunsdkemr.endpoint import endpoint_data

class CreateFlowProjectClusterSettingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'CreateFlowProjectClusterSetting','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_UserLists(self):
		return self.get_query_params().get('UserList')

	def set_UserLists(self, UserLists):
		for depth1 in range(len(UserLists)):
			if UserLists[depth1] is not None:
				self.add_query_param('UserList.' + str(depth1 + 1) , UserLists[depth1])

	def get_HostLists(self):
		return self.get_query_params().get('HostList')

	def set_HostLists(self, HostLists):
		for depth1 in range(len(HostLists)):
			if HostLists[depth1] is not None:
				self.add_query_param('HostList.' + str(depth1 + 1) , HostLists[depth1])

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_DefaultQueue(self):
		return self.get_query_params().get('DefaultQueue')

	def set_DefaultQueue(self,DefaultQueue):
		self.add_query_param('DefaultQueue',DefaultQueue)

	def get_DefaultUser(self):
		return self.get_query_params().get('DefaultUser')

	def set_DefaultUser(self,DefaultUser):
		self.add_query_param('DefaultUser',DefaultUser)

	def get_QueueLists(self):
		return self.get_query_params().get('QueueList')

	def set_QueueLists(self, QueueLists):
		for depth1 in range(len(QueueLists)):
			if QueueLists[depth1] is not None:
				self.add_query_param('QueueList.' + str(depth1 + 1) , QueueLists[depth1])

	def get_ProjectId(self):
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_query_param('ProjectId',ProjectId)