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
class CreateSubAccountPermissionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'CreateSubAccountPermission','cloudwf')

	def get_Uid(self):
		return self.get_query_params().get('Uid')

	def set_Uid(self,Uid):
		self.add_query_param('Uid',Uid)

	def get_ShopGroupIdss(self):
		return self.get_query_params().get('ShopGroupIdss')

	def set_ShopGroupIdss(self,ShopGroupIdss):
		for i in range(len(ShopGroupIdss)):	
			if ShopGroupIdss[i] is not None:
				self.add_query_param('ShopGroupIds.' + str(i + 1) , ShopGroupIdss[i]);

	def get_ShopIdss(self):
		return self.get_query_params().get('ShopIdss')

	def set_ShopIdss(self,ShopIdss):
		for i in range(len(ShopIdss)):	
			if ShopIdss[i] is not None:
				self.add_query_param('ShopIds.' + str(i + 1) , ShopIdss[i]);

	def get_PagePermission(self):
		return self.get_query_params().get('PagePermission')

	def set_PagePermission(self,PagePermission):
		self.add_query_param('PagePermission',PagePermission)

	def get_PermissionType(self):
		return self.get_query_params().get('PermissionType')

	def set_PermissionType(self,PermissionType):
		self.add_query_param('PermissionType',PermissionType)

	def get_BusinessIdss(self):
		return self.get_query_params().get('BusinessIdss')

	def set_BusinessIdss(self,BusinessIdss):
		for i in range(len(BusinessIdss)):	
			if BusinessIdss[i] is not None:
				self.add_query_param('BusinessIds.' + str(i + 1) , BusinessIdss[i]);