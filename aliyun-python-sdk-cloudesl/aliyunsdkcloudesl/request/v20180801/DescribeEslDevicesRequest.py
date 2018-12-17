# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeEslDevicesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2018-08-01', 'DescribeEslDevices')

	def get_EslStatus(self):
		return self.get_query_params().get('EslStatus')

	def set_EslStatus(self,EslStatus):
		self.add_query_param('EslStatus',EslStatus)

	def get_ToBatteryLevel(self):
		return self.get_query_params().get('ToBatteryLevel')

	def set_ToBatteryLevel(self,ToBatteryLevel):
		self.add_query_param('ToBatteryLevel',ToBatteryLevel)

	def get_StoreId(self):
		return self.get_query_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_query_param('StoreId',StoreId)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_Mac(self):
		return self.get_query_params().get('Mac')

	def set_Mac(self,Mac):
		self.add_query_param('Mac',Mac)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_FromBatteryLevel(self):
		return self.get_query_params().get('FromBatteryLevel')

	def set_FromBatteryLevel(self,FromBatteryLevel):
		self.add_query_param('FromBatteryLevel',FromBatteryLevel)

	def get_ShelfCode(self):
		return self.get_query_params().get('ShelfCode')

	def set_ShelfCode(self,ShelfCode):
		self.add_query_param('ShelfCode',ShelfCode)

	def get_EslBarCode(self):
		return self.get_query_params().get('EslBarCode')

	def set_EslBarCode(self,EslBarCode):
		self.add_query_param('EslBarCode',EslBarCode)

	def get_Vendor(self):
		return self.get_query_params().get('Vendor')

	def set_Vendor(self,Vendor):
		self.add_query_param('Vendor',Vendor)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_BeBind(self):
		return self.get_query_params().get('BeBind')

	def set_BeBind(self,BeBind):
		self.add_query_param('BeBind',BeBind)

	def get_ItemBarCode(self):
		return self.get_query_params().get('ItemBarCode')

	def set_ItemBarCode(self,ItemBarCode):
		self.add_query_param('ItemBarCode',ItemBarCode)