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
class BindEslDeviceShelfRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2018-08-01', 'BindEslDeviceShelf')

	def get_ShelfCode(self):
		return self.get_query_params().get('ShelfCode')

	def set_ShelfCode(self,ShelfCode):
		self.add_query_param('ShelfCode',ShelfCode)

	def get_EslBarCode(self):
		return self.get_query_params().get('EslBarCode')

	def set_EslBarCode(self,EslBarCode):
		self.add_query_param('EslBarCode',EslBarCode)

	def get_StoreId(self):
		return self.get_query_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_query_param('StoreId',StoreId)