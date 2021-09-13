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
from aliyunsdklinkwan.endpoint import endpoint_data

class CountGatewaysRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2019-03-01', 'CountGateways','linkwan')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_FuzzyGwEui(self):
		return self.get_query_params().get('FuzzyGwEui')

	def set_FuzzyGwEui(self,FuzzyGwEui):
		self.add_query_param('FuzzyGwEui',FuzzyGwEui)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_FuzzyCity(self):
		return self.get_query_params().get('FuzzyCity')

	def set_FuzzyCity(self,FuzzyCity):
		self.add_query_param('FuzzyCity',FuzzyCity)

	def get_OnlineState(self):
		return self.get_query_params().get('OnlineState')

	def set_OnlineState(self,OnlineState):
		self.add_query_param('OnlineState',OnlineState)

	def get_IsEnabled(self):
		return self.get_query_params().get('IsEnabled')

	def set_IsEnabled(self,IsEnabled):
		self.add_query_param('IsEnabled',IsEnabled)

	def get_FuzzyName(self):
		return self.get_query_params().get('FuzzyName')

	def set_FuzzyName(self,FuzzyName):
		self.add_query_param('FuzzyName',FuzzyName)

	def get_FreqBandPlanGroupId(self):
		return self.get_query_params().get('FreqBandPlanGroupId')

	def set_FreqBandPlanGroupId(self,FreqBandPlanGroupId):
		self.add_query_param('FreqBandPlanGroupId',FreqBandPlanGroupId)