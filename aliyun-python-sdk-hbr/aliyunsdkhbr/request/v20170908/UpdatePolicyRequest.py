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
class UpdatePolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdatePolicy','hbr')
		self.set_protocol_type('https')

	def get_Schedule(self):
		return self.get_query_params().get('Schedule')

	def set_Schedule(self,Schedule):
		self.add_query_param('Schedule',Schedule)

	def get_ClientId(self):
		return self.get_query_params().get('ClientId')

	def set_ClientId(self,ClientId):
		self.add_query_param('ClientId',ClientId)

	def get_PolicyId(self):
		return self.get_query_params().get('PolicyId')

	def set_PolicyId(self,PolicyId):
		self.add_query_param('PolicyId',PolicyId)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_LastRunTime(self):
		return self.get_query_params().get('LastRunTime')

	def set_LastRunTime(self,LastRunTime):
		self.add_query_param('LastRunTime',LastRunTime)

	def get_PolicyName(self):
		return self.get_query_params().get('PolicyName')

	def set_PolicyName(self,PolicyName):
		self.add_query_param('PolicyName',PolicyName)

	def get_Source(self):
		return self.get_query_params().get('Source')

	def set_Source(self,Source):
		self.add_query_param('Source',Source)

	def get_Retention(self):
		return self.get_query_params().get('Retention')

	def set_Retention(self,Retention):
		self.add_query_param('Retention',Retention)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)