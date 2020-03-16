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
from aliyunsdkiot.endpoint import endpoint_data

class CancelOTATaskByJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'CancelOTATaskByJob','Iot')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CancelScheduledTask(self):
		return self.get_query_params().get('CancelScheduledTask')

	def set_CancelScheduledTask(self,CancelScheduledTask):
		self.add_query_param('CancelScheduledTask',CancelScheduledTask)

	def get_JobId(self):
		return self.get_query_params().get('JobId')

	def set_JobId(self,JobId):
		self.add_query_param('JobId',JobId)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_CancelQueuedTask(self):
		return self.get_query_params().get('CancelQueuedTask')

	def set_CancelQueuedTask(self,CancelQueuedTask):
		self.add_query_param('CancelQueuedTask',CancelQueuedTask)

	def get_CancelInProgressTask(self):
		return self.get_query_params().get('CancelInProgressTask')

	def set_CancelInProgressTask(self,CancelInProgressTask):
		self.add_query_param('CancelInProgressTask',CancelInProgressTask)

	def get_CancelNotifiedTask(self):
		return self.get_query_params().get('CancelNotifiedTask')

	def set_CancelNotifiedTask(self,CancelNotifiedTask):
		self.add_query_param('CancelNotifiedTask',CancelNotifiedTask)