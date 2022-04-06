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
from aliyunsdkschedulerx2.endpoint import endpoint_data

class CreateAppGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'schedulerx2', '2019-04-30', 'CreateAppGroup')
		self.set_protocol_type('https')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MaxJobs(self): # Integer
		return self.get_query_params().get('MaxJobs')

	def set_MaxJobs(self, MaxJobs):  # Integer
		self.add_query_param('MaxJobs', MaxJobs)
	def get_NamespaceName(self): # String
		return self.get_query_params().get('NamespaceName')

	def set_NamespaceName(self, NamespaceName):  # String
		self.add_query_param('NamespaceName', NamespaceName)
	def get_NamespaceSource(self): # String
		return self.get_query_params().get('NamespaceSource')

	def set_NamespaceSource(self, NamespaceSource):  # String
		self.add_query_param('NamespaceSource', NamespaceSource)
	def get_ScheduleBusyWorkers(self): # Boolean
		return self.get_query_params().get('ScheduleBusyWorkers')

	def set_ScheduleBusyWorkers(self, ScheduleBusyWorkers):  # Boolean
		self.add_query_param('ScheduleBusyWorkers', ScheduleBusyWorkers)
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_MonitorConfigJson(self): # String
		return self.get_query_params().get('MonitorConfigJson')

	def set_MonitorConfigJson(self, MonitorConfigJson):  # String
		self.add_query_param('MonitorConfigJson', MonitorConfigJson)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
	def get_AppKey(self): # String
		return self.get_query_params().get('AppKey')

	def set_AppKey(self, AppKey):  # String
		self.add_query_param('AppKey', AppKey)
	def get_MonitorContactsJson(self): # String
		return self.get_query_params().get('MonitorContactsJson')

	def set_MonitorContactsJson(self, MonitorContactsJson):  # String
		self.add_query_param('MonitorContactsJson', MonitorContactsJson)
