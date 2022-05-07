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
from aliyunsdkvpc.endpoint import endpoint_data

class ModifyForwardEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ModifyForwardEntry','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ForwardTableId(self): # String
		return self.get_query_params().get('ForwardTableId')

	def set_ForwardTableId(self, ForwardTableId):  # String
		self.add_query_param('ForwardTableId', ForwardTableId)
	def get_InternalIp(self): # String
		return self.get_query_params().get('InternalIp')

	def set_InternalIp(self, InternalIp):  # String
		self.add_query_param('InternalIp', InternalIp)
	def get_ForwardEntryId(self): # String
		return self.get_query_params().get('ForwardEntryId')

	def set_ForwardEntryId(self, ForwardEntryId):  # String
		self.add_query_param('ForwardEntryId', ForwardEntryId)
	def get_ExternalIp(self): # String
		return self.get_query_params().get('ExternalIp')

	def set_ExternalIp(self, ExternalIp):  # String
		self.add_query_param('ExternalIp', ExternalIp)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_IpProtocol(self): # String
		return self.get_query_params().get('IpProtocol')

	def set_IpProtocol(self, IpProtocol):  # String
		self.add_query_param('IpProtocol', IpProtocol)
	def get_ForwardEntryName(self): # String
		return self.get_query_params().get('ForwardEntryName')

	def set_ForwardEntryName(self, ForwardEntryName):  # String
		self.add_query_param('ForwardEntryName', ForwardEntryName)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_InternalPort(self): # String
		return self.get_query_params().get('InternalPort')

	def set_InternalPort(self, InternalPort):  # String
		self.add_query_param('InternalPort', InternalPort)
	def get_PortBreak(self): # Boolean
		return self.get_query_params().get('PortBreak')

	def set_PortBreak(self, PortBreak):  # Boolean
		self.add_query_param('PortBreak', PortBreak)
	def get_ExternalPort(self): # String
		return self.get_query_params().get('ExternalPort')

	def set_ExternalPort(self, ExternalPort):  # String
		self.add_query_param('ExternalPort', ExternalPort)
