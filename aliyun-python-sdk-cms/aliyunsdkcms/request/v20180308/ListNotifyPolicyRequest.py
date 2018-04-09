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
class ListNotifyPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2018-03-08', 'ListNotifyPolicy','cms')

	def get_PolicyType(self):
		return self.get_query_params().get('PolicyType')

	def set_PolicyType(self,PolicyType):
		self.add_query_param('PolicyType',PolicyType)

	def get_AlertName(self):
		return self.get_query_params().get('AlertName')

	def set_AlertName(self,AlertName):
		self.add_query_param('AlertName',AlertName)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_Dimensions(self):
		return self.get_query_params().get('Dimensions')

	def set_Dimensions(self,Dimensions):
		self.add_query_param('Dimensions',Dimensions)