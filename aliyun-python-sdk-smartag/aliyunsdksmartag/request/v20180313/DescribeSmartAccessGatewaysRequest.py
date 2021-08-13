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

class DescribeSmartAccessGatewaysRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'DescribeSmartAccessGateways','smartag')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_AclIds(self): # String
		return self.get_query_params().get('AclIds')

	def set_AclIds(self, AclIds):  # String
		self.add_query_param('AclIds', AclIds)
	def get_CanAssociateQos(self): # Boolean
		return self.get_query_params().get('CanAssociateQos')

	def set_CanAssociateQos(self, CanAssociateQos):  # Boolean
		self.add_query_param('CanAssociateQos', CanAssociateQos)
	def get_SoftwareVersion(self): # String
		return self.get_query_params().get('SoftwareVersion')

	def set_SoftwareVersion(self, SoftwareVersion):  # String
		self.add_query_param('SoftwareVersion', SoftwareVersion)
	def get_UnboundAclIds(self): # String
		return self.get_query_params().get('UnboundAclIds')

	def set_UnboundAclIds(self, UnboundAclIds):  # String
		self.add_query_param('UnboundAclIds', UnboundAclIds)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_VersionComparator(self): # String
		return self.get_query_params().get('VersionComparator')

	def set_VersionComparator(self, VersionComparator):  # String
		self.add_query_param('VersionComparator', VersionComparator)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_HardwareType(self): # String
		return self.get_query_params().get('HardwareType')

	def set_HardwareType(self, HardwareType):  # String
		self.add_query_param('HardwareType', HardwareType)
	def get_SmartAGIdss(self): # RepeatList
		return self.get_query_params().get('SmartAGIds')

	def set_SmartAGIdss(self, SmartAGIds):  # RepeatList
		pass
	def get_SerialNumber(self): # String
		return self.get_query_params().get('SerialNumber')

	def set_SerialNumber(self, SerialNumber):  # String
		self.add_query_param('SerialNumber', SerialNumber)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_AssociatedCcnId(self): # String
		return self.get_query_params().get('AssociatedCcnId')

	def set_AssociatedCcnId(self, AssociatedCcnId):  # String
		self.add_query_param('AssociatedCcnId', AssociatedCcnId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_BusinessState(self): # String
		return self.get_query_params().get('BusinessState')

	def set_BusinessState(self, BusinessState):  # String
		self.add_query_param('BusinessState', BusinessState)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_SmartAGId(self): # String
		return self.get_query_params().get('SmartAGId')

	def set_SmartAGId(self, SmartAGId):  # String
		self.add_query_param('SmartAGId', SmartAGId)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
