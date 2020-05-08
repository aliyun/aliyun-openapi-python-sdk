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

class ModifyAskingBackConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'VoiceNavigator', '2018-06-12', 'ModifyAskingBackConfig','voicebot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_NegativeFeedbackPrompt(self):
		return self.get_query_params().get('NegativeFeedbackPrompt')

	def set_NegativeFeedbackPrompt(self,NegativeFeedbackPrompt):
		self.add_query_param('NegativeFeedbackPrompt',NegativeFeedbackPrompt)

	def get_NegativeFeedbackAction(self):
		return self.get_query_params().get('NegativeFeedbackAction')

	def set_NegativeFeedbackAction(self,NegativeFeedbackAction):
		self.add_query_param('NegativeFeedbackAction',NegativeFeedbackAction)

	def get_Enabled(self):
		return self.get_query_params().get('Enabled')

	def set_Enabled(self,Enabled):
		self.add_query_param('Enabled',Enabled)

	def get_EnableNegativeFeedback(self):
		return self.get_query_params().get('EnableNegativeFeedback')

	def set_EnableNegativeFeedback(self,EnableNegativeFeedback):
		self.add_query_param('EnableNegativeFeedback',EnableNegativeFeedback)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Prompt(self):
		return self.get_query_params().get('Prompt')

	def set_Prompt(self,Prompt):
		self.add_query_param('Prompt',Prompt)

	def get_NegativeFeedbackUtterancess(self):
		return self.get_query_params().get('NegativeFeedbackUtterancess')

	def set_NegativeFeedbackUtterancess(self,NegativeFeedbackUtterancess):
		for i in range(len(NegativeFeedbackUtterancess)):	
			if NegativeFeedbackUtterancess[i] is not None:
				self.add_query_param('NegativeFeedbackUtterances.' + str(i + 1) , NegativeFeedbackUtterancess[i]);

	def get_NegativeFeedbackActionParams(self):
		return self.get_query_params().get('NegativeFeedbackActionParams')

	def set_NegativeFeedbackActionParams(self,NegativeFeedbackActionParams):
		self.add_query_param('NegativeFeedbackActionParams',NegativeFeedbackActionParams)