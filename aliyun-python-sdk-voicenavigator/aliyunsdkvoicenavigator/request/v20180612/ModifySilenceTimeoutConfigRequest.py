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
from aliyunsdkvoicenavigator.endpoint import endpoint_data

class ModifySilenceTimeoutConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'VoiceNavigator', '2018-06-12', 'ModifySilenceTimeoutConfig','voicebot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_FinalAction(self):
		return self.get_query_params().get('FinalAction')

	def set_FinalAction(self,FinalAction):
		self.add_query_param('FinalAction',FinalAction)

	def get_FinalPrompt(self):
		return self.get_query_params().get('FinalPrompt')

	def set_FinalPrompt(self,FinalPrompt):
		self.add_query_param('FinalPrompt',FinalPrompt)

	def get_Threshold(self):
		return self.get_query_params().get('Threshold')

	def set_Threshold(self,Threshold):
		self.add_query_param('Threshold',Threshold)

	def get_IntentTrigger(self):
		return self.get_query_params().get('IntentTrigger')

	def set_IntentTrigger(self,IntentTrigger):
		self.add_query_param('IntentTrigger',IntentTrigger)

	def get_Timeout(self):
		return self.get_query_params().get('Timeout')

	def set_Timeout(self,Timeout):
		self.add_query_param('Timeout',Timeout)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_SourceType(self):
		return self.get_query_params().get('SourceType')

	def set_SourceType(self,SourceType):
		self.add_query_param('SourceType',SourceType)

	def get_FinalActionParams(self):
		return self.get_query_params().get('FinalActionParams')

	def set_FinalActionParams(self,FinalActionParams):
		self.add_query_param('FinalActionParams',FinalActionParams)

	def get_Prompt(self):
		return self.get_query_params().get('Prompt')

	def set_Prompt(self,Prompt):
		self.add_query_param('Prompt',Prompt)