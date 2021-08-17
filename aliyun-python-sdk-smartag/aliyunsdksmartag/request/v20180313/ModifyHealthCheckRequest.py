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

class ModifyHealthCheckRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'ModifyHealthCheck','smartag')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProbeInterval(self): # Integer
		return self.get_query_params().get('ProbeInterval')

	def set_ProbeInterval(self, ProbeInterval):  # Integer
		self.add_query_param('ProbeInterval', ProbeInterval)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_DstPort(self): # Integer
		return self.get_query_params().get('DstPort')

	def set_DstPort(self, DstPort):  # Integer
		self.add_query_param('DstPort', DstPort)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_HcInstanceId(self): # String
		return self.get_query_params().get('HcInstanceId')

	def set_HcInstanceId(self, HcInstanceId):  # String
		self.add_query_param('HcInstanceId', HcInstanceId)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_FailCountThreshold(self): # Integer
		return self.get_query_params().get('FailCountThreshold')

	def set_FailCountThreshold(self, FailCountThreshold):  # Integer
		self.add_query_param('FailCountThreshold', FailCountThreshold)
	def get_ProbeTimeout(self): # Integer
		return self.get_query_params().get('ProbeTimeout')

	def set_ProbeTimeout(self, ProbeTimeout):  # Integer
		self.add_query_param('ProbeTimeout', ProbeTimeout)
	def get_RttFailThreshold(self): # Integer
		return self.get_query_params().get('RttFailThreshold')

	def set_RttFailThreshold(self, RttFailThreshold):  # Integer
		self.add_query_param('RttFailThreshold', RttFailThreshold)
	def get_RttThreshold(self): # Integer
		return self.get_query_params().get('RttThreshold')

	def set_RttThreshold(self, RttThreshold):  # Integer
		self.add_query_param('RttThreshold', RttThreshold)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_DstIpAddr(self): # String
		return self.get_query_params().get('DstIpAddr')

	def set_DstIpAddr(self, DstIpAddr):  # String
		self.add_query_param('DstIpAddr', DstIpAddr)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SrcIpAddr(self): # String
		return self.get_query_params().get('SrcIpAddr')

	def set_SrcIpAddr(self, SrcIpAddr):  # String
		self.add_query_param('SrcIpAddr', SrcIpAddr)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_SmartAGId(self): # String
		return self.get_query_params().get('SmartAGId')

	def set_SmartAGId(self, SmartAGId):  # String
		self.add_query_param('SmartAGId', SmartAGId)
	def get_SrcPort(self): # Integer
		return self.get_query_params().get('SrcPort')

	def set_SrcPort(self, SrcPort):  # Integer
		self.add_query_param('SrcPort', SrcPort)
	def get_ProbeCount(self): # Integer
		return self.get_query_params().get('ProbeCount')

	def set_ProbeCount(self, ProbeCount):  # Integer
		self.add_query_param('ProbeCount', ProbeCount)
