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
from aliyunsdksas.endpoint import endpoint_data

class BindAuthToMachineRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'BindAuthToMachine','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Criteria(self): # String
		return self.get_query_params().get('Criteria')

	def set_Criteria(self, Criteria):  # String
		self.add_query_param('Criteria', Criteria)
	def get_BindAll(self): # Boolean
		return self.get_query_params().get('BindAll')

	def set_BindAll(self, BindAll):  # Boolean
		self.add_query_param('BindAll', BindAll)
	def get_Binds(self): # RepeatList
		return self.get_query_params().get('Bind')

	def set_Binds(self, Bind):  # RepeatList
		for depth1 in range(len(Bind)):
			self.add_query_param('Bind.' + str(depth1 + 1), Bind[depth1])
	def get_AuthVersion(self): # Integer
		return self.get_query_params().get('AuthVersion')

	def set_AuthVersion(self, AuthVersion):  # Integer
		self.add_query_param('AuthVersion', AuthVersion)
	def get_LogicalExp(self): # String
		return self.get_query_params().get('LogicalExp')

	def set_LogicalExp(self, LogicalExp):  # String
		self.add_query_param('LogicalExp', LogicalExp)
	def get_AutoBind(self): # Integer
		return self.get_query_params().get('AutoBind')

	def set_AutoBind(self, AutoBind):  # Integer
		self.add_query_param('AutoBind', AutoBind)
	def get_UnBinds(self): # RepeatList
		return self.get_query_params().get('UnBind')

	def set_UnBinds(self, UnBind):  # RepeatList
		for depth1 in range(len(UnBind)):
			self.add_query_param('UnBind.' + str(depth1 + 1), UnBind[depth1])
