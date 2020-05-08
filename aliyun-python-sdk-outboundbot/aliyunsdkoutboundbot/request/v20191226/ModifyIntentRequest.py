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

class ModifyIntentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'ModifyIntent','outboundbot')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Utterances(self):
		return self.get_query_params().get('Utterances')

	def set_Utterances(self,Utterances):
		self.add_query_param('Utterances',Utterances)

	def get_Keywords(self):
		return self.get_query_params().get('Keywords')

	def set_Keywords(self,Keywords):
		self.add_query_param('Keywords',Keywords)

	def get_IntentDescription(self):
		return self.get_query_params().get('IntentDescription')

	def set_IntentDescription(self,IntentDescription):
		self.add_query_param('IntentDescription',IntentDescription)

	def get_IntentId(self):
		return self.get_query_params().get('IntentId')

	def set_IntentId(self,IntentId):
		self.add_query_param('IntentId',IntentId)

	def get_ScriptId(self):
		return self.get_query_params().get('ScriptId')

	def set_ScriptId(self,ScriptId):
		self.add_query_param('ScriptId',ScriptId)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_IntentName(self):
		return self.get_query_params().get('IntentName')

	def set_IntentName(self,IntentName):
		self.add_query_param('IntentName',IntentName)