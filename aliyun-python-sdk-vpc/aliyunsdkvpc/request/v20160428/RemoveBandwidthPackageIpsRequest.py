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
class RemoveBandwidthPackageIpsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'RemoveBandwidthPackageIps','vpc')

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

	def get_BandwidthPackageId(self):
		return self.get_query_params().get('BandwidthPackageId')

	def set_BandwidthPackageId(self,BandwidthPackageId):
		self.add_query_param('BandwidthPackageId',BandwidthPackageId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def  set_RemovedIpAddresses_1(self, RemovedIpAddresses_1):
		self.add_query_param('RemovedIpAddresses.1', RemovedIpAddresses_1)

	def  get_RemovedIpAddresses_1(self):
		self.get_query_params().get('RemovedIpAddresses.1')

	def  set_RemovedIpAddresses_2(self, RemovedIpAddresses_2):
		self.add_query_param('RemovedIpAddresses.2', RemovedIpAddresses_2)

	def  get_RemovedIpAddresses_2(self):
		self.get_query_params().get('RemovedIpAddresses.2')

	def  set_RemovedIpAddresses_3(self, RemovedIpAddresses_3):
		self.add_query_param('RemovedIpAddresses.3', RemovedIpAddresses_3)

	def  get_RemovedIpAddresses_3(self):
		self.get_query_params().get('RemovedIpAddresses.3')

	def  set_RemovedIpAddresses_4(self, RemovedIpAddresses_4):
		self.add_query_param('RemovedIpAddresses.4', RemovedIpAddresses_4)

	def  get_RemovedIpAddresses_4(self):
		self.get_query_params().get('RemovedIpAddresses.4')

	def  set_RemovedIpAddresses_5(self, RemovedIpAddresses_5):
		self.add_query_param('RemovedIpAddresses.5', RemovedIpAddresses_5)

	def  get_RemovedIpAddresses_5(self):
		self.get_query_params().get('RemovedIpAddresses.5')

	def  set_RemovedIpAddresses_6(self, RemovedIpAddresses_6):
		self.add_query_param('RemovedIpAddresses.6', RemovedIpAddresses_6)

	def  get_RemovedIpAddresses_6(self):
		self.get_query_params().get('RemovedIpAddresses.6')

	def  set_RemovedIpAddresses_7(self, RemovedIpAddresses_7):
		self.add_query_param('RemovedIpAddresses.7', RemovedIpAddresses_7)

	def  get_RemovedIpAddresses_7(self):
		self.get_query_params().get('RemovedIpAddresses.7')

	def  set_RemovedIpAddresses_8(self, RemovedIpAddresses_8):
		self.add_query_param('RemovedIpAddresses.8', RemovedIpAddresses_8)

	def  get_RemovedIpAddresses_8(self):
		self.get_query_params().get('RemovedIpAddresses.8')

	def  set_RemovedIpAddresses_9(self, RemovedIpAddresses_9):
		self.add_query_param('RemovedIpAddresses.9', RemovedIpAddresses_9)

	def  get_RemovedIpAddresses_9(self):
		self.get_query_params().get('RemovedIpAddresses.9')

	def  set_RemovedIpAddresses_10(self, RemovedIpAddresses_10):
		self.add_query_param('RemovedIpAddresses.10', RemovedIpAddresses_10)

	def  get_RemovedIpAddresses_10(self):
		self.get_query_params().get('RemovedIpAddresses.10')

	def  set_RemovedIpAddresses_11(self, RemovedIpAddresses_11):
		self.add_query_param('RemovedIpAddresses.11', RemovedIpAddresses_11)

	def  get_RemovedIpAddresses_11(self):
		self.get_query_params().get('RemovedIpAddresses.11')

	def  set_RemovedIpAddresses_12(self, RemovedIpAddresses_12):
		self.add_query_param('RemovedIpAddresses.12', RemovedIpAddresses_12)

	def  get_RemovedIpAddresses_12(self):
		self.get_query_params().get('RemovedIpAddresses.12')

	def  set_RemovedIpAddresses_13(self, RemovedIpAddresses_13):
		self.add_query_param('RemovedIpAddresses.13', RemovedIpAddresses_13)

	def  get_RemovedIpAddresses_13(self):
		self.get_query_params().get('RemovedIpAddresses.13')

	def  set_RemovedIpAddresses_14(self, RemovedIpAddresses_14):
		self.add_query_param('RemovedIpAddresses.14', RemovedIpAddresses_14)

	def  get_RemovedIpAddresses_14(self):
		self.get_query_params().get('RemovedIpAddresses.14')

	def  set_RemovedIpAddresses_15(self, RemovedIpAddresses_15):
		self.add_query_param('RemovedIpAddresses.15', RemovedIpAddresses_15)

	def  get_RemovedIpAddresses_15(self):
		self.get_query_params().get('RemovedIpAddresses.15')

	def  set_RemovedIpAddresses_16(self, RemovedIpAddresses_16):
		self.add_query_param('RemovedIpAddresses.16', RemovedIpAddresses_16)

	def  get_RemovedIpAddresses_16(self):
		self.get_query_params().get('RemovedIpAddresses.16')

	def  set_RemovedIpAddresses_17(self, RemovedIpAddresses_17):
		self.add_query_param('RemovedIpAddresses.17', RemovedIpAddresses_17)

	def  get_RemovedIpAddresses_17(self):
		self.get_query_params().get('RemovedIpAddresses.17')

	def  set_RemovedIpAddresses_18(self, RemovedIpAddresses_18):
		self.add_query_param('RemovedIpAddresses.18', RemovedIpAddresses_18)

	def  get_RemovedIpAddresses_18(self):
		self.get_query_params().get('RemovedIpAddresses.18')

	def  set_RemovedIpAddresses_19(self, RemovedIpAddresses_19):
		self.add_query_param('RemovedIpAddresses.19', RemovedIpAddresses_19)

	def  get_RemovedIpAddresses_19(self):
		self.get_query_params().get('RemovedIpAddresses.19')

	def  set_RemovedIpAddresses_20(self, RemovedIpAddresses_20):
		self.add_query_param('RemovedIpAddresses.20', RemovedIpAddresses_20)

	def  get_RemovedIpAddresses_20(self):
		self.get_query_params().get('RemovedIpAddresses.20')
