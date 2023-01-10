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
from aliyunsdkdas.endpoint import endpoint_data

class ModifyAutoScalingConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'ModifyAutoScalingConfig')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Bandwidth(self): # Struct
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self, Bandwidth):  # Struct
		if Bandwidth.get('ObservationWindowSize') is not None:
			self.add_query_param('Bandwidth.ObservationWindowSize', Bandwidth.get('ObservationWindowSize'))
		if Bandwidth.get('Upgrade') is not None:
			self.add_query_param('Bandwidth.Upgrade', Bandwidth.get('Upgrade'))
		if Bandwidth.get('Apply') is not None:
			self.add_query_param('Bandwidth.Apply', Bandwidth.get('Apply'))
		if Bandwidth.get('BandwidthUsageLowerThreshold') is not None:
			self.add_query_param('Bandwidth.BandwidthUsageLowerThreshold', Bandwidth.get('BandwidthUsageLowerThreshold'))
		if Bandwidth.get('Downgrade') is not None:
			self.add_query_param('Bandwidth.Downgrade', Bandwidth.get('Downgrade'))
		if Bandwidth.get('BandwidthUsageUpperThreshold') is not None:
			self.add_query_param('Bandwidth.BandwidthUsageUpperThreshold', Bandwidth.get('BandwidthUsageUpperThreshold'))
	def get_Resource(self): # Struct
		return self.get_query_params().get('Resource')

	def set_Resource(self, Resource):  # Struct
		if Resource.get('Apply') is not None:
			self.add_query_param('Resource.Apply', Resource.get('Apply'))
		if Resource.get('Enable') is not None:
			self.add_query_param('Resource.Enable', Resource.get('Enable'))
		if Resource.get('UpgradeObservationWindowSize') is not None:
			self.add_query_param('Resource.UpgradeObservationWindowSize', Resource.get('UpgradeObservationWindowSize'))
		if Resource.get('DowngradeObservationWindowSize') is not None:
			self.add_query_param('Resource.DowngradeObservationWindowSize', Resource.get('DowngradeObservationWindowSize'))
		if Resource.get('CpuUsageUpperThreshold') is not None:
			self.add_query_param('Resource.CpuUsageUpperThreshold', Resource.get('CpuUsageUpperThreshold'))
	def get_Storage(self): # Struct
		return self.get_query_params().get('Storage')

	def set_Storage(self, Storage):  # Struct
		if Storage.get('Upgrade') is not None:
			self.add_query_param('Storage.Upgrade', Storage.get('Upgrade'))
		if Storage.get('Apply') is not None:
			self.add_query_param('Storage.Apply', Storage.get('Apply'))
		if Storage.get('MaxStorage') is not None:
			self.add_query_param('Storage.MaxStorage', Storage.get('MaxStorage'))
		if Storage.get('DiskUsageUpperThreshold') is not None:
			self.add_query_param('Storage.DiskUsageUpperThreshold', Storage.get('DiskUsageUpperThreshold'))
	def get_Spec(self): # Struct
		return self.get_query_params().get('Spec')

	def set_Spec(self, Spec):  # Struct
		if Spec.get('ObservationWindowSize') is not None:
			self.add_query_param('Spec.ObservationWindowSize', Spec.get('ObservationWindowSize'))
		if Spec.get('MaxSpec') is not None:
			self.add_query_param('Spec.MaxSpec', Spec.get('MaxSpec'))
		if Spec.get('Upgrade') is not None:
			self.add_query_param('Spec.Upgrade', Spec.get('Upgrade'))
		if Spec.get('Apply') is not None:
			self.add_query_param('Spec.Apply', Spec.get('Apply'))
		if Spec.get('MemUsageUpperThreshold') is not None:
			self.add_query_param('Spec.MemUsageUpperThreshold', Spec.get('MemUsageUpperThreshold'))
		if Spec.get('CoolDownTime') is not None:
			self.add_query_param('Spec.CoolDownTime', Spec.get('CoolDownTime'))
		if Spec.get('CpuUsageUpperThreshold') is not None:
			self.add_query_param('Spec.CpuUsageUpperThreshold', Spec.get('CpuUsageUpperThreshold'))
		if Spec.get('MaxReadOnlyNodes') is not None:
			self.add_query_param('Spec.MaxReadOnlyNodes', Spec.get('MaxReadOnlyNodes'))
		if Spec.get('Downgrade') is not None:
			self.add_query_param('Spec.Downgrade', Spec.get('Downgrade'))
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_Shard(self): # Struct
		return self.get_query_params().get('Shard')

	def set_Shard(self, Shard):  # Struct
		if Shard.get('Upgrade') is not None:
			self.add_query_param('Shard.Upgrade', Shard.get('Upgrade'))
		if Shard.get('Apply') is not None:
			self.add_query_param('Shard.Apply', Shard.get('Apply'))
		if Shard.get('MemUsageUpperThreshold') is not None:
			self.add_query_param('Shard.MemUsageUpperThreshold', Shard.get('MemUsageUpperThreshold'))
		if Shard.get('MinShards') is not None:
			self.add_query_param('Shard.MinShards', Shard.get('MinShards'))
		if Shard.get('UpgradeObservationWindowSize') is not None:
			self.add_query_param('Shard.UpgradeObservationWindowSize', Shard.get('UpgradeObservationWindowSize'))
		if Shard.get('DowngradeObservationWindowSize') is not None:
			self.add_query_param('Shard.DowngradeObservationWindowSize', Shard.get('DowngradeObservationWindowSize'))
		if Shard.get('MemUsageLowerThreshold') is not None:
			self.add_query_param('Shard.MemUsageLowerThreshold', Shard.get('MemUsageLowerThreshold'))
		if Shard.get('MaxShards') is not None:
			self.add_query_param('Shard.MaxShards', Shard.get('MaxShards'))
		if Shard.get('Downgrade') is not None:
			self.add_query_param('Shard.Downgrade', Shard.get('Downgrade'))
