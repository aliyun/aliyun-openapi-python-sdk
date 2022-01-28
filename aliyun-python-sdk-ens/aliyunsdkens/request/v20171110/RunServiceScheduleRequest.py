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

class RunServiceScheduleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'RunServiceSchedule','ens')
		self.set_method('POST')

	def get_Uuid(self): # String
		return self.get_query_params().get('Uuid')

	def set_Uuid(self, Uuid):  # String
		self.add_query_param('Uuid', Uuid)
	def get_ClientIp(self): # String
		return self.get_query_params().get('ClientIp')

	def set_ClientIp(self, ClientIp):  # String
		self.add_query_param('ClientIp', ClientIp)
	def get_PodConfigName(self): # String
		return self.get_query_params().get('PodConfigName')

	def set_PodConfigName(self, PodConfigName):  # String
		self.add_query_param('PodConfigName', PodConfigName)
	def get_ServiceCommands(self): # String
		return self.get_query_params().get('ServiceCommands')

	def set_ServiceCommands(self, ServiceCommands):  # String
		self.add_query_param('ServiceCommands', ServiceCommands)
	def get_ScheduleStrategy(self): # String
		return self.get_query_params().get('ScheduleStrategy')

	def set_ScheduleStrategy(self, ScheduleStrategy):  # String
		self.add_query_param('ScheduleStrategy', ScheduleStrategy)
	def get_Directorys(self): # String
		return self.get_query_params().get('Directorys')

	def set_Directorys(self, Directorys):  # String
		self.add_query_param('Directorys', Directorys)
	def get_PreLockedTimeout(self): # Integer
		return self.get_query_params().get('PreLockedTimeout')

	def set_PreLockedTimeout(self, PreLockedTimeout):  # Integer
		self.add_query_param('PreLockedTimeout', PreLockedTimeout)
	def get_ServiceAction(self): # String
		return self.get_query_params().get('ServiceAction')

	def set_ServiceAction(self, ServiceAction):  # String
		self.add_query_param('ServiceAction', ServiceAction)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
