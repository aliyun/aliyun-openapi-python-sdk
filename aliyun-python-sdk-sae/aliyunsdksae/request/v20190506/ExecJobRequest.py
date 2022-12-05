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

from aliyunsdkcore.request import RoaRequest
from aliyunsdksae.endpoint import endpoint_data

class ExecJobRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'sae', '2019-05-06', 'ExecJob','serverless')
		self.set_uri_pattern('/pop/v1/sam/job/execJob')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EventId(self): # String
		return self.get_query_params().get('EventId')

	def set_EventId(self, EventId):  # String
		self.add_query_param('EventId', EventId)
	def get_JarStartOptions(self): # String
		return self.get_query_params().get('JarStartOptions')

	def set_JarStartOptions(self, JarStartOptions):  # String
		self.add_query_param('JarStartOptions', JarStartOptions)
	def get_JarStartArgs(self): # String
		return self.get_query_params().get('JarStartArgs')

	def set_JarStartArgs(self, JarStartArgs):  # String
		self.add_query_param('JarStartArgs', JarStartArgs)
	def get_CommandArgs(self): # String
		return self.get_query_params().get('CommandArgs')

	def set_CommandArgs(self, CommandArgs):  # String
		self.add_query_param('CommandArgs', CommandArgs)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_Envs(self): # String
		return self.get_query_params().get('Envs')

	def set_Envs(self, Envs):  # String
		self.add_query_param('Envs', Envs)
	def get_Time(self): # String
		return self.get_query_params().get('Time')

	def set_Time(self, Time):  # String
		self.add_query_param('Time', Time)
	def get_Command(self): # String
		return self.get_query_params().get('Command')

	def set_Command(self, Command):  # String
		self.add_query_param('Command', Command)
	def get_WarStartOptions(self): # String
		return self.get_query_params().get('WarStartOptions')

	def set_WarStartOptions(self, WarStartOptions):  # String
		self.add_query_param('WarStartOptions', WarStartOptions)
