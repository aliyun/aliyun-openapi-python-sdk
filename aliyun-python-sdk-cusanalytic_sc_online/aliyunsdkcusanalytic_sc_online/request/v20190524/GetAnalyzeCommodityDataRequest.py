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
from aliyunsdkcusanalytic_sc_online.endpoint import endpoint_data

class GetAnalyzeCommodityDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cusanalytic_sc_online', '2019-05-24', 'GetAnalyzeCommodityData')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StoreId(self):
		return self.get_body_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_body_params('StoreId', StoreId)

	def get_StartDate(self):
		return self.get_body_params().get('StartDate')

	def set_StartDate(self,StartDate):
		self.add_body_params('StartDate', StartDate)

	def get_EndUserCount(self):
		return self.get_body_params().get('EndUserCount')

	def set_EndUserCount(self,EndUserCount):
		self.add_body_params('EndUserCount', EndUserCount)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_PageIndex(self):
		return self.get_body_params().get('PageIndex')

	def set_PageIndex(self,PageIndex):
		self.add_body_params('PageIndex', PageIndex)

	def get_StayPeriod(self):
		return self.get_body_params().get('StayPeriod')

	def set_StayPeriod(self,StayPeriod):
		self.add_body_params('StayPeriod', StayPeriod)

	def get_StartUserCount(self):
		return self.get_body_params().get('StartUserCount')

	def set_StartUserCount(self,StartUserCount):
		self.add_body_params('StartUserCount', StartUserCount)

	def get_MinSupportCount(self):
		return self.get_body_params().get('MinSupportCount')

	def set_MinSupportCount(self,MinSupportCount):
		self.add_body_params('MinSupportCount', MinSupportCount)

	def get_EndDate(self):
		return self.get_body_params().get('EndDate')

	def set_EndDate(self,EndDate):
		self.add_body_params('EndDate', EndDate)