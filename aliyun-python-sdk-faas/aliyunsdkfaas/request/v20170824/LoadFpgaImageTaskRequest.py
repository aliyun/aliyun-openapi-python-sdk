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
class LoadFpgaImageTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'faas', '2017-08-24', 'LoadFpgaImageTask')
		self.set_method('POST')

	def get_FpgaImageType(self):
		return self.get_query_params().get('FpgaImageType')

	def set_FpgaImageType(self,FpgaImageType):
		self.add_query_param('FpgaImageType',FpgaImageType)

	def get_ShellUUID(self):
		return self.get_query_params().get('ShellUUID')

	def set_ShellUUID(self,ShellUUID):
		self.add_query_param('ShellUUID',ShellUUID)

	def get_OwnerAlias(self):
		return self.get_query_params().get('OwnerAlias')

	def set_OwnerAlias(self,OwnerAlias):
		self.add_query_param('OwnerAlias',OwnerAlias)

	def get_FpgaImageUUID(self):
		return self.get_query_params().get('FpgaImageUUID')

	def set_FpgaImageUUID(self,FpgaImageUUID):
		self.add_query_param('FpgaImageUUID',FpgaImageUUID)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_RoleArn(self):
		return self.get_query_params().get('RoleArn')

	def set_RoleArn(self,RoleArn):
		self.add_query_param('RoleArn',RoleArn)

	def get_FpgaType(self):
		return self.get_query_params().get('FpgaType')

	def set_FpgaType(self,FpgaType):
		self.add_query_param('FpgaType',FpgaType)

	def get_FpgaUUID(self):
		return self.get_query_params().get('FpgaUUID')

	def set_FpgaUUID(self,FpgaUUID):
		self.add_query_param('FpgaUUID',FpgaUUID)

	def get_Object(self):
		return self.get_query_params().get('Object')

	def set_Object(self,Object):
		self.add_query_param('Object',Object)