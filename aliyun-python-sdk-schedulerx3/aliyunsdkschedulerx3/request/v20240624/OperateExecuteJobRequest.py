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

class OperateExecuteJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SchedulerX3', '2024-06-24', 'OperateExecuteJob')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_JobId(self): # Long
		return self.get_body_params().get('JobId')

	def set_JobId(self, JobId):  # Long
		self.add_body_params('JobId', JobId)
	def get_AppName(self): # String
		return self.get_body_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_body_params('AppName', AppName)
	def get_Worker(self): # String
		return self.get_body_params().get('Worker')

	def set_Worker(self, Worker):  # String
		self.add_body_params('Worker', Worker)
	def get_InstanceParameters(self): # String
		return self.get_body_params().get('InstanceParameters')

	def set_InstanceParameters(self, InstanceParameters):  # String
		self.add_body_params('InstanceParameters', InstanceParameters)
	def get_ClusterId(self): # String
		return self.get_body_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_body_params('ClusterId', ClusterId)
	def get_Label(self): # String
		return self.get_body_params().get('Label')

	def set_Label(self, Label):  # String
		self.add_body_params('Label', Label)
