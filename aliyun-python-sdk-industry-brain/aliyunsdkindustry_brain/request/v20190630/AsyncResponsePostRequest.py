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

class AsyncResponsePostRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'industry-brain', '2019-06-30', 'AsyncResponsePost')
		self.set_method('POST')

	def get_Data(self):
		return self.get_query_params().get('Data')

	def set_Data(self,Data):
		self.add_query_param('Data',Data)

	def get_Context(self):
		return self.get_query_params().get('Context')

	def set_Context(self,Context):
		self.add_query_param('Context',Context)

	def get_Progress(self):
		return self.get_query_params().get('Progress')

	def set_Progress(self,Progress):
		self.add_query_param('Progress',Progress)

	def get_Message(self):
		return self.get_query_params().get('Message')

	def set_Message(self,Message):
		self.add_query_param('Message',Message)

	def get_TaskId(self):
		return self.get_query_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_query_param('TaskId',TaskId)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)