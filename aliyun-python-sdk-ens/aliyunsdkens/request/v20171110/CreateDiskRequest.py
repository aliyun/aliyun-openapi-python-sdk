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

class CreateDiskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'CreateDisk','ens')
		self.set_method('POST')

	def get_DiskName(self): # String
		return self.get_query_params().get('DiskName')

	def set_DiskName(self, DiskName):  # String
		self.add_query_param('DiskName', DiskName)
	def get_EnsRegionId(self): # String
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_query_param('EnsRegionId', EnsRegionId)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_Size(self): # String
		return self.get_query_params().get('Size')

	def set_Size(self, Size):  # String
		self.add_query_param('Size', Size)
	def get_SnapshotId(self): # String
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self, SnapshotId):  # String
		self.add_query_param('SnapshotId', SnapshotId)
	def get_InstanceChargeType(self): # String
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self, InstanceChargeType):  # String
		self.add_query_param('InstanceChargeType', InstanceChargeType)
	def get_Encrypted(self): # Boolean
		return self.get_query_params().get('Encrypted')

	def set_Encrypted(self, Encrypted):  # Boolean
		self.add_query_param('Encrypted', Encrypted)
	def get_Category(self): # String
		return self.get_query_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_query_param('Category', Category)
	def get_KMSKeyId(self): # String
		return self.get_query_params().get('KMSKeyId')

	def set_KMSKeyId(self, KMSKeyId):  # String
		self.add_query_param('KMSKeyId', KMSKeyId)
