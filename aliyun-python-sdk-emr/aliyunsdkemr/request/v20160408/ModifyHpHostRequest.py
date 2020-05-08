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
from aliyunsdkemr.endpoint import endpoint_data

class ModifyHpHostRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ModifyHpHost','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CpuCore(self):
		return self.get_query_params().get('CpuCore')

	def set_CpuCore(self,CpuCore):
		self.add_query_param('CpuCore',CpuCore)

	def get_MemSize(self):
		return self.get_query_params().get('MemSize')

	def set_MemSize(self,MemSize):
		self.add_query_param('MemSize',MemSize)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_RackInfo(self):
		return self.get_query_params().get('RackInfo')

	def set_RackInfo(self,RackInfo):
		self.add_query_param('RackInfo',RackInfo)

	def get_Role(self):
		return self.get_query_params().get('Role')

	def set_Role(self,Role):
		self.add_query_param('Role',Role)

	def get_SerialNumber(self):
		return self.get_query_params().get('SerialNumber')

	def set_SerialNumber(self,SerialNumber):
		self.add_query_param('SerialNumber',SerialNumber)

	def get_HostType(self):
		return self.get_query_params().get('HostType')

	def set_HostType(self,HostType):
		self.add_query_param('HostType',HostType)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_HpHostDisks(self):
		return self.get_query_params().get('HpHostDisks')

	def set_HpHostDisks(self,HpHostDisks):
		for i in range(len(HpHostDisks)):	
			if HpHostDisks[i].get('DiskSize') is not None:
				self.add_query_param('HpHostDisk.' + str(i + 1) + '.DiskSize' , HpHostDisks[i].get('DiskSize'))
			if HpHostDisks[i].get('MountPath') is not None:
				self.add_query_param('HpHostDisk.' + str(i + 1) + '.MountPath' , HpHostDisks[i].get('MountPath'))
			if HpHostDisks[i].get('DiskDevice') is not None:
				self.add_query_param('HpHostDisk.' + str(i + 1) + '.DiskDevice' , HpHostDisks[i].get('DiskDevice'))


	def get_VswitchId(self):
		return self.get_query_params().get('VswitchId')

	def set_VswitchId(self,VswitchId):
		self.add_query_param('VswitchId',VswitchId)

	def get_HpHostBizId(self):
		return self.get_query_params().get('HpHostBizId')

	def set_HpHostBizId(self,HpHostBizId):
		self.add_query_param('HpHostBizId',HpHostBizId)

	def get_ExternalKey(self):
		return self.get_query_params().get('ExternalKey')

	def set_ExternalKey(self,ExternalKey):
		self.add_query_param('ExternalKey',ExternalKey)

	def get_HostName(self):
		return self.get_query_params().get('HostName')

	def set_HostName(self,HostName):
		self.add_query_param('HostName',HostName)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_InnerIp(self):
		return self.get_query_params().get('InnerIp')

	def set_InnerIp(self,InnerIp):
		self.add_query_param('InnerIp',InnerIp)

	def get_ExternalIp(self):
		return self.get_query_params().get('ExternalIp')

	def set_ExternalIp(self,ExternalIp):
		self.add_query_param('ExternalIp',ExternalIp)