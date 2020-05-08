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
class CombineLoaRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Trademark', '2018-07-24', 'CombineLoa','trademark')

	def get_TrademarkName(self):
		return self.get_query_params().get('TrademarkName')

	def set_TrademarkName(self,TrademarkName):
		self.add_query_param('TrademarkName',TrademarkName)

	def get_MaterialName(self):
		return self.get_query_params().get('MaterialName')

	def set_MaterialName(self,MaterialName):
		self.add_query_param('MaterialName',MaterialName)

	def get_Address(self):
		return self.get_query_params().get('Address')

	def set_Address(self,Address):
		self.add_query_param('Address',Address)

	def get_Nationality(self):
		return self.get_query_params().get('Nationality')

	def set_Nationality(self,Nationality):
		self.add_query_param('Nationality',Nationality)

	def get_TmProduceType(self):
		return self.get_query_params().get('TmProduceType')

	def set_TmProduceType(self,TmProduceType):
		self.add_query_param('TmProduceType',TmProduceType)

	def get_MaterialId(self):
		return self.get_query_params().get('MaterialId')

	def set_MaterialId(self,MaterialId):
		self.add_query_param('MaterialId',MaterialId)