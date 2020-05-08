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
class ShopCreateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'ShopCreate','cloudwf')

	def get_ShopCoordinate(self):
		return self.get_query_params().get('ShopCoordinate')

	def set_ShopCoordinate(self,ShopCoordinate):
		self.add_query_param('ShopCoordinate',ShopCoordinate)

	def get_ShopProvince(self):
		return self.get_query_params().get('ShopProvince')

	def set_ShopProvince(self,ShopProvince):
		self.add_query_param('ShopProvince',ShopProvince)

	def get_ShopTopType(self):
		return self.get_query_params().get('ShopTopType')

	def set_ShopTopType(self,ShopTopType):
		self.add_query_param('ShopTopType',ShopTopType)

	def get_ShopAddress(self):
		return self.get_query_params().get('ShopAddress')

	def set_ShopAddress(self,ShopAddress):
		self.add_query_param('ShopAddress',ShopAddress)

	def get_ShopType(self):
		return self.get_query_params().get('ShopType')

	def set_ShopType(self,ShopType):
		self.add_query_param('ShopType',ShopType)

	def get_WarnEmail(self):
		return self.get_query_params().get('WarnEmail')

	def set_WarnEmail(self,WarnEmail):
		self.add_query_param('WarnEmail',WarnEmail)

	def get_ShopTel(self):
		return self.get_query_params().get('ShopTel')

	def set_ShopTel(self,ShopTel):
		self.add_query_param('ShopTel',ShopTel)

	def get_WarnpHone(self):
		return self.get_query_params().get('WarnpHone')

	def set_WarnpHone(self,WarnpHone):
		self.add_query_param('WarnpHone',WarnpHone)

	def get_Warn(self):
		return self.get_query_params().get('Warn')

	def set_Warn(self,Warn):
		self.add_query_param('Warn',Warn)

	def get_ShopArea(self):
		return self.get_query_params().get('ShopArea')

	def set_ShopArea(self,ShopArea):
		self.add_query_param('ShopArea',ShopArea)

	def get_ShopRemarks(self):
		return self.get_query_params().get('ShopRemarks')

	def set_ShopRemarks(self,ShopRemarks):
		self.add_query_param('ShopRemarks',ShopRemarks)

	def get_ShopCity(self):
		return self.get_query_params().get('ShopCity')

	def set_ShopCity(self,ShopCity):
		self.add_query_param('ShopCity',ShopCity)

	def get_ShopSubtype(self):
		return self.get_query_params().get('ShopSubtype')

	def set_ShopSubtype(self,ShopSubtype):
		self.add_query_param('ShopSubtype',ShopSubtype)

	def get_ShopBrand(self):
		return self.get_query_params().get('ShopBrand')

	def set_ShopBrand(self,ShopBrand):
		self.add_query_param('ShopBrand',ShopBrand)

	def get_ShopName(self):
		return self.get_query_params().get('ShopName')

	def set_ShopName(self,ShopName):
		self.add_query_param('ShopName',ShopName)

	def get_ShopCloseWarn(self):
		return self.get_query_params().get('ShopCloseWarn')

	def set_ShopCloseWarn(self,ShopCloseWarn):
		self.add_query_param('ShopCloseWarn',ShopCloseWarn)

	def get_Bid(self):
		return self.get_query_params().get('Bid')

	def set_Bid(self,Bid):
		self.add_query_param('Bid',Bid)

	def get_ShopManager(self):
		return self.get_query_params().get('ShopManager')

	def set_ShopManager(self,ShopManager):
		self.add_query_param('ShopManager',ShopManager)

	def get_ShopBusinessHours(self):
		return self.get_query_params().get('ShopBusinessHours')

	def set_ShopBusinessHours(self,ShopBusinessHours):
		self.add_query_param('ShopBusinessHours',ShopBusinessHours)