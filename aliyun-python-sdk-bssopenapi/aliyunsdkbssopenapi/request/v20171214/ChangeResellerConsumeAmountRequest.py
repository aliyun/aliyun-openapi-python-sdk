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

class ChangeResellerConsumeAmountRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'ChangeResellerConsumeAmount')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Amount(self):
		return self.get_query_params().get('Amount')

	def set_Amount(self,Amount):
		self.add_query_param('Amount',Amount)

	def get_OutBizId(self):
		return self.get_query_params().get('OutBizId')

	def set_OutBizId(self,OutBizId):
		self.add_query_param('OutBizId',OutBizId)

	def get_Source(self):
		return self.get_query_params().get('Source')

	def set_Source(self,Source):
		self.add_query_param('Source',Source)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_BusinessType(self):
		return self.get_query_params().get('BusinessType')

	def set_BusinessType(self,BusinessType):
		self.add_query_param('BusinessType',BusinessType)

	def get_AdjustType(self):
		return self.get_query_params().get('AdjustType')

	def set_AdjustType(self,AdjustType):
		self.add_query_param('AdjustType',AdjustType)

	def get_ExtendMap(self):
		return self.get_query_params().get('ExtendMap')

	def set_ExtendMap(self,ExtendMap):
		self.add_query_param('ExtendMap',ExtendMap)

	def get_Currency(self):
		return self.get_query_params().get('Currency')

	def set_Currency(self,Currency):
		self.add_query_param('Currency',Currency)