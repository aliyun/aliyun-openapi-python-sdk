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

from aliyunsdkcore.request import RoaRequest

class CreateTaskRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'tingwu', '2023-09-30', 'CreateTask')
		self.set_protocol_type('https')
		self.set_uri_pattern('/openapi/tingwu/v2/tasks')
		self.set_method('PUT')

	def get_type(self): # String
		return self.get_query_params().get('type')

	def set_type(self, type):  # String
		self.add_query_param('type', type)
	def get_body(self): # String
		return self.get_body_params().get('body')

	def set_body(self, body):  # String
		self.add_body_params('body', body)
	def get_operation(self): # String
		return self.get_query_params().get('operation')

	def set_operation(self, operation):  # String
		self.add_query_param('operation', operation)
