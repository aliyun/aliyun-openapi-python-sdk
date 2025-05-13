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

class UpdateAppGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'schedulerx2', '2019-04-30', 'UpdateAppGroup','schedulerx2')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_MonitorContactsJson(self): # String
		return self.get_query_params().get('MonitorContactsJson')

	def set_MonitorContactsJson(self, MonitorContactsJson):  # String
		self.add_query_param('MonitorContactsJson', MonitorContactsJson)
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_AppVersion(self): # Integer
		return self.get_query_params().get('AppVersion')

	def set_AppVersion(self, AppVersion):  # Integer
		self.add_query_param('AppVersion', AppVersion)
	def get_MonitorConfigJson(self): # String
		return self.get_query_params().get('MonitorConfigJson')

	def set_MonitorConfigJson(self, MonitorConfigJson):  # String
		self.add_query_param('MonitorConfigJson', MonitorConfigJson)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
	def get_MaxConcurrency(self): # Integer
		return self.get_query_params().get('MaxConcurrency')

	def set_MaxConcurrency(self, MaxConcurrency):  # Integer
		self.add_query_param('MaxConcurrency', MaxConcurrency)
