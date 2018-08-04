# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeFlowNodeInstanceLauncherLogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'DescribeFlowNodeInstanceLauncherLog')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Start(self):
		return self.get_query_params().get('Start')

	def set_Start(self,Start):
		self.add_query_param('Start',Start)

	def get_Lines(self):
		return self.get_query_params().get('Lines')

	def set_Lines(self,Lines):
		self.add_query_param('Lines',Lines)

	def get_NodeInstanceId(self):
		return self.get_query_params().get('NodeInstanceId')

	def set_NodeInstanceId(self,NodeInstanceId):
		self.add_query_param('NodeInstanceId',NodeInstanceId)

	def get_ProjectId(self):
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_query_param('ProjectId',ProjectId)