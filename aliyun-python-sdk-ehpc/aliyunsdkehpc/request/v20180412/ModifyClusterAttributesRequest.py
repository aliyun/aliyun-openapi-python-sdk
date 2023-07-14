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
from aliyunsdkehpc.endpoint import endpoint_data

class ModifyClusterAttributesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'ModifyClusterAttributes')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_RamRoleName(self): # String
		return self.get_query_params().get('RamRoleName')

	def set_RamRoleName(self, RamRoleName):  # String
		self.add_query_param('RamRoleName', RamRoleName)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_ImageOwnerAlias(self): # String
		return self.get_query_params().get('ImageOwnerAlias')

	def set_ImageOwnerAlias(self, ImageOwnerAlias):  # String
		self.add_query_param('ImageOwnerAlias', ImageOwnerAlias)
	def get_RamNodeTypess(self): # RepeatList
		return self.get_query_params().get('RamNodeTypes')

	def set_RamNodeTypess(self, RamNodeTypes):  # RepeatList
		for depth1 in range(len(RamNodeTypes)):
			self.add_query_param('RamNodeTypes.' + str(depth1 + 1), RamNodeTypes[depth1])
	def get_WinAdPar(self): # Struct
		return self.get_query_params().get('WinAdPar')

	def set_WinAdPar(self, WinAdPar):  # Struct
		if WinAdPar.get('AdUser') is not None:
			self.add_query_param('WinAdPar.AdUser', WinAdPar.get('AdUser'))
		if WinAdPar.get('AdUserPasswd') is not None:
			self.add_query_param('WinAdPar.AdUserPasswd', WinAdPar.get('AdUserPasswd'))
		if WinAdPar.get('AdIp') is not None:
			self.add_query_param('WinAdPar.AdIp', WinAdPar.get('AdIp'))
		if WinAdPar.get('FallbackHomeDir') is not None:
			self.add_query_param('WinAdPar.FallbackHomeDir', WinAdPar.get('FallbackHomeDir'))
		if WinAdPar.get('AdDc') is not None:
			self.add_query_param('WinAdPar.AdDc', WinAdPar.get('AdDc'))
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
