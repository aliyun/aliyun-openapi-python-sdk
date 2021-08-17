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

class ModifySagWanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'ModifySagWan','smartag')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ISP(self): # String
		return self.get_query_params().get('ISP')

	def set_ISP(self, ISP):  # String
		self.add_query_param('ISP', ISP)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_Mask(self): # String
		return self.get_query_params().get('Mask')

	def set_Mask(self, Mask):  # String
		self.add_query_param('Mask', Mask)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_Bandwidth(self): # Integer
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self, Bandwidth):  # Integer
		self.add_query_param('Bandwidth', Bandwidth)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_IP(self): # String
		return self.get_query_params().get('IP')

	def set_IP(self, IP):  # String
		self.add_query_param('IP', IP)
	def get_Weight(self): # Integer
		return self.get_query_params().get('Weight')

	def set_Weight(self, Weight):  # Integer
		self.add_query_param('Weight', Weight)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_IPType(self): # String
		return self.get_query_params().get('IPType')

	def set_IPType(self, IPType):  # String
		self.add_query_param('IPType', IPType)
	def get_Priority(self): # Integer
		return self.get_query_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_query_param('Priority', Priority)
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
	def get_Gateway(self): # String
		return self.get_query_params().get('Gateway')

	def set_Gateway(self, Gateway):  # String
		self.add_query_param('Gateway', Gateway)
	def get_Username(self): # String
		return self.get_query_params().get('Username')

	def set_Username(self, Username):  # String
		self.add_query_param('Username', Username)
