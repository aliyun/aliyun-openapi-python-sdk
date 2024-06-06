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
from aliyunsdkidaas_doraemon.endpoint import endpoint_data

class ListOrderConsumeStatisticRecordsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'idaas-doraemon', '2021-05-20', 'ListOrderConsumeStatisticRecords','idaasauth')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StatisticTimeMin(self): # String
		return self.get_query_params().get('StatisticTimeMin')

	def set_StatisticTimeMin(self, StatisticTimeMin):  # String
		self.add_query_param('StatisticTimeMin', StatisticTimeMin)
	def get_AliOrderCode(self): # String
		return self.get_query_params().get('AliOrderCode')

	def set_AliOrderCode(self, AliOrderCode):  # String
		self.add_query_param('AliOrderCode', AliOrderCode)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_ServiceCode(self): # String
		return self.get_query_params().get('ServiceCode')

	def set_ServiceCode(self, ServiceCode):  # String
		self.add_query_param('ServiceCode', ServiceCode)
	def get_StatisticTimeMax(self): # String
		return self.get_query_params().get('StatisticTimeMax')

	def set_StatisticTimeMax(self, StatisticTimeMax):  # String
		self.add_query_param('StatisticTimeMax', StatisticTimeMax)
	def get_ApplicationExternalId(self): # String
		return self.get_query_params().get('ApplicationExternalId')

	def set_ApplicationExternalId(self, ApplicationExternalId):  # String
		self.add_query_param('ApplicationExternalId', ApplicationExternalId)
