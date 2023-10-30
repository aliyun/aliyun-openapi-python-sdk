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
from aliyunsdklive.endpoint import endpoint_data

class ModifyLiveMessageGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'ModifyLiveMessageGroup','live')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_GroupInfo(self): # String
		return self.get_query_params().get('GroupInfo')

	def set_GroupInfo(self, GroupInfo):  # String
		self.add_query_param('GroupInfo', GroupInfo)
	def get_DataCenter(self): # String
		return self.get_query_params().get('DataCenter')

	def set_DataCenter(self, DataCenter):  # String
		self.add_query_param('DataCenter', DataCenter)
	def get_ModifyInfo(self): # Boolean
		return self.get_query_params().get('ModifyInfo')

	def set_ModifyInfo(self, ModifyInfo):  # Boolean
		self.add_query_param('ModifyInfo', ModifyInfo)
	def get_AdminList(self): # Array
		return self.get_query_params().get('AdminList')

	def set_AdminList(self, AdminList):  # Array
		for index1, value1 in enumerate(AdminList):
			self.add_query_param('AdminList.' + str(index1 + 1), value1)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_ModifyAdmin(self): # Boolean
		return self.get_query_params().get('ModifyAdmin')

	def set_ModifyAdmin(self, ModifyAdmin):  # Boolean
		self.add_query_param('ModifyAdmin', ModifyAdmin)
