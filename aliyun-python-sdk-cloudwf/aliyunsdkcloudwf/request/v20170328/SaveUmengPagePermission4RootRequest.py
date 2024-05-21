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
class SaveUmengPagePermission4RootRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'SaveUmengPagePermission4Root','cloudwf')

	def get_GsPermission(self):
		return self.get_query_params().get('GsPermission')

	def set_GsPermission(self,GsPermission):
		self.add_query_param('GsPermission',GsPermission)

	def get_AliyunPk(self):
		return self.get_query_params().get('AliyunPk')

	def set_AliyunPk(self,AliyunPk):
		self.add_query_param('AliyunPk',AliyunPk)

	def get_PagePermission(self):
		return self.get_query_params().get('PagePermission')

	def set_PagePermission(self,PagePermission):
		self.add_query_param('PagePermission',PagePermission)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_Bid(self):
		return self.get_query_params().get('Bid')

	def set_Bid(self,Bid):
		self.add_query_param('Bid',Bid)