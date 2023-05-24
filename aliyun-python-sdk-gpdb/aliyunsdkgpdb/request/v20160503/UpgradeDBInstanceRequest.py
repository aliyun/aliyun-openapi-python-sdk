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
from aliyunsdkgpdb.endpoint import endpoint_data

class UpgradeDBInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'UpgradeDBInstance')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_InstanceSpec(self): # String
		return self.get_query_params().get('InstanceSpec')

	def set_InstanceSpec(self, InstanceSpec):  # String
		self.add_query_param('InstanceSpec', InstanceSpec)
	def get_StorageSize(self): # String
		return self.get_query_params().get('StorageSize')

	def set_StorageSize(self, StorageSize):  # String
		self.add_query_param('StorageSize', StorageSize)
	def get_SegStorageType(self): # String
		return self.get_query_params().get('SegStorageType')

	def set_SegStorageType(self, SegStorageType):  # String
		self.add_query_param('SegStorageType', SegStorageType)
	def get_MasterNodeNum(self): # String
		return self.get_query_params().get('MasterNodeNum')

	def set_MasterNodeNum(self, MasterNodeNum):  # String
		self.add_query_param('MasterNodeNum', MasterNodeNum)
	def get_UpgradeType(self): # Long
		return self.get_query_params().get('UpgradeType')

	def set_UpgradeType(self, UpgradeType):  # Long
		self.add_query_param('UpgradeType', UpgradeType)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_SegNodeNum(self): # String
		return self.get_query_params().get('SegNodeNum')

	def set_SegNodeNum(self, SegNodeNum):  # String
		self.add_query_param('SegNodeNum', SegNodeNum)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_DBInstanceGroupCount(self): # String
		return self.get_query_params().get('DBInstanceGroupCount')

	def set_DBInstanceGroupCount(self, DBInstanceGroupCount):  # String
		self.add_query_param('DBInstanceGroupCount', DBInstanceGroupCount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SegDiskPerformanceLevel(self): # String
		return self.get_query_params().get('SegDiskPerformanceLevel')

	def set_SegDiskPerformanceLevel(self, SegDiskPerformanceLevel):  # String
		self.add_query_param('SegDiskPerformanceLevel', SegDiskPerformanceLevel)
	def get_DBInstanceClass(self): # String
		return self.get_query_params().get('DBInstanceClass')

	def set_DBInstanceClass(self, DBInstanceClass):  # String
		self.add_query_param('DBInstanceClass', DBInstanceClass)
	def get_PayType(self): # String
		return self.get_query_params().get('PayType')

	def set_PayType(self, PayType):  # String
		self.add_query_param('PayType', PayType)
