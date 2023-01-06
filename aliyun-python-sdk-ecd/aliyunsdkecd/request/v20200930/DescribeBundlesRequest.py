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
from aliyunsdkecd.endpoint import endpoint_data

class DescribeBundlesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'DescribeBundles')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_GpuCount(self): # Float
		return self.get_query_params().get('GpuCount')

	def set_GpuCount(self, GpuCount):  # Float
		self.add_query_param('GpuCount', GpuCount)
	def get_BundleIds(self): # RepeatList
		return self.get_query_params().get('BundleId')

	def set_BundleIds(self, BundleId):  # RepeatList
		for depth1 in range(len(BundleId)):
			self.add_query_param('BundleId.' + str(depth1 + 1), BundleId[depth1])
	def get_DesktopTypeFamily(self): # String
		return self.get_query_params().get('DesktopTypeFamily')

	def set_DesktopTypeFamily(self, DesktopTypeFamily):  # String
		self.add_query_param('DesktopTypeFamily', DesktopTypeFamily)
	def get_SelectedBundle(self): # Boolean
		return self.get_query_params().get('SelectedBundle')

	def set_SelectedBundle(self, SelectedBundle):  # Boolean
		self.add_query_param('SelectedBundle', SelectedBundle)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_FromDesktopGroup(self): # Boolean
		return self.get_query_params().get('FromDesktopGroup')

	def set_FromDesktopGroup(self, FromDesktopGroup):  # Boolean
		self.add_query_param('FromDesktopGroup', FromDesktopGroup)
	def get_BundleType(self): # String
		return self.get_query_params().get('BundleType')

	def set_BundleType(self, BundleType):  # String
		self.add_query_param('BundleType', BundleType)
	def get_FotaChannel(self): # String
		return self.get_query_params().get('FotaChannel')

	def set_FotaChannel(self, FotaChannel):  # String
		self.add_query_param('FotaChannel', FotaChannel)
	def get_VolumeEncryptionEnabled(self): # Boolean
		return self.get_query_params().get('VolumeEncryptionEnabled')

	def set_VolumeEncryptionEnabled(self, VolumeEncryptionEnabled):  # Boolean
		self.add_query_param('VolumeEncryptionEnabled', VolumeEncryptionEnabled)
	def get_MemorySize(self): # Integer
		return self.get_query_params().get('MemorySize')

	def set_MemorySize(self, MemorySize):  # Integer
		self.add_query_param('MemorySize', MemorySize)
	def get_SessionType(self): # String
		return self.get_query_params().get('SessionType')

	def set_SessionType(self, SessionType):  # String
		self.add_query_param('SessionType', SessionType)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_CheckStock(self): # Boolean
		return self.get_query_params().get('CheckStock')

	def set_CheckStock(self, CheckStock):  # Boolean
		self.add_query_param('CheckStock', CheckStock)
	def get_ProtocolType(self): # String
		return self.get_query_params().get('ProtocolType')

	def set_ProtocolType(self, ProtocolType):  # String
		self.add_query_param('ProtocolType', ProtocolType)
	def get_CpuCount(self): # Integer
		return self.get_query_params().get('CpuCount')

	def set_CpuCount(self, CpuCount):  # Integer
		self.add_query_param('CpuCount', CpuCount)
	def get_SupportMultiSession(self): # Boolean
		return self.get_query_params().get('SupportMultiSession')

	def set_SupportMultiSession(self, SupportMultiSession):  # Boolean
		self.add_query_param('SupportMultiSession', SupportMultiSession)
