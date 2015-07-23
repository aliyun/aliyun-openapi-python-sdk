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
class CreateInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateInstance')

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

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_InternetMaxBandwidthIn(self):
		return self.get_query_params().get('InternetMaxBandwidthIn')

	def set_InternetMaxBandwidthIn(self,InternetMaxBandwidthIn):
		self.add_query_param('InternetMaxBandwidthIn',InternetMaxBandwidthIn)

	def get_InternetMaxBandwidthOut(self):
		return self.get_query_params().get('InternetMaxBandwidthOut')

	def set_InternetMaxBandwidthOut(self,InternetMaxBandwidthOut):
		self.add_query_param('InternetMaxBandwidthOut',InternetMaxBandwidthOut)

	def get_HostName(self):
		return self.get_query_params().get('HostName')

	def set_HostName(self,HostName):
		self.add_query_param('HostName',HostName)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_VlanId(self):
		return self.get_query_params().get('VlanId')

	def set_VlanId(self,VlanId):
		self.add_query_param('VlanId',VlanId)

	def get_InnerIpAddress(self):
		return self.get_query_params().get('InnerIpAddress')

	def set_InnerIpAddress(self,InnerIpAddress):
		self.add_query_param('InnerIpAddress',InnerIpAddress)

	def get_SystemDiskCategory(self):
		return self.get_query_params().get('SystemDiskCategory')

	def set_SystemDiskCategory(self,SystemDiskCategory):
		self.add_query_param('SystemDiskCategory',SystemDiskCategory)

	def get_SystemDiskDiskName(self):
		return self.get_query_params().get('SystemDiskDiskName')

	def set_SystemDiskDiskName(self,SystemDiskDiskName):
		self.add_query_param('SystemDiskDiskName',SystemDiskDiskName)

	def get_SystemDiskDescription(self):
		return self.get_query_params().get('SystemDiskDescription')

	def set_SystemDiskDescription(self,SystemDiskDescription):
		self.add_query_param('SystemDiskDescription',SystemDiskDescription)

	def get_DataDisk1Size(self):
		return self.get_query_params().get('DataDisk1Size')

	def set_DataDisk1Size(self,DataDisk1Size):
		self.add_query_param('DataDisk1Size',DataDisk1Size)

	def get_DataDisk1Category(self):
		return self.get_query_params().get('DataDisk1Category')

	def set_DataDisk1Category(self,DataDisk1Category):
		self.add_query_param('DataDisk1Category',DataDisk1Category)

	def get_DataDisk1SnapshotId(self):
		return self.get_query_params().get('DataDisk1SnapshotId')

	def set_DataDisk1SnapshotId(self,DataDisk1SnapshotId):
		self.add_query_param('DataDisk1SnapshotId',DataDisk1SnapshotId)

	def get_DataDisk1DiskName(self):
		return self.get_query_params().get('DataDisk1DiskName')

	def set_DataDisk1DiskName(self,DataDisk1DiskName):
		self.add_query_param('DataDisk1DiskName',DataDisk1DiskName)

	def get_DataDisk1Description(self):
		return self.get_query_params().get('DataDisk1Description')

	def set_DataDisk1Description(self,DataDisk1Description):
		self.add_query_param('DataDisk1Description',DataDisk1Description)

	def get_DataDisk1Device(self):
		return self.get_query_params().get('DataDisk1Device')

	def set_DataDisk1Device(self,DataDisk1Device):
		self.add_query_param('DataDisk1Device',DataDisk1Device)

	def get_DataDisk1DeleteWithInstance(self):
		return self.get_query_params().get('DataDisk1DeleteWithInstance')

	def set_DataDisk1DeleteWithInstance(self,DataDisk1DeleteWithInstance):
		self.add_query_param('DataDisk1DeleteWithInstance',DataDisk1DeleteWithInstance)

	def get_DataDisk2Size(self):
		return self.get_query_params().get('DataDisk2Size')

	def set_DataDisk2Size(self,DataDisk2Size):
		self.add_query_param('DataDisk2Size',DataDisk2Size)

	def get_DataDisk2Category(self):
		return self.get_query_params().get('DataDisk2Category')

	def set_DataDisk2Category(self,DataDisk2Category):
		self.add_query_param('DataDisk2Category',DataDisk2Category)

	def get_DataDisk2SnapshotId(self):
		return self.get_query_params().get('DataDisk2SnapshotId')

	def set_DataDisk2SnapshotId(self,DataDisk2SnapshotId):
		self.add_query_param('DataDisk2SnapshotId',DataDisk2SnapshotId)

	def get_DataDisk2DiskName(self):
		return self.get_query_params().get('DataDisk2DiskName')

	def set_DataDisk2DiskName(self,DataDisk2DiskName):
		self.add_query_param('DataDisk2DiskName',DataDisk2DiskName)

	def get_DataDisk2Description(self):
		return self.get_query_params().get('DataDisk2Description')

	def set_DataDisk2Description(self,DataDisk2Description):
		self.add_query_param('DataDisk2Description',DataDisk2Description)

	def get_DataDisk2Device(self):
		return self.get_query_params().get('DataDisk2Device')

	def set_DataDisk2Device(self,DataDisk2Device):
		self.add_query_param('DataDisk2Device',DataDisk2Device)

	def get_DataDisk2DeleteWithInstance(self):
		return self.get_query_params().get('DataDisk2DeleteWithInstance')

	def set_DataDisk2DeleteWithInstance(self,DataDisk2DeleteWithInstance):
		self.add_query_param('DataDisk2DeleteWithInstance',DataDisk2DeleteWithInstance)

	def get_DataDisk3Size(self):
		return self.get_query_params().get('DataDisk3Size')

	def set_DataDisk3Size(self,DataDisk3Size):
		self.add_query_param('DataDisk3Size',DataDisk3Size)

	def get_DataDisk3Category(self):
		return self.get_query_params().get('DataDisk3Category')

	def set_DataDisk3Category(self,DataDisk3Category):
		self.add_query_param('DataDisk3Category',DataDisk3Category)

	def get_DataDisk3SnapshotId(self):
		return self.get_query_params().get('DataDisk3SnapshotId')

	def set_DataDisk3SnapshotId(self,DataDisk3SnapshotId):
		self.add_query_param('DataDisk3SnapshotId',DataDisk3SnapshotId)

	def get_DataDisk3DiskName(self):
		return self.get_query_params().get('DataDisk3DiskName')

	def set_DataDisk3DiskName(self,DataDisk3DiskName):
		self.add_query_param('DataDisk3DiskName',DataDisk3DiskName)

	def get_DataDisk3Description(self):
		return self.get_query_params().get('DataDisk3Description')

	def set_DataDisk3Description(self,DataDisk3Description):
		self.add_query_param('DataDisk3Description',DataDisk3Description)

	def get_DataDisk3Device(self):
		return self.get_query_params().get('DataDisk3Device')

	def set_DataDisk3Device(self,DataDisk3Device):
		self.add_query_param('DataDisk3Device',DataDisk3Device)

	def get_DataDisk3DeleteWithInstance(self):
		return self.get_query_params().get('DataDisk3DeleteWithInstance')

	def set_DataDisk3DeleteWithInstance(self,DataDisk3DeleteWithInstance):
		self.add_query_param('DataDisk3DeleteWithInstance',DataDisk3DeleteWithInstance)

	def get_DataDisk4Size(self):
		return self.get_query_params().get('DataDisk4Size')

	def set_DataDisk4Size(self,DataDisk4Size):
		self.add_query_param('DataDisk4Size',DataDisk4Size)

	def get_DataDisk4Category(self):
		return self.get_query_params().get('DataDisk4Category')

	def set_DataDisk4Category(self,DataDisk4Category):
		self.add_query_param('DataDisk4Category',DataDisk4Category)

	def get_DataDisk4SnapshotId(self):
		return self.get_query_params().get('DataDisk4SnapshotId')

	def set_DataDisk4SnapshotId(self,DataDisk4SnapshotId):
		self.add_query_param('DataDisk4SnapshotId',DataDisk4SnapshotId)

	def get_DataDisk4DiskName(self):
		return self.get_query_params().get('DataDisk4DiskName')

	def set_DataDisk4DiskName(self,DataDisk4DiskName):
		self.add_query_param('DataDisk4DiskName',DataDisk4DiskName)

	def get_DataDisk4Description(self):
		return self.get_query_params().get('DataDisk4Description')

	def set_DataDisk4Description(self,DataDisk4Description):
		self.add_query_param('DataDisk4Description',DataDisk4Description)

	def get_DataDisk4Device(self):
		return self.get_query_params().get('DataDisk4Device')

	def set_DataDisk4Device(self,DataDisk4Device):
		self.add_query_param('DataDisk4Device',DataDisk4Device)

	def get_DataDisk4DeleteWithInstance(self):
		return self.get_query_params().get('DataDisk4DeleteWithInstance')

	def set_DataDisk4DeleteWithInstance(self,DataDisk4DeleteWithInstance):
		self.add_query_param('DataDisk4DeleteWithInstance',DataDisk4DeleteWithInstance)

	def get_NodeControllerId(self):
		return self.get_query_params().get('NodeControllerId')

	def set_NodeControllerId(self,NodeControllerId):
		self.add_query_param('NodeControllerId',NodeControllerId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_PrivateIpAddress(self):
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self,PrivateIpAddress):
		self.add_query_param('PrivateIpAddress',PrivateIpAddress)

	def get_IoOptimized(self):
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self,IoOptimized):
		self.add_query_param('IoOptimized',IoOptimized)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_InstanceChargeType(self):
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self,InstanceChargeType):
		self.add_query_param('InstanceChargeType',InstanceChargeType)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)