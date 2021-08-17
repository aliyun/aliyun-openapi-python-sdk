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

class ModifyDeviceAutoUpgradePolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'ModifyDeviceAutoUpgradePolicy','smartag')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_CronExpression(self): # String
		return self.get_query_params().get('CronExpression')

	def set_CronExpression(self, CronExpression):  # String
		self.add_query_param('CronExpression', CronExpression)
	def get_TimeZone(self): # String
		return self.get_query_params().get('TimeZone')

	def set_TimeZone(self, TimeZone):  # String
		self.add_query_param('TimeZone', TimeZone)
	def get_UpgradeType(self): # String
		return self.get_query_params().get('UpgradeType')

	def set_UpgradeType(self, UpgradeType):  # String
		self.add_query_param('UpgradeType', UpgradeType)
	def get_Duration(self): # Integer
		return self.get_query_params().get('Duration')

	def set_Duration(self, Duration):  # Integer
		self.add_query_param('Duration', Duration)
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
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_VersionType(self): # String
		return self.get_query_params().get('VersionType')

	def set_VersionType(self, VersionType):  # String
		self.add_query_param('VersionType', VersionType)
	def get_SmartAGId(self): # String
		return self.get_query_params().get('SmartAGId')

	def set_SmartAGId(self, SmartAGId):  # String
		self.add_query_param('SmartAGId', SmartAGId)
