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

class ModifySnatEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'ModifySnatEntry','ens')
		self.set_method('POST')

	def get_SnatIp(self): # String
		return self.get_query_params().get('SnatIp')

	def set_SnatIp(self, SnatIp):  # String
		self.add_query_param('SnatIp', SnatIp)
	def get_EipAffinity(self): # Boolean
		return self.get_query_params().get('EipAffinity')

	def set_EipAffinity(self, EipAffinity):  # Boolean
		self.add_query_param('EipAffinity', EipAffinity)
	def get_SnatEntryId(self): # String
		return self.get_query_params().get('SnatEntryId')

	def set_SnatEntryId(self, SnatEntryId):  # String
		self.add_query_param('SnatEntryId', SnatEntryId)
	def get_SnatEntryName(self): # String
		return self.get_query_params().get('SnatEntryName')

	def set_SnatEntryName(self, SnatEntryName):  # String
		self.add_query_param('SnatEntryName', SnatEntryName)
	def get_IspAffinity(self): # Boolean
		return self.get_query_params().get('IspAffinity')

	def set_IspAffinity(self, IspAffinity):  # Boolean
		self.add_query_param('IspAffinity', IspAffinity)
