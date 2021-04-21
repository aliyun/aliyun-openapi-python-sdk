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
from aliyunsdkdbfs.endpoint import endpoint_data

class CreateDbfsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DBFS', '2020-04-18', 'CreateDbfs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SizeG(self):
		return self.get_query_params().get('SizeG')

	def set_SizeG(self,SizeG):
		self.add_query_param('SizeG',SizeG)

	def get_SnapshotId(self):
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self,SnapshotId):
		self.add_query_param('SnapshotId',SnapshotId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_UsedScene(self):
		return self.get_query_params().get('UsedScene')

	def set_UsedScene(self,UsedScene):
		self.add_query_param('UsedScene',UsedScene)

	def get_FsName(self):
		return self.get_query_params().get('FsName')

	def set_FsName(self,FsName):
		self.add_query_param('FsName',FsName)

	def get_RaidStripeUnitNumber(self):
		return self.get_query_params().get('RaidStripeUnitNumber')

	def set_RaidStripeUnitNumber(self,RaidStripeUnitNumber):
		self.add_query_param('RaidStripeUnitNumber',RaidStripeUnitNumber)

	def get_Encryption(self):
		return self.get_query_params().get('Encryption')

	def set_Encryption(self,Encryption):
		self.add_query_param('Encryption',Encryption)

	def get_PerformanceLevel(self):
		return self.get_query_params().get('PerformanceLevel')

	def set_PerformanceLevel(self,PerformanceLevel):
		self.add_query_param('PerformanceLevel',PerformanceLevel)

	def get_EnableRaid(self):
		return self.get_query_params().get('EnableRaid')

	def set_EnableRaid(self,EnableRaid):
		self.add_query_param('EnableRaid',EnableRaid)

	def get_DeleteSnapshot(self):
		return self.get_query_params().get('DeleteSnapshot')

	def set_DeleteSnapshot(self,DeleteSnapshot):
		self.add_query_param('DeleteSnapshot',DeleteSnapshot)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_Category(self):
		return self.get_query_params().get('Category')

	def set_Category(self,Category):
		self.add_query_param('Category',Category)

	def get_KMSKeyId(self):
		return self.get_query_params().get('KMSKeyId')

	def set_KMSKeyId(self,KMSKeyId):
		self.add_query_param('KMSKeyId',KMSKeyId)