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

class GetPredictResultRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'iqa', '2019-08-13', 'GetPredictResult','iqa')

	def get_TopK(self):
		return self.get_query_params().get('TopK')

	def set_TopK(self,TopK):
		self.add_query_param('TopK',TopK)

	def get_TraceTag(self):
		return self.get_query_params().get('TraceTag')

	def set_TraceTag(self,TraceTag):
		self.add_query_param('TraceTag',TraceTag)

	def get_Question(self):
		return self.get_body_params().get('Question')

	def set_Question(self,Question):
		self.add_body_params('Question', Question)

	def get_ProjectId(self):
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_query_param('ProjectId',ProjectId)