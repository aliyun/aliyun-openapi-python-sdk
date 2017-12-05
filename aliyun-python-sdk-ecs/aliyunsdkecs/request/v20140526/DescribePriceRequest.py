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
class DescribePriceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribePrice','ecs')

	def get_DataDisk3Size(self):
		return self.get_query_params().get('DataDisk.3.Size')

	def set_DataDisk3Size(self,DataDisk3Size):
		self.add_query_param('DataDisk.3.Size',DataDisk3Size)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_DataDisk3Category(self):
		return self.get_query_params().get('DataDisk.3.Category')

	def set_DataDisk3Category(self,DataDisk3Category):
		self.add_query_param('DataDisk.3.Category',DataDisk3Category)

	def get_IoOptimized(self):
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self,IoOptimized):
		self.add_query_param('IoOptimized',IoOptimized)

	def get_InternetMaxBandwidthOut(self):
		return self.get_query_params().get('InternetMaxBandwidthOut')

	def set_InternetMaxBandwidthOut(self,InternetMaxBandwidthOut):
		self.add_query_param('InternetMaxBandwidthOut',InternetMaxBandwidthOut)

	def get_SystemDiskCategory(self):
		return self.get_query_params().get('SystemDisk.Category')

	def set_SystemDiskCategory(self,SystemDiskCategory):
		self.add_query_param('SystemDisk.Category',SystemDiskCategory)

	def get_DataDisk4Category(self):
		return self.get_query_params().get('DataDisk.4.Category')

	def set_DataDisk4Category(self,DataDisk4Category):
		self.add_query_param('DataDisk.4.Category',DataDisk4Category)

	def get_DataDisk4Size(self):
		return self.get_query_params().get('DataDisk.4.Size')

	def set_DataDisk4Size(self,DataDisk4Size):
		self.add_query_param('DataDisk.4.Size',DataDisk4Size)

	def get_PriceUnit(self):
		return self.get_query_params().get('PriceUnit')

	def set_PriceUnit(self,PriceUnit):
		self.add_query_param('PriceUnit',PriceUnit)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_DataDisk2Category(self):
		return self.get_query_params().get('DataDisk.2.Category')

	def set_DataDisk2Category(self,DataDisk2Category):
		self.add_query_param('DataDisk.2.Category',DataDisk2Category)

	def get_DataDisk1Size(self):
		return self.get_query_params().get('DataDisk.1.Size')

	def set_DataDisk1Size(self,DataDisk1Size):
		self.add_query_param('DataDisk.1.Size',DataDisk1Size)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_Amount(self):
		return self.get_query_params().get('Amount')

	def set_Amount(self,Amount):
		self.add_query_param('Amount',Amount)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_DataDisk2Size(self):
		return self.get_query_params().get('DataDisk.2.Size')

	def set_DataDisk2Size(self,DataDisk2Size):
		self.add_query_param('DataDisk.2.Size',DataDisk2Size)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)

	def get_DataDisk1Category(self):
		return self.get_query_params().get('DataDisk.1.Category')

	def set_DataDisk1Category(self,DataDisk1Category):
		self.add_query_param('DataDisk.1.Category',DataDisk1Category)

	def get_SystemDiskSize(self):
		return self.get_query_params().get('SystemDisk.Size')

	def set_SystemDiskSize(self,SystemDiskSize):
		self.add_query_param('SystemDisk.Size',SystemDiskSize)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_InstanceNetworkType(self):
		return self.get_query_params().get('InstanceNetworkType')

	def set_InstanceNetworkType(self,InstanceNetworkType):
		self.add_query_param('InstanceNetworkType',InstanceNetworkType)