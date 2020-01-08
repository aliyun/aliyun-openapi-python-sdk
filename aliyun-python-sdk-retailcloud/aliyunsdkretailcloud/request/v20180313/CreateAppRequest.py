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

class CreateAppRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'CreateApp','retailcloud')
		self.set_method('POST')

	def get_BizTitle(self):
		return self.get_body_params().get('BizTitle')

	def set_BizTitle(self,BizTitle):
		self.add_body_params('BizTitle', BizTitle)

	def get_StateType(self):
		return self.get_body_params().get('StateType')

	def set_StateType(self,StateType):
		self.add_body_params('StateType', StateType)

	def get_ServiceType(self):
		return self.get_body_params().get('ServiceType')

	def set_ServiceType(self,ServiceType):
		self.add_body_params('ServiceType', ServiceType)

	def get_BizCode(self):
		return self.get_body_params().get('BizCode')

	def set_BizCode(self,BizCode):
		self.add_body_params('BizCode', BizCode)

	def get_OperatingSystem(self):
		return self.get_body_params().get('OperatingSystem')

	def set_OperatingSystem(self,OperatingSystem):
		self.add_body_params('OperatingSystem', OperatingSystem)

	def get_Description(self):
		return self.get_body_params().get('Description')

	def set_Description(self,Description):
		self.add_body_params('Description', Description)

	def get_Language(self):
		return self.get_body_params().get('Language')

	def set_Language(self,Language):
		self.add_body_params('Language', Language)

	def get_Title(self):
		return self.get_body_params().get('Title')

	def set_Title(self,Title):
		self.add_body_params('Title', Title)