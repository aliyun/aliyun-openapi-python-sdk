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
from aliyunsdkarms.endpoint import endpoint_data

class ApplyScenarioRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'ApplyScenario','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SnForce(self): # Boolean
		return self.get_query_params().get('SnForce')

	def set_SnForce(self, SnForce):  # Boolean
		self.add_query_param('SnForce', SnForce)
	def get_Sign(self): # String
		return self.get_query_params().get('Sign')

	def set_Sign(self, Sign):  # String
		self.add_query_param('Sign', Sign)
	def get_SnStat(self): # Boolean
		return self.get_query_params().get('SnStat')

	def set_SnStat(self, SnStat):  # Boolean
		self.add_query_param('SnStat', SnStat)
	def get_Scenario(self): # String
		return self.get_query_params().get('Scenario')

	def set_Scenario(self, Scenario):  # String
		self.add_query_param('Scenario', Scenario)
	def get_SnDump(self): # Boolean
		return self.get_query_params().get('SnDump')

	def set_SnDump(self, SnDump):  # Boolean
		self.add_query_param('SnDump', SnDump)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_SnTransfer(self): # Boolean
		return self.get_query_params().get('SnTransfer')

	def set_SnTransfer(self, SnTransfer):  # Boolean
		self.add_query_param('SnTransfer', SnTransfer)
	def get_UpdateOption(self): # Boolean
		return self.get_query_params().get('UpdateOption')

	def set_UpdateOption(self, UpdateOption):  # Boolean
		self.add_query_param('UpdateOption', UpdateOption)
	def get_Config(self): # String
		return self.get_query_params().get('Config')

	def set_Config(self, Config):  # String
		self.add_query_param('Config', Config)
