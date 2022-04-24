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

class DescribeForwardTableEntriesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribeForwardTableEntries','ens')
		self.set_method('POST')

	def get_InternalIp(self): # String
		return self.get_query_params().get('InternalIp')

	def set_InternalIp(self, InternalIp):  # String
		self.add_query_param('InternalIp', InternalIp)
	def get_ExternalIp(self): # String
		return self.get_query_params().get('ExternalIp')

	def set_ExternalIp(self, ExternalIp):  # String
		self.add_query_param('ExternalIp', ExternalIp)
	def get_IpProtocol(self): # String
		return self.get_query_params().get('IpProtocol')

	def set_IpProtocol(self, IpProtocol):  # String
		self.add_query_param('IpProtocol', IpProtocol)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_ForwardEntryId(self): # String
		return self.get_query_params().get('ForwardEntryId')

	def set_ForwardEntryId(self, ForwardEntryId):  # String
		self.add_query_param('ForwardEntryId', ForwardEntryId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_NatGatewayId(self): # String
		return self.get_query_params().get('NatGatewayId')

	def set_NatGatewayId(self, NatGatewayId):  # String
		self.add_query_param('NatGatewayId', NatGatewayId)
	def get_ForwardEntryName(self): # String
		return self.get_query_params().get('ForwardEntryName')

	def set_ForwardEntryName(self, ForwardEntryName):  # String
		self.add_query_param('ForwardEntryName', ForwardEntryName)
