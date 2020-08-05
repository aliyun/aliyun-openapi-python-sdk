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
from aliyunsdkunimkt.endpoint import endpoint_data

class ServingPlanMigrateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-07', 'ServingPlanMigrate','uniMkt')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_QuotaPerDay(self):
		return self.get_body_params().get('QuotaPerDay')

	def set_QuotaPerDay(self,QuotaPerDay):
		self.add_body_params('QuotaPerDay', QuotaPerDay)

	def get_BrandUserId(self):
		return self.get_body_params().get('BrandUserId')

	def set_BrandUserId(self,BrandUserId):
		self.add_body_params('BrandUserId', BrandUserId)

	def get_EndTime(self):
		return self.get_body_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_body_params('EndTime', EndTime)

	def get_BrandUserNick(self):
		return self.get_body_params().get('BrandUserNick')

	def set_BrandUserNick(self,BrandUserNick):
		self.add_body_params('BrandUserNick', BrandUserNick)

	def get_StartTime(self):
		return self.get_body_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_body_params('StartTime', StartTime)

	def get_ProxyUserId(self):
		return self.get_body_params().get('ProxyUserId')

	def set_ProxyUserId(self,ProxyUserId):
		self.add_body_params('ProxyUserId', ProxyUserId)

	def get_BizType(self):
		return self.get_body_params().get('BizType')

	def set_BizType(self,BizType):
		self.add_body_params('BizType', BizType)

	def get_Quota(self):
		return self.get_body_params().get('Quota')

	def set_Quota(self,Quota):
		self.add_body_params('Quota', Quota)

	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)

	def get_ProxyUserNick(self):
		return self.get_body_params().get('ProxyUserNick')

	def set_ProxyUserNick(self,ProxyUserNick):
		self.add_body_params('ProxyUserNick', ProxyUserNick)

	def get_PayType(self):
		return self.get_body_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_body_params('PayType', PayType)

	def get_TaskId(self):
		return self.get_body_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_body_params('TaskId', TaskId)

	def get_Status(self):
		return self.get_body_params().get('Status')

	def set_Status(self,Status):
		self.add_body_params('Status', Status)