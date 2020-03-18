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

class GetReportRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'address-purification', '2019-11-18', 'GetReport')

	def get_ProductCode(self):
		return self.get_body_params().get('ProductCode')

	def set_ProductCode(self,ProductCode):
		self.add_body_params('ProductCode', ProductCode)

	def get_ReportType(self):
		return self.get_body_params().get('ReportType')

	def set_ReportType(self,ReportType):
		self.add_body_params('ReportType', ReportType)

	def get_ApiCode(self):
		return self.get_body_params().get('ApiCode')

	def set_ApiCode(self,ApiCode):
		self.add_body_params('ApiCode', ApiCode)

	def get_Granularity(self):
		return self.get_body_params().get('Granularity')

	def set_Granularity(self,Granularity):
		self.add_body_params('Granularity', Granularity)

	def get_CommodityCode(self):
		return self.get_body_params().get('CommodityCode')

	def set_CommodityCode(self,CommodityCode):
		self.add_body_params('CommodityCode', CommodityCode)

	def get_Parameters(self):
		return self.get_body_params().get('Parameters')

	def set_Parameters(self,Parameters):
		self.add_body_params('Parameters', Parameters)