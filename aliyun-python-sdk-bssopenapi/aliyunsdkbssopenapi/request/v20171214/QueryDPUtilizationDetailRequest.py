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
from aliyunsdkbssopenapi.endpoint import endpoint_data

class QueryDPUtilizationDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'QueryDPUtilizationDetail')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DeductedInstanceId(self): # String
		return self.get_query_params().get('DeductedInstanceId')

	def set_DeductedInstanceId(self, DeductedInstanceId):  # String
		self.add_query_param('DeductedInstanceId', DeductedInstanceId)
	def get_LastToken(self): # String
		return self.get_query_params().get('LastToken')

	def set_LastToken(self, LastToken):  # String
		self.add_query_param('LastToken', LastToken)
	def get_InstanceSpec(self): # String
		return self.get_query_params().get('InstanceSpec')

	def set_InstanceSpec(self, InstanceSpec):  # String
		self.add_query_param('InstanceSpec', InstanceSpec)
	def get_ProdCode(self): # String
		return self.get_query_params().get('ProdCode')

	def set_ProdCode(self, ProdCode):  # String
		self.add_query_param('ProdCode', ProdCode)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_IncludeShare(self): # Boolean
		return self.get_query_params().get('IncludeShare')

	def set_IncludeShare(self, IncludeShare):  # Boolean
		self.add_query_param('IncludeShare', IncludeShare)
	def get_CommodityCode(self): # String
		return self.get_query_params().get('CommodityCode')

	def set_CommodityCode(self, CommodityCode):  # String
		self.add_query_param('CommodityCode', CommodityCode)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_Limit(self): # Integer
		return self.get_query_params().get('Limit')

	def set_Limit(self, Limit):  # Integer
		self.add_query_param('Limit', Limit)
