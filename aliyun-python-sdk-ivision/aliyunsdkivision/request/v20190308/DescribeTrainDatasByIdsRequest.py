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
class DescribeTrainDatasByIdsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ivision', '2019-03-08', 'DescribeTrainDatasByIds','ivision')

	def get_DataIds(self):
		return self.get_query_params().get('DataIds')

	def set_DataIds(self,DataIds):
		self.add_query_param('DataIds',DataIds)

	def get_ProjectId(self):
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_query_param('ProjectId',ProjectId)

	def get_ShowLog(self):
		return self.get_query_params().get('ShowLog')

	def set_ShowLog(self,ShowLog):
		self.add_query_param('ShowLog',ShowLog)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_IterationId(self):
		return self.get_query_params().get('IterationId')

	def set_IterationId(self,IterationId):
		self.add_query_param('IterationId',IterationId)