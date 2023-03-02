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
from aliyunsdkiot.endpoint import endpoint_data

class ListAnalyticsDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'ListAnalyticsData','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_IsoId(self):
		return self.get_query_params().get('IsoId')

	def set_IsoId(self,IsoId):
		self.add_query_param('IsoId',IsoId)

	def get_ApiPath(self):
		return self.get_query_params().get('ApiPath')

	def set_ApiPath(self,ApiPath):
		self.add_query_param('ApiPath',ApiPath)

	def get_Conditions(self):
		return self.get_query_params().get('Condition')

	def set_Conditions(self, Conditions):
		for depth1 in range(len(Conditions)):
			if Conditions[depth1].get('FieldName') is not None:
				self.add_query_param('Condition.' + str(depth1 + 1) + '.FieldName', Conditions[depth1].get('FieldName'))
			if Conditions[depth1].get('Operate') is not None:
				self.add_query_param('Condition.' + str(depth1 + 1) + '.Operate', Conditions[depth1].get('Operate'))
			if Conditions[depth1].get('BetweenStart') is not None:
				self.add_query_param('Condition.' + str(depth1 + 1) + '.BetweenStart', Conditions[depth1].get('BetweenStart'))
			if Conditions[depth1].get('BetweenEnd') is not None:
				self.add_query_param('Condition.' + str(depth1 + 1) + '.BetweenEnd', Conditions[depth1].get('BetweenEnd'))
			if Conditions[depth1].get('Value') is not None:
				self.add_query_param('Condition.' + str(depth1 + 1) + '.Value', Conditions[depth1].get('Value'))