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

class CreateDeliveryChannelRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceCenter', '2022-12-01', 'CreateDeliveryChannel')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_DeliveryChannelDescription(self): # String
		return self.get_query_params().get('DeliveryChannelDescription')

	def set_DeliveryChannelDescription(self, DeliveryChannelDescription):  # String
		self.add_query_param('DeliveryChannelDescription', DeliveryChannelDescription)
	def get_ResourceChangeDelivery(self): # Struct
		return self.get_query_params().get('ResourceChangeDelivery')

	def set_ResourceChangeDelivery(self, ResourceChangeDelivery):  # Struct
		if ResourceChangeDelivery.get('TargetType') is not None:
			self.add_query_param('ResourceChangeDelivery.TargetType', ResourceChangeDelivery.get('TargetType'))
		if ResourceChangeDelivery.get('SlsProperties') is not None:
			if ResourceChangeDelivery.get('SlsProperties').get('OversizedDataOssTargetArn') is not None:
				self.add_query_param('ResourceChangeDelivery.SlsProperties.OversizedDataOssTargetArn', ResourceChangeDelivery.get('SlsProperties').get('OversizedDataOssTargetArn'))
		if ResourceChangeDelivery.get('TargetArn') is not None:
			self.add_query_param('ResourceChangeDelivery.TargetArn', ResourceChangeDelivery.get('TargetArn'))
	def get_DeliveryChannelName(self): # String
		return self.get_query_params().get('DeliveryChannelName')

	def set_DeliveryChannelName(self, DeliveryChannelName):  # String
		self.add_query_param('DeliveryChannelName', DeliveryChannelName)
	def get_DeliveryChannelFilter(self): # Struct
		return self.get_query_params().get('DeliveryChannelFilter')

	def set_DeliveryChannelFilter(self, DeliveryChannelFilter):  # Struct
		if DeliveryChannelFilter.get('ResourceTypes') is not None:
			for index1, value1 in enumerate(DeliveryChannelFilter.get('ResourceTypes')):
				self.add_query_param('DeliveryChannelFilter.ResourceTypes.' + str(index1 + 1), value1)
	def get_ResourceSnapshotDelivery(self): # Struct
		return self.get_query_params().get('ResourceSnapshotDelivery')

	def set_ResourceSnapshotDelivery(self, ResourceSnapshotDelivery):  # Struct
		if ResourceSnapshotDelivery.get('TargetType') is not None:
			self.add_query_param('ResourceSnapshotDelivery.TargetType', ResourceSnapshotDelivery.get('TargetType'))
		if ResourceSnapshotDelivery.get('DeliveryTime') is not None:
			self.add_query_param('ResourceSnapshotDelivery.DeliveryTime', ResourceSnapshotDelivery.get('DeliveryTime'))
		if ResourceSnapshotDelivery.get('CustomExpression') is not None:
			self.add_query_param('ResourceSnapshotDelivery.CustomExpression', ResourceSnapshotDelivery.get('CustomExpression'))
		if ResourceSnapshotDelivery.get('SlsProperties') is not None:
			if ResourceSnapshotDelivery.get('SlsProperties').get('OversizedDataOssTargetArn') is not None:
				self.add_query_param('ResourceSnapshotDelivery.SlsProperties.OversizedDataOssTargetArn', ResourceSnapshotDelivery.get('SlsProperties').get('OversizedDataOssTargetArn'))
		if ResourceSnapshotDelivery.get('TargetArn') is not None:
			self.add_query_param('ResourceSnapshotDelivery.TargetArn', ResourceSnapshotDelivery.get('TargetArn'))
