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
class AfsCheckRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'jaq', '2016-11-23', 'AfsCheck')

	def get_CallerName(self):
		return self.get_query_params().get('CallerName')

	def set_CallerName(self,CallerName):
		self.add_query_param('CallerName',CallerName)

	def get_Session(self):
		return self.get_query_params().get('Session')

	def set_Session(self,Session):
		self.add_query_param('Session',Session)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_Sig(self):
		return self.get_query_params().get('Sig')

	def set_Sig(self,Sig):
		self.add_query_param('Sig',Sig)

	def get_Platform(self):
		return self.get_query_params().get('Platform')

	def set_Platform(self,Platform):
		self.add_query_param('Platform',Platform)

	def get_Scene(self):
		return self.get_query_params().get('Scene')

	def set_Scene(self,Scene):
		self.add_query_param('Scene',Scene)