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

class DeleteTaskRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'eas', '2018-05-22', 'DeleteTask')
		self.set_uri_pattern('/api/tasks/[region]/[task_name]')
		self.set_method('DELETE')

	def get_task_name(self):
		return self.get_path_params().get('task_name')

	def set_task_name(self,task_name):
		self.add_path_param('task_name',task_name)

	def get_region(self):
		return self.get_path_params().get('region')

	def set_region(self,region):
		self.add_path_param('region',region)