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

class PreCreateEnsServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'PreCreateEnsService','ens')
		self.set_method('POST')

	def get_BandwidthType(self):
		return self.get_query_params().get('BandwidthType')

	def set_BandwidthType(self,BandwidthType):
		self.add_query_param('BandwidthType',BandwidthType)

	def get_SchedulingPriceStrategy(self):
		return self.get_query_params().get('SchedulingPriceStrategy')

	def set_SchedulingPriceStrategy(self,SchedulingPriceStrategy):
		self.add_query_param('SchedulingPriceStrategy',SchedulingPriceStrategy)

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_InstanceSpec(self):
		return self.get_query_params().get('InstanceSpec')

	def set_InstanceSpec(self,InstanceSpec):
		self.add_query_param('InstanceSpec',InstanceSpec)

	def get_KeyPairName(self):
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self,KeyPairName):
		self.add_query_param('KeyPairName',KeyPairName)

	def get_UserData(self):
		return self.get_query_params().get('UserData')

	def set_UserData(self,UserData):
		self.add_query_param('UserData',UserData)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_BuyResourcesDetail(self):
		return self.get_query_params().get('BuyResourcesDetail')

	def set_BuyResourcesDetail(self,BuyResourcesDetail):
		self.add_query_param('BuyResourcesDetail',BuyResourcesDetail)

	def get_SystemDiskSize(self):
		return self.get_query_params().get('SystemDiskSize')

	def set_SystemDiskSize(self,SystemDiskSize):
		self.add_query_param('SystemDiskSize',SystemDiskSize)

	def get_InstanceBandwithdLimit(self):
		return self.get_query_params().get('InstanceBandwithdLimit')

	def set_InstanceBandwithdLimit(self,InstanceBandwithdLimit):
		self.add_query_param('InstanceBandwithdLimit',InstanceBandwithdLimit)

	def get_EnsServiceName(self):
		return self.get_query_params().get('EnsServiceName')

	def set_EnsServiceName(self,EnsServiceName):
		self.add_query_param('EnsServiceName',EnsServiceName)

	def get_Version(self):
		return self.get_query_params().get('Version')

	def set_Version(self,Version):
		self.add_query_param('Version',Version)

	def get_NetLevel(self):
		return self.get_query_params().get('NetLevel')

	def set_NetLevel(self,NetLevel):
		self.add_query_param('NetLevel',NetLevel)

	def get_SchedulingStrategy(self):
		return self.get_query_params().get('SchedulingStrategy')

	def set_SchedulingStrategy(self,SchedulingStrategy):
		self.add_query_param('SchedulingStrategy',SchedulingStrategy)

	def get_DataDiskSize(self):
		return self.get_query_params().get('DataDiskSize')

	def set_DataDiskSize(self,DataDiskSize):
		self.add_query_param('DataDiskSize',DataDiskSize)