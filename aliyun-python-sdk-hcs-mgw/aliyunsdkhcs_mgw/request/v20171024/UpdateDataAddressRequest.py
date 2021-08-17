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

class UpdateDataAddressRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hcs-mgw', '2017-10-24', 'UpdateDataAddress')
		self.set_method('POST')

	def get_ServerEncryption(self):
		return self.get_query_params().get('ServerEncryption')

	def set_ServerEncryption(self,ServerEncryption):
		self.add_query_param('ServerEncryption',ServerEncryption)

	def get_AccessMethod(self):
		return self.get_query_params().get('AccessMethod')

	def set_AccessMethod(self,AccessMethod):
		self.add_query_param('AccessMethod',AccessMethod)

	def get_AccessKeySecret(self):
		return self.get_query_params().get('AccessKeySecret')

	def set_AccessKeySecret(self,AccessKeySecret):
		self.add_query_param('AccessKeySecret',AccessKeySecret)

	def get_ListFilePath(self):
		return self.get_query_params().get('ListFilePath')

	def set_ListFilePath(self,ListFilePath):
		self.add_query_param('ListFilePath',ListFilePath)

	def get_AccessKey(self):
		return self.get_query_params().get('AccessKey')

	def set_AccessKey(self,AccessKey):
		self.add_query_param('AccessKey',AccessKey)

	def get_AddressType(self):
		return self.get_query_params().get('AddressType')

	def set_AddressType(self,AddressType):
		self.add_query_param('AddressType',AddressType)

	def get_Address(self):
		return self.get_query_params().get('Address')

	def set_Address(self,Address):
		self.add_query_param('Address',Address)

	def get_AccessProxy(self):
		return self.get_query_params().get('AccessProxy')

	def set_AccessProxy(self,AccessProxy):
		self.add_query_param('AccessProxy',AccessProxy)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_Domain(self):
		return self.get_query_params().get('Domain')

	def set_Domain(self,Domain):
		self.add_query_param('Domain',Domain)

	def get_Appid(self):
		return self.get_query_params().get('Appid')

	def set_Appid(self,Appid):
		self.add_query_param('Appid',Appid)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_MgwRegionId(self):
		return self.get_query_params().get('MgwRegionId')

	def set_MgwRegionId(self,MgwRegionId):
		self.add_query_param('MgwRegionId',MgwRegionId)

	def get_SubAddress(self):
		return self.get_query_params().get('SubAddress')

	def set_SubAddress(self,SubAddress):
		self.add_query_param('SubAddress',SubAddress)