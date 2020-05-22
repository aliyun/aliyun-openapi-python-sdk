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
from aliyunsdkfnf.endpoint import endpoint_data

class UpdateScheduleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'fnf', '2019-03-15', 'UpdateSchedule')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ScheduleName(self):
		return self.get_body_params().get('ScheduleName')

	def set_ScheduleName(self,ScheduleName):
		self.add_body_params('ScheduleName', ScheduleName)

	def get_CronExpression(self):
		return self.get_body_params().get('CronExpression')

	def set_CronExpression(self,CronExpression):
		self.add_body_params('CronExpression', CronExpression)

	def get_Payload(self):
		return self.get_body_params().get('Payload')

	def set_Payload(self,Payload):
		self.add_body_params('Payload', Payload)

	def get_RequestId(self):
		return self.get_query_params().get('RequestId')

	def set_RequestId(self,RequestId):
		self.add_query_param('RequestId',RequestId)

	def get_Enable(self):
		return self.get_body_params().get('Enable')

	def set_Enable(self,Enable):
		self.add_body_params('Enable', Enable)

	def get_Description(self):
		return self.get_body_params().get('Description')

	def set_Description(self,Description):
		self.add_body_params('Description', Description)

	def get_FlowName(self):
		return self.get_body_params().get('FlowName')

	def set_FlowName(self,FlowName):
		self.add_body_params('FlowName', FlowName)