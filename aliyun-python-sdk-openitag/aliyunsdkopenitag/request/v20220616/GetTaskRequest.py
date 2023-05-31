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

class GetTaskRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'OpenITag', '2022-06-16', 'GetTask')
		self.set_uri_pattern('/openapi/api/v1/tenants/[TenantId]/tasks/[TaskId]')
		self.set_method('GET')

	def get_TenantId(self): # String
		return self.get_path_params().get('TenantId')

	def set_TenantId(self, TenantId):  # String
		self.add_path_param('TenantId', TenantId)
	def get_TaskId(self): # String
		return self.get_path_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_path_param('TaskId', TaskId)
