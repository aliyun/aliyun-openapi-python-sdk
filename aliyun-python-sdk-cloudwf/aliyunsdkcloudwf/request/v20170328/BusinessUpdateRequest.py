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
class BusinessUpdateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'BusinessUpdate','cloudwf')

	def get_Warn(self):
		return self.get_query_params().get('Warn')

	def set_Warn(self,Warn):
		self.add_query_param('Warn',Warn)

	def get_BusinessCity(self):
		return self.get_query_params().get('BusinessCity')

	def set_BusinessCity(self,BusinessCity):
		self.add_query_param('BusinessCity',BusinessCity)

	def get_WarnEmail(self):
		return self.get_query_params().get('WarnEmail')

	def set_WarnEmail(self,WarnEmail):
		self.add_query_param('WarnEmail',WarnEmail)

	def get_BusinessAddress(self):
		return self.get_query_params().get('BusinessAddress')

	def set_BusinessAddress(self,BusinessAddress):
		self.add_query_param('BusinessAddress',BusinessAddress)

	def get_Bid(self):
		return self.get_query_params().get('Bid')

	def set_Bid(self,Bid):
		self.add_query_param('Bid',Bid)

	def get_BusinessManager(self):
		return self.get_query_params().get('BusinessManager')

	def set_BusinessManager(self,BusinessManager):
		self.add_query_param('BusinessManager',BusinessManager)

	def get_BusinessProvince(self):
		return self.get_query_params().get('BusinessProvince')

	def set_BusinessProvince(self,BusinessProvince):
		self.add_query_param('BusinessProvince',BusinessProvince)