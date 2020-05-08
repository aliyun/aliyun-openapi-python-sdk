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
class MobileStartSpeedUpRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Snsuapi', '2018-07-09', 'MobileStartSpeedUp','snsuapi')

	def get_Duration(self):
		return self.get_query_params().get('Duration')

	def set_Duration(self,Duration):
		self.add_query_param('Duration',Duration)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_Ip(self):
		return self.get_query_params().get('Ip')

	def set_Ip(self,Ip):
		self.add_query_param('Ip',Ip)

	def get_DestinationIpAddress(self):
		return self.get_query_params().get('DestinationIpAddress')

	def set_DestinationIpAddress(self,DestinationIpAddress):
		self.add_query_param('DestinationIpAddress',DestinationIpAddress)

	def get_PublicIp(self):
		return self.get_query_params().get('PublicIp')

	def set_PublicIp(self,PublicIp):
		self.add_query_param('PublicIp',PublicIp)

	def get_PublicPort(self):
		return self.get_query_params().get('PublicPort')

	def set_PublicPort(self,PublicPort):
		self.add_query_param('PublicPort',PublicPort)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)