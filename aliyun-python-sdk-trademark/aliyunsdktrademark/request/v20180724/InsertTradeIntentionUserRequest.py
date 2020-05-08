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
class InsertTradeIntentionUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Trademark', '2018-07-24', 'InsertTradeIntentionUser','trademark')

	def get_Mobile(self):
		return self.get_query_params().get('Mobile')

	def set_Mobile(self,Mobile):
		self.add_query_param('Mobile',Mobile)

	def get_PartnerCode(self):
		return self.get_query_params().get('PartnerCode')

	def set_PartnerCode(self,PartnerCode):
		self.add_query_param('PartnerCode',PartnerCode)

	def get_Classification(self):
		return self.get_query_params().get('Classification')

	def set_Classification(self,Classification):
		self.add_query_param('Classification',Classification)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_RegisterNumber(self):
		return self.get_query_params().get('RegisterNumber')

	def set_RegisterNumber(self,RegisterNumber):
		self.add_query_param('RegisterNumber',RegisterNumber)

	def get_Vcode(self):
		return self.get_query_params().get('Vcode')

	def set_Vcode(self,Vcode):
		self.add_query_param('Vcode',Vcode)

	def get_UserName(self):
		return self.get_query_params().get('UserName')

	def set_UserName(self,UserName):
		self.add_query_param('UserName',UserName)