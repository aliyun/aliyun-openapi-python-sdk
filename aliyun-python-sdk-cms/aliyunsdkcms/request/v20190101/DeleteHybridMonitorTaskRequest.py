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

class DeleteHybridMonitorTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'DeleteHybridMonitorTask','cms')
		self.set_method('POST')

	def get_TargetUserId(self): # String
		return self.get_query_params().get('TargetUserId')

	def set_TargetUserId(self, TargetUserId):  # String
		self.add_query_param('TargetUserId', TargetUserId)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
