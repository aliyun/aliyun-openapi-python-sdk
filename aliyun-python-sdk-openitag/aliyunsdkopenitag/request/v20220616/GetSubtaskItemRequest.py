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

class GetSubtaskItemRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'OpenITag', '2022-06-16', 'GetSubtaskItem')
		self.set_uri_pattern('/openapi/api/v1/tenants/[TenantId]/tasks/[TaskId]/subtasks/[SubtaskId]/items/[ItemId]')
		self.set_method('GET')

	def get_ItemId(self): # String
		return self.get_path_params().get('ItemId')

	def set_ItemId(self, ItemId):  # String
		self.add_path_param('ItemId', ItemId)
	def get_TenantId(self): # String
		return self.get_path_params().get('TenantId')

	def set_TenantId(self, TenantId):  # String
		self.add_path_param('TenantId', TenantId)
	def get_SubtaskId(self): # String
		return self.get_path_params().get('SubtaskId')

	def set_SubtaskId(self, SubtaskId):  # String
		self.add_path_param('SubtaskId', SubtaskId)
	def get_TaskId(self): # String
		return self.get_path_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_path_param('TaskId', TaskId)
