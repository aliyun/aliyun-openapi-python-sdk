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
from aliyunsdksas.endpoint import endpoint_data

class GetCloudAssetDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'GetCloudAssetDetail','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AssetSubType(self): # Integer
		return self.get_query_params().get('AssetSubType')

	def set_AssetSubType(self, AssetSubType):  # Integer
		self.add_query_param('AssetSubType', AssetSubType)
	def get_Vendor(self): # Integer
		return self.get_query_params().get('Vendor')

	def set_Vendor(self, Vendor):  # Integer
		self.add_query_param('Vendor', Vendor)
	def get_AssetType(self): # Integer
		return self.get_query_params().get('AssetType')

	def set_AssetType(self, AssetType):  # Integer
		self.add_query_param('AssetType', AssetType)
	def get_CloudAssetInstancess(self): # RepeatList
		return self.get_query_params().get('CloudAssetInstances')

	def set_CloudAssetInstancess(self, CloudAssetInstances):  # RepeatList
		for depth1 in range(len(CloudAssetInstances)):
			if CloudAssetInstances[depth1].get('InstanceId') is not None:
				self.add_query_param('CloudAssetInstances.' + str(depth1 + 1) + '.InstanceId', CloudAssetInstances[depth1].get('InstanceId'))
			if CloudAssetInstances[depth1].get('RegionId') is not None:
				self.add_query_param('CloudAssetInstances.' + str(depth1 + 1) + '.RegionId', CloudAssetInstances[depth1].get('RegionId'))
