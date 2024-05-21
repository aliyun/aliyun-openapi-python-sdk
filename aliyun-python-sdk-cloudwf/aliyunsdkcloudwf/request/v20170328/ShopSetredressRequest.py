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
class ShopSetredressRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'ShopSetredress','cloudwf')

	def get_Workday(self):
		return self.get_query_params().get('Workday')

	def set_Workday(self,Workday):
		self.add_query_param('Workday',Workday)

	def get_Filterclose(self):
		return self.get_query_params().get('Filterclose')

	def set_Filterclose(self,Filterclose):
		self.add_query_param('Filterclose',Filterclose)

	def get_Minstoptime(self):
		return self.get_query_params().get('Minstoptime')

	def set_Minstoptime(self,Minstoptime):
		self.add_query_param('Minstoptime',Minstoptime)

	def get_Holiday(self):
		return self.get_query_params().get('Holiday')

	def set_Holiday(self,Holiday):
		self.add_query_param('Holiday',Holiday)

	def get_Hnum(self):
		return self.get_query_params().get('Hnum')

	def set_Hnum(self,Hnum):
		self.add_query_param('Hnum',Hnum)

	def get_Sid(self):
		return self.get_query_params().get('Sid')

	def set_Sid(self,Sid):
		self.add_query_param('Sid',Sid)

	def get_Clerk(self):
		return self.get_query_params().get('Clerk')

	def set_Clerk(self,Clerk):
		self.add_query_param('Clerk',Clerk)

	def get_Filterstate(self):
		return self.get_query_params().get('Filterstate')

	def set_Filterstate(self,Filterstate):
		self.add_query_param('Filterstate',Filterstate)

	def get_Wnum(self):
		return self.get_query_params().get('Wnum')

	def set_Wnum(self,Wnum):
		self.add_query_param('Wnum',Wnum)

	def get_State(self):
		return self.get_query_params().get('State')

	def set_State(self,State):
		self.add_query_param('State',State)

	def get_Crowdfixed(self):
		return self.get_query_params().get('Crowdfixed')

	def set_Crowdfixed(self,Crowdfixed):
		self.add_query_param('Crowdfixed',Crowdfixed)

	def get_Maxstoptime(self):
		return self.get_query_params().get('Maxstoptime')

	def set_Maxstoptime(self,Maxstoptime):
		self.add_query_param('Maxstoptime',Maxstoptime)