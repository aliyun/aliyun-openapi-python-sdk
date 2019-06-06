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
class StartSceneRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'PTS', '2019-05-22', 'StartScene')

	def get_TeamId(self):
		return self.get_query_params().get('TeamId')

	def set_TeamId(self,TeamId):
		self.add_query_param('TeamId',TeamId)

	def get_SceneId(self):
		return self.get_query_params().get('SceneId')

	def set_SceneId(self,SceneId):
		self.add_query_param('SceneId',SceneId)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_TaskId(self):
		return self.get_query_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_query_param('TaskId',TaskId)