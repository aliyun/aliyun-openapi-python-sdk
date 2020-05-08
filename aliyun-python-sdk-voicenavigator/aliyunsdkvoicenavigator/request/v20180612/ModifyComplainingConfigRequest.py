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

class ModifyComplainingConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'VoiceNavigator', '2018-06-12', 'ModifyComplainingConfig','voicebot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Utterancess(self):
		return self.get_query_params().get('Utterancess')

	def set_Utterancess(self,Utterancess):
		for i in range(len(Utterancess)):	
			if Utterancess[i] is not None:
				self.add_query_param('Utterances.' + str(i + 1) , Utterancess[i]);

	def get_FinalAction(self):
		return self.get_query_params().get('FinalAction')

	def set_FinalAction(self,FinalAction):
		self.add_query_param('FinalAction',FinalAction)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_FinalActionParams(self):
		return self.get_query_params().get('FinalActionParams')

	def set_FinalActionParams(self,FinalActionParams):
		self.add_query_param('FinalActionParams',FinalActionParams)

	def get_Prompt(self):
		return self.get_query_params().get('Prompt')

	def set_Prompt(self,Prompt):
		self.add_query_param('Prompt',Prompt)