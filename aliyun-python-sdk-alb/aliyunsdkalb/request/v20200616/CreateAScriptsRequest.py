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
from aliyunsdkalb.endpoint import endpoint_data

class CreateAScriptsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'CreateAScripts','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ListenerId(self): # String
		return self.get_query_params().get('ListenerId')

	def set_ListenerId(self, ListenerId):  # String
		self.add_query_param('ListenerId', ListenerId)
	def get_AScripts(self): # Array
		return self.get_query_params().get('AScripts')

	def set_AScripts(self, AScripts):  # Array
		for index1, value1 in enumerate(AScripts):
			if value1.get('AScriptName') is not None:
				self.add_query_param('AScripts.' + str(index1 + 1) + '.AScriptName', value1.get('AScriptName'))
			if value1.get('ExtAttributeEnabled') is not None:
				self.add_query_param('AScripts.' + str(index1 + 1) + '.ExtAttributeEnabled', value1.get('ExtAttributeEnabled'))
			if value1.get('Position') is not None:
				self.add_query_param('AScripts.' + str(index1 + 1) + '.Position', value1.get('Position'))
			if value1.get('ScriptContent') is not None:
				self.add_query_param('AScripts.' + str(index1 + 1) + '.ScriptContent', value1.get('ScriptContent'))
			if value1.get('ExtAttributes') is not None:
				for index2, value2 in enumerate(value1.get('ExtAttributes')):
					if value2.get('AttributeValue') is not None:
						self.add_query_param('AScripts.' + str(index1 + 1) + '.ExtAttributes.' + str(index2 + 1) + '.AttributeValue', value2.get('AttributeValue'))
					if value2.get('AttributeKey') is not None:
						self.add_query_param('AScripts.' + str(index1 + 1) + '.ExtAttributes.' + str(index2 + 1) + '.AttributeKey', value2.get('AttributeKey'))
			if value1.get('Enabled') is not None:
				self.add_query_param('AScripts.' + str(index1 + 1) + '.Enabled', value1.get('Enabled'))
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
