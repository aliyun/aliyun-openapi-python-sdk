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
from aliyunsdksmartag.endpoint import endpoint_data

class ModifySagLanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'ModifySagLan','smartag')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EndIp(self): # String
		return self.get_query_params().get('EndIp')

	def set_EndIp(self, EndIp):  # String
		self.add_query_param('EndIp', EndIp)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_Mask(self): # String
		return self.get_query_params().get('Mask')

	def set_Mask(self, Mask):  # String
		self.add_query_param('Mask', Mask)
	def get_StartIp(self): # String
		return self.get_query_params().get('StartIp')

	def set_StartIp(self, StartIp):  # String
		self.add_query_param('StartIp', StartIp)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_IP(self): # String
		return self.get_query_params().get('IP')

	def set_IP(self, IP):  # String
		self.add_query_param('IP', IP)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_IPType(self): # String
		return self.get_query_params().get('IPType')

	def set_IPType(self, IPType):  # String
		self.add_query_param('IPType', IPType)
	def get_SmartAGId(self): # String
		return self.get_query_params().get('SmartAGId')

	def set_SmartAGId(self, SmartAGId):  # String
		self.add_query_param('SmartAGId', SmartAGId)
	def get_SmartAGSn(self): # String
		return self.get_query_params().get('SmartAGSn')

	def set_SmartAGSn(self, SmartAGSn):  # String
		self.add_query_param('SmartAGSn', SmartAGSn)
	def get_PortName(self): # String
		return self.get_query_params().get('PortName')

	def set_PortName(self, PortName):  # String
		self.add_query_param('PortName', PortName)
	def get_Lease(self): # String
		return self.get_query_params().get('Lease')

	def set_Lease(self, Lease):  # String
		self.add_query_param('Lease', Lease)
