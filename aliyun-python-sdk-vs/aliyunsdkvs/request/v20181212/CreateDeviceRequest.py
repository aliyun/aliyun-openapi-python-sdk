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
from aliyunsdkvs.endpoint import endpoint_data

class CreateDeviceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vs', '2018-12-12', 'CreateDevice','vs')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_GbId(self):
		return self.get_query_params().get('GbId')

	def set_GbId(self,GbId):
		self.add_query_param('GbId',GbId)

	def get_Latitude(self):
		return self.get_query_params().get('Latitude')

	def set_Latitude(self,Latitude):
		self.add_query_param('Latitude',Latitude)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_AutoStart(self):
		return self.get_query_params().get('AutoStart')

	def set_AutoStart(self,AutoStart):
		self.add_query_param('AutoStart',AutoStart)

	def get_ParentId(self):
		return self.get_query_params().get('ParentId')

	def set_ParentId(self,ParentId):
		self.add_query_param('ParentId',ParentId)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_Vendor(self):
		return self.get_query_params().get('Vendor')

	def set_Vendor(self,Vendor):
		self.add_query_param('Vendor',Vendor)

	def get_DirectoryId(self):
		return self.get_query_params().get('DirectoryId')

	def set_DirectoryId(self,DirectoryId):
		self.add_query_param('DirectoryId',DirectoryId)

	def get_Longitude(self):
		return self.get_query_params().get('Longitude')

	def set_Longitude(self,Longitude):
		self.add_query_param('Longitude',Longitude)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_Ip(self):
		return self.get_query_params().get('Ip')

	def set_Ip(self,Ip):
		self.add_query_param('Ip',Ip)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Params(self):
		return self.get_query_params().get('Params')

	def set_Params(self,Params):
		self.add_query_param('Params',Params)

	def get_Url(self):
		return self.get_query_params().get('Url')

	def set_Url(self,Url):
		self.add_query_param('Url',Url)

	def get_Port(self):
		return self.get_query_params().get('Port')

	def set_Port(self,Port):
		self.add_query_param('Port',Port)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_PosInterval(self):
		return self.get_query_params().get('PosInterval')

	def set_PosInterval(self,PosInterval):
		self.add_query_param('PosInterval',PosInterval)

	def get_Dsn(self):
		return self.get_query_params().get('Dsn')

	def set_Dsn(self,Dsn):
		self.add_query_param('Dsn',Dsn)

	def get_Username(self):
		return self.get_query_params().get('Username')

	def set_Username(self,Username):
		self.add_query_param('Username',Username)

	def get_AutoPos(self):
		return self.get_query_params().get('AutoPos')

	def set_AutoPos(self,AutoPos):
		self.add_query_param('AutoPos',AutoPos)