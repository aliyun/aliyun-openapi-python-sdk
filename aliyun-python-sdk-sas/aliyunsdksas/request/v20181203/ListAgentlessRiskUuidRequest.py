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

class ListAgentlessRiskUuidRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ListAgentlessRiskUuid','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_InternetIp(self): # String
		return self.get_query_params().get('InternetIp')

	def set_InternetIp(self, InternetIp):  # String
		self.add_query_param('InternetIp', InternetIp)
	def get_TargetName(self): # String
		return self.get_query_params().get('TargetName')

	def set_TargetName(self, TargetName):  # String
		self.add_query_param('TargetName', TargetName)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_MachineName(self): # String
		return self.get_query_params().get('MachineName')

	def set_MachineName(self, MachineName):  # String
		self.add_query_param('MachineName', MachineName)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_Risk(self): # Boolean
		return self.get_query_params().get('Risk')

	def set_Risk(self, Risk):  # Boolean
		self.add_query_param('Risk', Risk)
	def get_IntranetIp(self): # String
		return self.get_query_params().get('IntranetIp')

	def set_IntranetIp(self, IntranetIp):  # String
		self.add_query_param('IntranetIp', IntranetIp)
