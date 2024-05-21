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
class SaveApgroupConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'SaveApgroupConfig','cloudwf')

	def get_Country(self):
		return self.get_query_params().get('Country')

	def set_Country(self,Country):
		self.add_query_param('Country',Country)

	def get_LogLevel(self):
		return self.get_query_params().get('LogLevel')

	def set_LogLevel(self,LogLevel):
		self.add_query_param('LogLevel',LogLevel)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_EchoInt(self):
		return self.get_query_params().get('EchoInt')

	def set_EchoInt(self,EchoInt):
		self.add_query_param('EchoInt',EchoInt)

	def get_Scan(self):
		return self.get_query_params().get('Scan')

	def set_Scan(self,Scan):
		self.add_query_param('Scan',Scan)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_Dai(self):
		return self.get_query_params().get('Dai')

	def set_Dai(self,Dai):
		self.add_query_param('Dai',Dai)

	def get_LogIp(self):
		return self.get_query_params().get('LogIp')

	def set_LogIp(self,LogIp):
		self.add_query_param('LogIp',LogIp)