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
from aliyunsdkpolardb.endpoint import endpoint_data

class ModifyApplicationWhitelistRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'ModifyApplicationWhitelist','polardb')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ApplicationId(self): # String
		return self.get_query_params().get('ApplicationId')

	def set_ApplicationId(self, ApplicationId):  # String
		self.add_query_param('ApplicationId', ApplicationId)
	def get_SecurityIPArrayName(self): # String
		return self.get_query_params().get('SecurityIPArrayName')

	def set_SecurityIPArrayName(self, SecurityIPArrayName):  # String
		self.add_query_param('SecurityIPArrayName', SecurityIPArrayName)
	def get_ModifyMode(self): # String
		return self.get_query_params().get('ModifyMode')

	def set_ModifyMode(self, ModifyMode):  # String
		self.add_query_param('ModifyMode', ModifyMode)
	def get_ComponentId(self): # String
		return self.get_query_params().get('ComponentId')

	def set_ComponentId(self, ComponentId):  # String
		self.add_query_param('ComponentId', ComponentId)
	def get_SecurityIPList(self): # String
		return self.get_query_params().get('SecurityIPList')

	def set_SecurityIPList(self, SecurityIPList):  # String
		self.add_query_param('SecurityIPList', SecurityIPList)
	def get_SecurityGroups(self): # String
		return self.get_query_params().get('SecurityGroups')

	def set_SecurityGroups(self, SecurityGroups):  # String
		self.add_query_param('SecurityGroups', SecurityGroups)
