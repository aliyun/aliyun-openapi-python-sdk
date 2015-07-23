# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class RenewInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'RenewInstance')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_InternetMaxBandwidthOut(self):
		return self.get_query_params().get('InternetMaxBandwidthOut')

	def set_InternetMaxBandwidthOut(self,InternetMaxBandwidthOut):
		self.add_query_param('InternetMaxBandwidthOut',InternetMaxBandwidthOut)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_RebootTime(self):
		return self.get_query_params().get('RebootTime')

	def set_RebootTime(self,RebootTime):
		self.add_query_param('RebootTime',RebootTime)

	def get_CovertDiskPortable1DiskId(self):
		return self.get_query_params().get('CovertDiskPortable1DiskId')

	def set_CovertDiskPortable1DiskId(self,CovertDiskPortable1DiskId):
		self.add_query_param('CovertDiskPortable1DiskId',CovertDiskPortable1DiskId)

	def get_CovertDiskPortable2DiskId(self):
		return self.get_query_params().get('CovertDiskPortable2DiskId')

	def set_CovertDiskPortable2DiskId(self,CovertDiskPortable2DiskId):
		self.add_query_param('CovertDiskPortable2DiskId',CovertDiskPortable2DiskId)

	def get_CovertDiskPortable3DiskId(self):
		return self.get_query_params().get('CovertDiskPortable3DiskId')

	def set_CovertDiskPortable3DiskId(self,CovertDiskPortable3DiskId):
		self.add_query_param('CovertDiskPortable3DiskId',CovertDiskPortable3DiskId)

	def get_CovertDiskPortable4DiskId(self):
		return self.get_query_params().get('CovertDiskPortable4DiskId')

	def set_CovertDiskPortable4DiskId(self,CovertDiskPortable4DiskId):
		self.add_query_param('CovertDiskPortable4DiskId',CovertDiskPortable4DiskId)