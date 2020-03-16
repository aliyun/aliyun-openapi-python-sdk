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

class CreateStreamAnalyseTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'CreateStreamAnalyseTask','imm')

	def get_Project(self):
		return self.get_query_params().get('Project')

	def set_Project(self,Project):
		self.add_query_param('Project',Project)

	def get_NotifyEndpoint(self):
		return self.get_query_params().get('NotifyEndpoint')

	def set_NotifyEndpoint(self,NotifyEndpoint):
		self.add_query_param('NotifyEndpoint',NotifyEndpoint)

	def get_StreamUri(self):
		return self.get_query_params().get('StreamUri')

	def set_StreamUri(self,StreamUri):
		self.add_query_param('StreamUri',StreamUri)

	def get_NotifyTopicName(self):
		return self.get_query_params().get('NotifyTopicName')

	def set_NotifyTopicName(self,NotifyTopicName):
		self.add_query_param('NotifyTopicName',NotifyTopicName)

	def get_TgtUri(self):
		return self.get_query_params().get('TgtUri')

	def set_TgtUri(self,TgtUri):
		self.add_query_param('TgtUri',TgtUri)