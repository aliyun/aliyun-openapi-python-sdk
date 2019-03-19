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
class ResumeInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'ResumeInstance','cloudwf')

	def get_TraceId(self):
		return self.get_query_params().get('TraceId')

	def set_TraceId(self,TraceId):
		self.add_query_param('TraceId',TraceId)

	def get_SpMsg(self):
		return self.get_query_params().get('SpMsg')

	def set_SpMsg(self,SpMsg):
		self.add_query_param('SpMsg',SpMsg)