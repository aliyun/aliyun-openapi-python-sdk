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
from aliyunsdkretailcloud.endpoint import endpoint_data

class CreatePersistentVolumeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'CreatePersistentVolume','retailcloud')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ReclaimPolicy(self):
		return self.get_body_params().get('ReclaimPolicy')

	def set_ReclaimPolicy(self,ReclaimPolicy):
		self.add_body_params('ReclaimPolicy', ReclaimPolicy)

	def get_NFSVersion(self):
		return self.get_body_params().get('NFSVersion')

	def set_NFSVersion(self,NFSVersion):
		self.add_body_params('NFSVersion', NFSVersion)

	def get_AccessModes(self):
		return self.get_body_params().get('AccessModes')

	def set_AccessModes(self,AccessModes):
		self.add_body_params('AccessModes', AccessModes)

	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)

	def get_MountTargetDomain(self):
		return self.get_body_params().get('MountTargetDomain')

	def set_MountTargetDomain(self,MountTargetDomain):
		self.add_body_params('MountTargetDomain', MountTargetDomain)

	def get_MountDir(self):
		return self.get_body_params().get('MountDir')

	def set_MountDir(self,MountDir):
		self.add_body_params('MountDir', MountDir)

	def get_ClusterInstanceId(self):
		return self.get_body_params().get('ClusterInstanceId')

	def set_ClusterInstanceId(self,ClusterInstanceId):
		self.add_body_params('ClusterInstanceId', ClusterInstanceId)

	def get_Capacity(self):
		return self.get_body_params().get('Capacity')

	def set_Capacity(self,Capacity):
		self.add_body_params('Capacity', Capacity)

	def get_StorageClass(self):
		return self.get_body_params().get('StorageClass')

	def set_StorageClass(self,StorageClass):
		self.add_body_params('StorageClass', StorageClass)