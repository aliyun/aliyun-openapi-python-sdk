# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateMonitorGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'CreateMonitorGroup','cms')

	def get_ContactGroups(self):
		return self.get_query_params().get('ContactGroups')

	def set_ContactGroups(self,ContactGroups):
		self.add_query_param('ContactGroups',ContactGroups)

	def get_Options(self):
		return self.get_query_params().get('Options')

	def set_Options(self,Options):
		self.add_query_param('Options',Options)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_ServiceId(self):
		return self.get_query_params().get('ServiceId')

	def set_ServiceId(self,ServiceId):
		self.add_query_param('ServiceId',ServiceId)

	def get_GroupName(self):
		return self.get_query_params().get('GroupName')

	def set_GroupName(self,GroupName):
		self.add_query_param('GroupName',GroupName)

	def get_BindUrl(self):
		return self.get_query_params().get('BindUrl')

	def set_BindUrl(self,BindUrl):
		self.add_query_param('BindUrl',BindUrl)