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

class StopExecutionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'fnf', '2019-03-15', 'StopExecution','fnf')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ExecutionName(self):
		return self.get_body_params().get('ExecutionName')

	def set_ExecutionName(self,ExecutionName):
		self.add_body_params('ExecutionName', ExecutionName)

	def get_Cause(self):
		return self.get_body_params().get('Cause')

	def set_Cause(self,Cause):
		self.add_body_params('Cause', Cause)

	def get_Error(self):
		return self.get_body_params().get('Error')

	def set_Error(self,Error):
		self.add_body_params('Error', Error)

	def get_RequestId(self):
		return self.get_query_params().get('RequestId')

	def set_RequestId(self,RequestId):
		self.add_query_param('RequestId',RequestId)

	def get_FlowName(self):
		return self.get_body_params().get('FlowName')

	def set_FlowName(self,FlowName):
		self.add_body_params('FlowName', FlowName)