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
from aliyunsdkemas_appmonitor.endpoint import endpoint_data

class GetAlarmLogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'emas-appmonitor', '2019-06-11', 'GetAlarmLog')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AlarmItemType(self):
		return self.get_body_params().get('AlarmItemType')

	def set_AlarmItemType(self,AlarmItemType):
		self.add_body_params('AlarmItemType', AlarmItemType)

	def get_PageNumber(self):
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_body_params('PageNumber', PageNumber)

	def get_FromDate(self):
		return self.get_body_params().get('FromDate')

	def set_FromDate(self,FromDate):
		self.add_body_params('FromDate', FromDate)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_AlarmItemId(self):
		return self.get_body_params().get('AlarmItemId')

	def set_AlarmItemId(self,AlarmItemId):
		self.add_body_params('AlarmItemId', AlarmItemId)

	def get_UniqueAppId(self):
		return self.get_body_params().get('UniqueAppId')

	def set_UniqueAppId(self,UniqueAppId):
		self.add_body_params('UniqueAppId', UniqueAppId)

	def get_UntilDate(self):
		return self.get_body_params().get('UntilDate')

	def set_UntilDate(self,UntilDate):
		self.add_body_params('UntilDate', UntilDate)