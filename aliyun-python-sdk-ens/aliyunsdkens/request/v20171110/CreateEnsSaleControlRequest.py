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
import json

class CreateEnsSaleControlRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'CreateEnsSaleControl','ens')
		self.set_method('POST')

	def get_SaleControls(self): # Array
		return self.get_query_params().get('SaleControls')

	def set_SaleControls(self, SaleControls):  # Array
		self.add_query_param("SaleControls", json.dumps(SaleControls))
	def get_CustomAccount(self): # String
		return self.get_query_params().get('CustomAccount')

	def set_CustomAccount(self, CustomAccount):  # String
		self.add_query_param('CustomAccount', CustomAccount)
	def get_CommodityCode(self): # String
		return self.get_query_params().get('CommodityCode')

	def set_CommodityCode(self, CommodityCode):  # String
		self.add_query_param('CommodityCode', CommodityCode)
	def get_AliUidAccount(self): # String
		return self.get_query_params().get('AliUidAccount')

	def set_AliUidAccount(self, AliUidAccount):  # String
		self.add_query_param('AliUidAccount', AliUidAccount)
