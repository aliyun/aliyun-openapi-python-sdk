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

class DescribeEslDevicesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2020-02-01', 'DescribeEslDevices','cloudesl')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Type(self):
		return self.get_body_params().get('Type')

	def set_Type(self,Type):
		self.add_body_params('Type', Type)

	def get_StoreId(self):
		return self.get_body_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_body_params('StoreId', StoreId)

	def get_PageNumber(self):
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_body_params('PageNumber', PageNumber)

	def get_EslBarCode(self):
		return self.get_body_params().get('EslBarCode')

	def set_EslBarCode(self,EslBarCode):
		self.add_body_params('EslBarCode', EslBarCode)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_EslStatus(self):
		return self.get_body_params().get('EslStatus')

	def set_EslStatus(self,EslStatus):
		self.add_body_params('EslStatus', EslStatus)

	def get_ToBatteryLevel(self):
		return self.get_body_params().get('ToBatteryLevel')

	def set_ToBatteryLevel(self,ToBatteryLevel):
		self.add_body_params('ToBatteryLevel', ToBatteryLevel)

	def get_FromBatteryLevel(self):
		return self.get_body_params().get('FromBatteryLevel')

	def set_FromBatteryLevel(self,FromBatteryLevel):
		self.add_body_params('FromBatteryLevel', FromBatteryLevel)