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
class CreateFpgaImageTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'faas', '2017-08-24', 'CreateFpgaImageTask')
		self.set_method('POST')

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_KeyId(self):
		return self.get_query_params().get('KeyId')

	def set_KeyId(self,KeyId):
		self.add_query_param('KeyId',KeyId)

	def get_ShellUUID(self):
		return self.get_query_params().get('ShellUUID')

	def set_ShellUUID(self,ShellUUID):
		self.add_query_param('ShellUUID',ShellUUID)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_query_param('Tags',Tags)

	def get_Bucket(self):
		return self.get_query_params().get('Bucket')

	def set_Bucket(self,Bucket):
		self.add_query_param('Bucket',Bucket)

	def get_Encrypted(self):
		return self.get_query_params().get('Encrypted')

	def set_Encrypted(self,Encrypted):
		self.add_query_param('Encrypted',Encrypted)

	def get_RoleArn(self):
		return self.get_query_params().get('RoleArn')

	def set_RoleArn(self,RoleArn):
		self.add_query_param('RoleArn',RoleArn)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_FpgaType(self):
		return self.get_query_params().get('FpgaType')

	def set_FpgaType(self,FpgaType):
		self.add_query_param('FpgaType',FpgaType)

	def get_Email(self):
		return self.get_query_params().get('Email')

	def set_Email(self,Email):
		self.add_query_param('Email',Email)

	def get_Object(self):
		return self.get_query_params().get('Object')

	def set_Object(self,Object):
		self.add_query_param('Object',Object)