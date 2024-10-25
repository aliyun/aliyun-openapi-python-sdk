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

class CreateVSwitchRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'CreateVSwitch','ens')
		self.set_method('POST')

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_EnsRegionId(self): # String
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_query_param('EnsRegionId', EnsRegionId)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_VSwitchName(self): # String
		return self.get_query_params().get('VSwitchName')

	def set_VSwitchName(self, VSwitchName):  # String
		self.add_query_param('VSwitchName', VSwitchName)
	def get_CidrBlock(self): # String
		return self.get_query_params().get('CidrBlock')

	def set_CidrBlock(self, CidrBlock):  # String
		self.add_query_param('CidrBlock', CidrBlock)
	def get_NetworkId(self): # String
		return self.get_query_params().get('NetworkId')

	def set_NetworkId(self, NetworkId):  # String
		self.add_query_param('NetworkId', NetworkId)
