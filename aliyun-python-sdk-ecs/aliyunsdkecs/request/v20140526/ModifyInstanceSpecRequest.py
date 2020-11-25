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
from aliyunsdkecs.endpoint import endpoint_data

class ModifyInstanceSpecRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyInstanceSpec','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_AllowMigrateAcrossZone(self):
		return self.get_query_params().get('AllowMigrateAcrossZone')

	def set_AllowMigrateAcrossZone(self,AllowMigrateAcrossZone):
		self.add_query_param('AllowMigrateAcrossZone',AllowMigrateAcrossZone)

	def get_InternetMaxBandwidthOut(self):
		return self.get_query_params().get('InternetMaxBandwidthOut')

	def set_InternetMaxBandwidthOut(self,InternetMaxBandwidthOut):
		self.add_query_param('InternetMaxBandwidthOut',InternetMaxBandwidthOut)

	def get_SystemDiskCategory(self):
		return self.get_query_params().get('SystemDisk.Category')

	def set_SystemDiskCategory(self,SystemDiskCategory):
		self.add_query_param('SystemDisk.Category',SystemDiskCategory)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_TemporaryEndTime(self):
		return self.get_query_params().get('Temporary.EndTime')

	def set_TemporaryEndTime(self,TemporaryEndTime):
		self.add_query_param('Temporary.EndTime',TemporaryEndTime)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_TemporaryInternetMaxBandwidthOut(self):
		return self.get_query_params().get('Temporary.InternetMaxBandwidthOut')

	def set_TemporaryInternetMaxBandwidthOut(self,TemporaryInternetMaxBandwidthOut):
		self.add_query_param('Temporary.InternetMaxBandwidthOut',TemporaryInternetMaxBandwidthOut)

	def get_TemporaryStartTime(self):
		return self.get_query_params().get('Temporary.StartTime')

	def set_TemporaryStartTime(self,TemporaryStartTime):
		self.add_query_param('Temporary.StartTime',TemporaryStartTime)

	def get_Async(self):
		return self.get_query_params().get('Async')

	def set_Async(self,Async):
		self.add_query_param('Async',Async)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_InternetMaxBandwidthIn(self):
		return self.get_query_params().get('InternetMaxBandwidthIn')

	def set_InternetMaxBandwidthIn(self,InternetMaxBandwidthIn):
		self.add_query_param('InternetMaxBandwidthIn',InternetMaxBandwidthIn)