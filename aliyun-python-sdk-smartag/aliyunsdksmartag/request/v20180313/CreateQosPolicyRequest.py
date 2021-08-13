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

class CreateQosPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'CreateQosPolicy','smartag')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DpiGroupIdss(self): # RepeatList
		return self.get_query_params().get('DpiGroupIds')

	def set_DpiGroupIdss(self, DpiGroupIds):  # RepeatList
		pass
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_SourcePortRange(self): # String
		return self.get_query_params().get('SourcePortRange')

	def set_SourcePortRange(self, SourcePortRange):  # String
		self.add_query_param('SourcePortRange', SourcePortRange)
	def get_SourceCidr(self): # String
		return self.get_query_params().get('SourceCidr')

	def set_SourceCidr(self, SourceCidr):  # String
		self.add_query_param('SourceCidr', SourceCidr)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_DestCidr(self): # String
		return self.get_query_params().get('DestCidr')

	def set_DestCidr(self, DestCidr):  # String
		self.add_query_param('DestCidr', DestCidr)
	def get_DpiSignatureIdss(self): # RepeatList
		return self.get_query_params().get('DpiSignatureIds')

	def set_DpiSignatureIdss(self, DpiSignatureIds):  # RepeatList
		pass
	def get_QosId(self): # String
		return self.get_query_params().get('QosId')

	def set_QosId(self, QosId):  # String
		self.add_query_param('QosId', QosId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_IpProtocol(self): # String
		return self.get_query_params().get('IpProtocol')

	def set_IpProtocol(self, IpProtocol):  # String
		self.add_query_param('IpProtocol', IpProtocol)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Priority(self): # Integer
		return self.get_query_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_query_param('Priority', Priority)
	def get_DestPortRange(self): # String
		return self.get_query_params().get('DestPortRange')

	def set_DestPortRange(self, DestPortRange):  # String
		self.add_query_param('DestPortRange', DestPortRange)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
