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
from aliyunsdkdms_enterprise.endpoint import endpoint_data

class SetWorkflowExtraInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'SetWorkflowExtraInfo','dms-enterprise')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ThirdpartyWorkflowComment(self): # String
		return self.get_query_params().get('ThirdpartyWorkflowComment')

	def set_ThirdpartyWorkflowComment(self, ThirdpartyWorkflowComment):  # String
		self.add_query_param('ThirdpartyWorkflowComment', ThirdpartyWorkflowComment)
	def get_RenderAgree(self): # Boolean
		return self.get_query_params().get('RenderAgree')

	def set_RenderAgree(self, RenderAgree):  # Boolean
		self.add_query_param('RenderAgree', RenderAgree)
	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
	def get_WorkflowInstanceId(self): # Long
		return self.get_query_params().get('WorkflowInstanceId')

	def set_WorkflowInstanceId(self, WorkflowInstanceId):  # Long
		self.add_query_param('WorkflowInstanceId', WorkflowInstanceId)
	def get_RenderCancel(self): # Boolean
		return self.get_query_params().get('RenderCancel')

	def set_RenderCancel(self, RenderCancel):  # Boolean
		self.add_query_param('RenderCancel', RenderCancel)
	def get_RenderAddApprovalNode(self): # Boolean
		return self.get_query_params().get('RenderAddApprovalNode')

	def set_RenderAddApprovalNode(self, RenderAddApprovalNode):  # Boolean
		self.add_query_param('RenderAddApprovalNode', RenderAddApprovalNode)
	def get_RenderTransfer(self): # Boolean
		return self.get_query_params().get('RenderTransfer')

	def set_RenderTransfer(self, RenderTransfer):  # Boolean
		self.add_query_param('RenderTransfer', RenderTransfer)
	def get_RenderReject(self): # Boolean
		return self.get_query_params().get('RenderReject')

	def set_RenderReject(self, RenderReject):  # Boolean
		self.add_query_param('RenderReject', RenderReject)
	def get_ThirdpartyWorkflowUrl(self): # String
		return self.get_query_params().get('ThirdpartyWorkflowUrl')

	def set_ThirdpartyWorkflowUrl(self, ThirdpartyWorkflowUrl):  # String
		self.add_query_param('ThirdpartyWorkflowUrl', ThirdpartyWorkflowUrl)
