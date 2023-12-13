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

class ConfigNetStatusRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DdosDiversion', '2023-07-01', 'ConfigNetStatus')
		self.set_method('POST')

	def get_Regions(self): # Array
		return self.get_query_params().get('Regions')

	def set_Regions(self, Regions):  # Array
		for index1, value1 in enumerate(Regions):
			self.add_query_param('Regions.' + str(index1 + 1), value1)
	def get_SubNets(self): # Array
		return self.get_query_params().get('SubNets')

	def set_SubNets(self, SubNets):  # Array
		for index1, value1 in enumerate(SubNets):
			self.add_query_param('SubNets.' + str(index1 + 1), value1)
	def get_Net(self): # String
		return self.get_query_params().get('Net')

	def set_Net(self, Net):  # String
		self.add_query_param('Net', Net)
	def get_SaleId(self): # String
		return self.get_query_params().get('SaleId')

	def set_SaleId(self, SaleId):  # String
		self.add_query_param('SaleId', SaleId)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
