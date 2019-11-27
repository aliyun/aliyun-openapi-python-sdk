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
from aliyunsdksmc.endpoint import endpoint_data

class ModifyReplicationJobAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'smc', '2019-06-01', 'ModifyReplicationJobAttribute','smc')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TargetType(self):
		return self.get_query_params().get('TargetType')

	def set_TargetType(self,TargetType):
		self.add_query_param('TargetType',TargetType)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Frequency(self):
		return self.get_query_params().get('Frequency')

	def set_Frequency(self,Frequency):
		self.add_query_param('Frequency',Frequency)

	def get_JobId(self):
		return self.get_query_params().get('JobId')

	def set_JobId(self,JobId):
		self.add_query_param('JobId',JobId)

	def get_ImageName(self):
		return self.get_query_params().get('ImageName')

	def set_ImageName(self,ImageName):
		self.add_query_param('ImageName',ImageName)

	def get_SystemDiskSize(self):
		return self.get_query_params().get('SystemDiskSize')

	def set_SystemDiskSize(self,SystemDiskSize):
		self.add_query_param('SystemDiskSize',SystemDiskSize)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_DataDisks(self):
		return self.get_query_params().get('DataDisks')

	def set_DataDisks(self,DataDisks):
		for i in range(len(DataDisks)):	
			if DataDisks[i].get('Size') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.Size' , DataDisks[i].get('Size'))
			if DataDisks[i].get('Index') is not None:
				self.add_query_param('DataDisk.' + str(i + 1) + '.Index' , DataDisks[i].get('Index'))


	def get_ScheduledStartTime(self):
		return self.get_query_params().get('ScheduledStartTime')

	def set_ScheduledStartTime(self,ScheduledStartTime):
		self.add_query_param('ScheduledStartTime',ScheduledStartTime)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_MaxNumberOfImageToKeep(self):
		return self.get_query_params().get('MaxNumberOfImageToKeep')

	def set_MaxNumberOfImageToKeep(self,MaxNumberOfImageToKeep):
		self.add_query_param('MaxNumberOfImageToKeep',MaxNumberOfImageToKeep)