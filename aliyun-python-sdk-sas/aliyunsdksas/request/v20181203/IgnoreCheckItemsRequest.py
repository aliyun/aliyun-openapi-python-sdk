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

class IgnoreCheckItemsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'IgnoreCheckItems','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Reason(self): # String
		return self.get_query_params().get('Reason')

	def set_Reason(self, Reason):  # String
		self.add_query_param('Reason', Reason)
	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_Type(self): # Integer
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # Integer
		self.add_query_param('Type', Type)
	def get_UuidLists(self): # RepeatList
		return self.get_query_params().get('UuidList')

	def set_UuidLists(self, UuidList):  # RepeatList
		for depth1 in range(len(UuidList)):
			self.add_query_param('UuidList.' + str(depth1 + 1), UuidList[depth1])
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_CheckAndRiskTypeLists(self): # RepeatList
		return self.get_query_params().get('CheckAndRiskTypeList')

	def set_CheckAndRiskTypeLists(self, CheckAndRiskTypeList):  # RepeatList
		for depth1 in range(len(CheckAndRiskTypeList)):
			if CheckAndRiskTypeList[depth1].get('RiskType') is not None:
				self.add_query_param('CheckAndRiskTypeList.' + str(depth1 + 1) + '.RiskType', CheckAndRiskTypeList[depth1].get('RiskType'))
			if CheckAndRiskTypeList[depth1].get('CheckId') is not None:
				self.add_query_param('CheckAndRiskTypeList.' + str(depth1 + 1) + '.CheckId', CheckAndRiskTypeList[depth1].get('CheckId'))
