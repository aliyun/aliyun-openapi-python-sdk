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

class QueryRIUtilizationDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'QueryRIUtilizationDetail','bssopenapi')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DeductedInstanceId(self):
		return self.get_query_params().get('DeductedInstanceId')

	def set_DeductedInstanceId(self,DeductedInstanceId):
		self.add_query_param('DeductedInstanceId',DeductedInstanceId)

	def get_InstanceSpec(self):
		return self.get_query_params().get('InstanceSpec')

	def set_InstanceSpec(self,InstanceSpec):
		self.add_query_param('InstanceSpec',InstanceSpec)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_RIInstanceId(self):
		return self.get_query_params().get('RIInstanceId')

	def set_RIInstanceId(self,RIInstanceId):
		self.add_query_param('RIInstanceId',RIInstanceId)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_RICommodityCode(self):
		return self.get_query_params().get('RICommodityCode')

	def set_RICommodityCode(self,RICommodityCode):
		self.add_query_param('RICommodityCode',RICommodityCode)