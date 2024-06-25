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
from aliyunsdkschedulerx2.endpoint import endpoint_data

class UpdateWorkflowRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'schedulerx2', '2019-04-30', 'UpdateWorkflow','schedulerx2')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NamespaceSource(self): # String
		return self.get_body_params().get('NamespaceSource')

	def set_NamespaceSource(self, NamespaceSource):  # String
		self.add_body_params('NamespaceSource', NamespaceSource)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_WorkflowId(self): # String
		return self.get_body_params().get('WorkflowId')

	def set_WorkflowId(self, WorkflowId):  # String
		self.add_body_params('WorkflowId', WorkflowId)
	def get_GroupId(self): # String
		return self.get_body_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_body_params('GroupId', GroupId)
	def get_TimeExpression(self): # String
		return self.get_body_params().get('TimeExpression')

	def set_TimeExpression(self, TimeExpression):  # String
		self.add_body_params('TimeExpression', TimeExpression)
	def get_Namespace(self): # String
		return self.get_body_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_body_params('Namespace', Namespace)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_TimeType(self): # Integer
		return self.get_body_params().get('TimeType')

	def set_TimeType(self, TimeType):  # Integer
		self.add_body_params('TimeType', TimeType)
