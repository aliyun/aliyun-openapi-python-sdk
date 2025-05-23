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
class DescribeContainerLogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eci', '2018-08-08', 'DescribeContainerLog','eci')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ContainerName(self):
		return self.get_query_params().get('ContainerName')

	def set_ContainerName(self,ContainerName):
		self.add_query_param('ContainerName',ContainerName)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_ContainerGroupId(self):
		return self.get_query_params().get('ContainerGroupId')

	def set_ContainerGroupId(self,ContainerGroupId):
		self.add_query_param('ContainerGroupId',ContainerGroupId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_Tail(self):
		return self.get_query_params().get('Tail')

	def set_Tail(self,Tail):
		self.add_query_param('Tail',Tail)

	def get_LastTime(self):
		return self.get_query_params().get('LastTime')

	def set_LastTime(self,LastTime):
		self.add_query_param('LastTime',LastTime)

	def get_SinceSeconds(self):
		return self.get_query_params().get('SinceSeconds')

	def set_SinceSeconds(self,SinceSeconds):
		self.add_query_param('SinceSeconds',SinceSeconds)

	def get_LimitBytes(self):
		return self.get_query_params().get('LimitBytes')

	def set_LimitBytes(self,LimitBytes):
		self.add_query_param('LimitBytes',LimitBytes)

	def get_Timestamps(self):
		return self.get_query_params().get('Timestamps')

	def set_Timestamps(self,Timestamps):
		self.add_query_param('Timestamps',Timestamps)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)