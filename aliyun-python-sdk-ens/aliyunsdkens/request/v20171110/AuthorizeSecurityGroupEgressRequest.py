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

class AuthorizeSecurityGroupEgressRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'AuthorizeSecurityGroupEgress','ens')
		self.set_method('POST')

	def get_SourcePortRange(self): # String
		return self.get_query_params().get('SourcePortRange')

	def set_SourcePortRange(self, SourcePortRange):  # String
		self.add_query_param('SourcePortRange', SourcePortRange)
	def get_PortRange(self): # String
		return self.get_query_params().get('PortRange')

	def set_PortRange(self, PortRange):  # String
		self.add_query_param('PortRange', PortRange)
	def get_IpProtocol(self): # String
		return self.get_query_params().get('IpProtocol')

	def set_IpProtocol(self, IpProtocol):  # String
		self.add_query_param('IpProtocol', IpProtocol)
	def get_Priority(self): # Integer
		return self.get_query_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_query_param('Priority', Priority)
	def get_DestCidrIp(self): # String
		return self.get_query_params().get('DestCidrIp')

	def set_DestCidrIp(self, DestCidrIp):  # String
		self.add_query_param('DestCidrIp', DestCidrIp)
	def get_SecurityGroupId(self): # String
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self, SecurityGroupId):  # String
		self.add_query_param('SecurityGroupId', SecurityGroupId)
	def get_Policy(self): # String
		return self.get_query_params().get('Policy')

	def set_Policy(self, Policy):  # String
		self.add_query_param('Policy', Policy)
