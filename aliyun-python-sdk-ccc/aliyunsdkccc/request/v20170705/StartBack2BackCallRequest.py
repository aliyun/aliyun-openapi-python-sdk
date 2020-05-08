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
from aliyunsdkccc.endpoint import endpoint_data

class StartBack2BackCallRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'StartBack2BackCall')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CallCenterNumber(self):
		return self.get_query_params().get('CallCenterNumber')

	def set_CallCenterNumber(self,CallCenterNumber):
		self.add_query_param('CallCenterNumber',CallCenterNumber)

	def get_Callee(self):
		return self.get_query_params().get('Callee')

	def set_Callee(self,Callee):
		self.add_query_param('Callee',Callee)

	def get_Caller(self):
		return self.get_query_params().get('Caller')

	def set_Caller(self,Caller):
		self.add_query_param('Caller',Caller)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_WorkflowId(self):
		return self.get_query_params().get('WorkflowId')

	def set_WorkflowId(self,WorkflowId):
		self.add_query_param('WorkflowId',WorkflowId)