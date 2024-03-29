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

class CreateVirtualClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hcs-mgw', '2017-10-24', 'CreateVirtualCluster')
		self.set_method('POST')

	def get_MasterPublicIp(self):
		return self.get_query_params().get('MasterPublicIp')

	def set_MasterPublicIp(self,MasterPublicIp):
		self.add_query_param('MasterPublicIp',MasterPublicIp)

	def get_MasterPrivateIp(self):
		return self.get_query_params().get('MasterPrivateIp')

	def set_MasterPrivateIp(self,MasterPrivateIp):
		self.add_query_param('MasterPrivateIp',MasterPrivateIp)

	def get_WorkersPrivateIp(self):
		return self.get_query_params().get('WorkersPrivateIp')

	def set_WorkersPrivateIp(self,WorkersPrivateIp):
		self.add_query_param('WorkersPrivateIp',WorkersPrivateIp)

	def get_UserNmae(self):
		return self.get_query_params().get('UserNmae')

	def set_UserNmae(self,UserNmae):
		self.add_query_param('UserNmae',UserNmae)

	def get_AliasName(self):
		return self.get_query_params().get('AliasName')

	def set_AliasName(self,AliasName):
		self.add_query_param('AliasName',AliasName)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_MachineId(self):
		return self.get_query_params().get('MachineId')

	def set_MachineId(self,MachineId):
		self.add_query_param('MachineId',MachineId)

	def get_Port(self):
		return self.get_query_params().get('Port')

	def set_Port(self,Port):
		self.add_query_param('Port',Port)