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


	def get_SnForce(self):
		return self.get_query_params().get('SnForce')

	def set_SnForce(self,SnForce):
		self.add_query_param('SnForce',SnForce)

	def get_Sign(self):
		return self.get_query_params().get('Sign')

	def set_Sign(self,Sign):
		self.add_query_param('Sign',Sign)

	def get_SnStat(self):
		return self.get_query_params().get('SnStat')

	def set_SnStat(self,SnStat):
		self.add_query_param('SnStat',SnStat)

	def get_Scenario(self):
		return self.get_query_params().get('Scenario')

	def set_Scenario(self,Scenario):
		self.add_query_param('Scenario',Scenario)

	def get_SnDump(self):
		return self.get_query_params().get('SnDump')

	def set_SnDump(self,SnDump):
		self.add_query_param('SnDump',SnDump)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_SnTransfer(self):
		return self.get_query_params().get('SnTransfer')

	def set_SnTransfer(self,SnTransfer):
		self.add_query_param('SnTransfer',SnTransfer)

	def get_UpdateOption(self):
		return self.get_query_params().get('UpdateOption')

	def set_UpdateOption(self,UpdateOption):
		self.add_query_param('UpdateOption',UpdateOption)

	def get_Config(self):
		return self.get_query_params().get('Config')

	def set_Config(self,Config):
		self.add_query_param('Config',Config)