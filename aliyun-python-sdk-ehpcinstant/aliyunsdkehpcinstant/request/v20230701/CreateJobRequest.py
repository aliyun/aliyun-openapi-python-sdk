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
import json

class CreateJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EhpcInstant', '2023-07-01', 'CreateJob')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_JobDescription(self): # String
		return self.get_query_params().get('JobDescription')

	def set_JobDescription(self, JobDescription):  # String
		self.add_query_param('JobDescription', JobDescription)
	def get_DeploymentPolicy(self): # Struct
		return self.get_query_params().get('DeploymentPolicy')

	def set_DeploymentPolicy(self, DeploymentPolicy):  # Struct
		self.add_query_param("DeploymentPolicy", json.dumps(DeploymentPolicy))
	def get_JobName(self): # String
		return self.get_query_params().get('JobName')

	def set_JobName(self, JobName):  # String
		self.add_query_param('JobName', JobName)
	def get_Tasks(self): # Array
		return self.get_query_params().get('Tasks')

	def set_Tasks(self, Tasks):  # Array
		self.add_query_param("Tasks", json.dumps(Tasks))
