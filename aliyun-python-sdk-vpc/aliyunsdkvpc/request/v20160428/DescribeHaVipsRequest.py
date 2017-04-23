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
class DescribeHaVipsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'DescribeHaVips','vpc')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def  set_Filter_1_Key(self, Filter_1_Key):
		self.add_query_param('Filter.1.Key', Filter_1_Key)

	def  get_Filter_1_Key(self):
		self.get_query_params().get('Filter.1.Key')

	def  set_Filter_2_Key(self, Filter_2_Key):
		self.add_query_param('Filter.2.Key', Filter_2_Key)

	def  get_Filter_2_Key(self):
		self.get_query_params().get('Filter.2.Key')

	def  set_Filter_3_Key(self, Filter_3_Key):
		self.add_query_param('Filter.3.Key', Filter_3_Key)

	def  get_Filter_3_Key(self):
		self.get_query_params().get('Filter.3.Key')

	def  set_Filter_4_Key(self, Filter_4_Key):
		self.add_query_param('Filter.4.Key', Filter_4_Key)

	def  get_Filter_4_Key(self):
		self.get_query_params().get('Filter.4.Key')

	def  set_Filter_1_Value_1(self, Filter_1_Value_1):
		self.add_query_param('Filter.1.Value.1', Filter_1_Value_1)

	def  get_Filter_1_Value_1(self):
		self.get_query_params().get('Filter.1.Value.1')

	def  set_Filter_1_Value_2(self, Filter_1_Value_2):
		self.add_query_param('Filter.1.Value.2', Filter_1_Value_2)

	def  get_Filter_1_Value_2(self):
		self.get_query_params().get('Filter.1.Value.2')

	def  set_Filter_1_Value_3(self, Filter_1_Value_3):
		self.add_query_param('Filter.1.Value.3', Filter_1_Value_3)

	def  get_Filter_1_Value_3(self):
		self.get_query_params().get('Filter.1.Value.3')

	def  set_Filter_1_Value_4(self, Filter_1_Value_4):
		self.add_query_param('Filter.1.Value.4', Filter_1_Value_4)

	def  get_Filter_1_Value_4(self):
		self.get_query_params().get('Filter.1.Value.4')

	def  set_Filter_2_Value_1(self, Filter_2_Value_1):
		self.add_query_param('Filter.2.Value.1', Filter_2_Value_1)

	def  get_Filter_2_Value_1(self):
		self.get_query_params().get('Filter.2.Value.1')

	def  set_Filter_2_Value_2(self, Filter_2_Value_2):
		self.add_query_param('Filter.2.Value.2', Filter_2_Value_2)

	def  get_Filter_2_Value_2(self):
		self.get_query_params().get('Filter.2.Value.2')

	def  set_Filter_2_Value_3(self, Filter_2_Value_3):
		self.add_query_param('Filter.2.Value.3', Filter_2_Value_3)

	def  get_Filter_2_Value_3(self):
		self.get_query_params().get('Filter.2.Value.3')

	def  set_Filter_2_Value_4(self, Filter_2_Value_4):
		self.add_query_param('Filter.2.Value.4', Filter_2_Value_4)

	def  get_Filter_2_Value_4(self):
		self.get_query_params().get('Filter.2.Value.4')

	def  set_Filter_3_Value_1(self, Filter_3_Value_1):
		self.add_query_param('Filter.3.Value.1', Filter_3_Value_1)

	def  get_Filter_3_Value_1(self):
		self.get_query_params().get('Filter.3.Value.1')

	def  set_Filter_3_Value_2(self, Filter_3_Value_2):
		self.add_query_param('Filter.3.Value.2', Filter_3_Value_2)

	def  get_Filter_3_Value_2(self):
		self.get_query_params().get('Filter.3.Value.2')

	def  set_Filter_3_Value_3(self, Filter_3_Value_3):
		self.add_query_param('Filter.3.Value.3', Filter_3_Value_3)

	def  get_Filter_3_Value_3(self):
		self.get_query_params().get('Filter.3.Value.3')

	def  set_Filter_3_Value_4(self, Filter_3_Value_4):
		self.add_query_param('Filter.3.Value.4', Filter_3_Value_4)

	def  get_Filter_3_Value_4(self):
		self.get_query_params().get('Filter.3.Value.4')

	def  set_Filter_4_Value_1(self, Filter_4_Value_1):
		self.add_query_param('Filter.4.Value.1', Filter_4_Value_1)

	def  get_Filter_4_Value_1(self):
		self.get_query_params().get('Filter.4.Value.1')

	def  set_Filter_4_Value_2(self, Filter_4_Value_2):
		self.add_query_param('Filter.4.Value.2', Filter_4_Value_2)

	def  get_Filter_4_Value_2(self):
		self.get_query_params().get('Filter.4.Value.2')

	def  set_Filter_4_Value_3(self, Filter_4_Value_3):
		self.add_query_param('Filter.4.Value.3', Filter_4_Value_3)

	def  get_Filter_4_Value_3(self):
		self.get_query_params().get('Filter.4.Value.3')

	def  set_Filter_4_Value_4(self, Filter_4_Value_4):
		self.add_query_param('Filter.4.Value.4', Filter_4_Value_4)

	def  get_Filter_4_Value_4(self):
		self.get_query_params().get('Filter.4.Value.4')

