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

	def get_BandwidthType(self): # String
		return self.get_query_params().get('BandwidthType')

	def set_BandwidthType(self, BandwidthType):  # String
		self.add_query_param('BandwidthType', BandwidthType)
	def get_KeyPairName(self): # String
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self, KeyPairName):  # String
		self.add_query_param('KeyPairName', KeyPairName)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_BuyResourcesDetail(self): # String
		return self.get_query_params().get('BuyResourcesDetail')

	def set_BuyResourcesDetail(self, BuyResourcesDetail):  # String
		self.add_query_param('BuyResourcesDetail', BuyResourcesDetail)
	def get_SystemDiskSize(self): # String
		return self.get_query_params().get('SystemDiskSize')

	def set_SystemDiskSize(self, SystemDiskSize):  # String
		self.add_query_param('SystemDiskSize', SystemDiskSize)
	def get_InstanceBandwithdLimit(self): # String
		return self.get_query_params().get('InstanceBandwithdLimit')

	def set_InstanceBandwithdLimit(self, InstanceBandwithdLimit):  # String
		self.add_query_param('InstanceBandwithdLimit', InstanceBandwithdLimit)
	def get_EnsServiceName(self): # String
		return self.get_query_params().get('EnsServiceName')

	def set_EnsServiceName(self, EnsServiceName):  # String
		self.add_query_param('EnsServiceName', EnsServiceName)
	def get_NetLevel(self): # String
		return self.get_query_params().get('NetLevel')

	def set_NetLevel(self, NetLevel):  # String
		self.add_query_param('NetLevel', NetLevel)
	def get_DataDiskSize(self): # String
		return self.get_query_params().get('DataDiskSize')

	def set_DataDiskSize(self, DataDiskSize):  # String
		self.add_query_param('DataDiskSize', DataDiskSize)
	def get_SchedulingPriceStrategy(self): # String
		return self.get_query_params().get('SchedulingPriceStrategy')

	def set_SchedulingPriceStrategy(self, SchedulingPriceStrategy):  # String
		self.add_query_param('SchedulingPriceStrategy', SchedulingPriceStrategy)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_InstanceSpec(self): # String
		return self.get_query_params().get('InstanceSpec')

	def set_InstanceSpec(self, InstanceSpec):  # String
		self.add_query_param('InstanceSpec', InstanceSpec)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_SchedulingStrategy(self): # String
		return self.get_query_params().get('SchedulingStrategy')

	def set_SchedulingStrategy(self, SchedulingStrategy):  # String
		self.add_query_param('SchedulingStrategy', SchedulingStrategy)
