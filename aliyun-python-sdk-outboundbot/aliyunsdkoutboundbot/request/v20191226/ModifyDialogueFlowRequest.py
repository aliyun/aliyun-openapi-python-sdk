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
from aliyunsdkoutboundbot.endpoint import endpoint_data

class ModifyDialogueFlowRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'ModifyDialogueFlow','outboundbot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IsDrafted(self):
		return self.get_query_params().get('IsDrafted')

	def set_IsDrafted(self,IsDrafted):
		self.add_query_param('IsDrafted',IsDrafted)

	def get_ScriptId(self):
		return self.get_query_params().get('ScriptId')

	def set_ScriptId(self,ScriptId):
		self.add_query_param('ScriptId',ScriptId)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_DialogueFlowDefinition(self):
		return self.get_query_params().get('DialogueFlowDefinition')

	def set_DialogueFlowDefinition(self,DialogueFlowDefinition):
		self.add_query_param('DialogueFlowDefinition',DialogueFlowDefinition)

	def get_DialogueFlowId(self):
		return self.get_query_params().get('DialogueFlowId')

	def set_DialogueFlowId(self,DialogueFlowId):
		self.add_query_param('DialogueFlowId',DialogueFlowId)