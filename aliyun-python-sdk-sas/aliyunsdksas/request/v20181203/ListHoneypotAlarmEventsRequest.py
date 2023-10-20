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

class ListHoneypotAlarmEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ListHoneypotAlarmEvents','sas')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SrcIp(self): # String
		return self.get_body_params().get('SrcIp')

	def set_SrcIp(self, SrcIp):  # String
		self.add_body_params('SrcIp', SrcIp)
	def get_RiskLevelLists(self): # RepeatList
		return self.get_body_params().get('RiskLevelList')

	def set_RiskLevelLists(self, RiskLevelList):  # RepeatList
		for depth1 in range(len(RiskLevelList)):
			self.add_body_params('RiskLevelList.' + str(depth1 + 1), RiskLevelList[depth1])
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_DstIp(self): # String
		return self.get_body_params().get('DstIp')

	def set_DstIp(self, DstIp):  # String
		self.add_body_params('DstIp', DstIp)
	def get_Dealed(self): # String
		return self.get_body_params().get('Dealed')

	def set_Dealed(self, Dealed):  # String
		self.add_body_params('Dealed', Dealed)
	def get_CurrentPage(self): # Integer
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_body_params('CurrentPage', CurrentPage)
