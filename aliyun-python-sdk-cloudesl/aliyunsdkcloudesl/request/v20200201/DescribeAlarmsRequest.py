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
from aliyunsdkcloudesl.endpoint import endpoint_data

class DescribeAlarmsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2020-02-01', 'DescribeAlarms','cloudesl')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StoreId(self):
		return self.get_body_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_body_params('StoreId', StoreId)

	def get_PageNumber(self):
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_body_params('PageNumber', PageNumber)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_AlarmType(self):
		return self.get_body_params().get('AlarmType')

	def set_AlarmType(self,AlarmType):
		self.add_body_params('AlarmType', AlarmType)

	def get_AlarmStatus(self):
		return self.get_body_params().get('AlarmStatus')

	def set_AlarmStatus(self,AlarmStatus):
		self.add_body_params('AlarmStatus', AlarmStatus)

	def get_ErrorType(self):
		return self.get_body_params().get('ErrorType')

	def set_ErrorType(self,ErrorType):
		self.add_body_params('ErrorType', ErrorType)

	def get_AlarmId(self):
		return self.get_body_params().get('AlarmId')

	def set_AlarmId(self,AlarmId):
		self.add_body_params('AlarmId', AlarmId)

	def get_DeviceMac(self):
		return self.get_body_params().get('DeviceMac')

	def set_DeviceMac(self,DeviceMac):
		self.add_body_params('DeviceMac', DeviceMac)