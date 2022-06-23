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
from aliyunsdkcbn.endpoint import endpoint_data

class CreateCenInterRegionTrafficQosPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'CreateCenInterRegionTrafficQosPolicy')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_TrafficQosQueuess(self): # RepeatList
		return self.get_query_params().get('TrafficQosQueues')

	def set_TrafficQosQueuess(self, TrafficQosQueues):  # RepeatList
		for depth1 in range(len(TrafficQosQueues)):
			if TrafficQosQueues[depth1].get('Dscps') is not None:
				for depth2 in range(len(TrafficQosQueues[depth1].get('Dscps'))):
					self.add_query_param('TrafficQosQueues.' + str(depth1 + 1) + '.Dscps.' + str(depth2 + 1), TrafficQosQueues[depth1].get('Dscps')[depth2])
			if TrafficQosQueues[depth1].get('QosQueueName') is not None:
				self.add_query_param('TrafficQosQueues.' + str(depth1 + 1) + '.QosQueueName', TrafficQosQueues[depth1].get('QosQueueName'))
			if TrafficQosQueues[depth1].get('RemainBandwidthPercent') is not None:
				self.add_query_param('TrafficQosQueues.' + str(depth1 + 1) + '.RemainBandwidthPercent', TrafficQosQueues[depth1].get('RemainBandwidthPercent'))
			if TrafficQosQueues[depth1].get('QosQueueDescription') is not None:
				self.add_query_param('TrafficQosQueues.' + str(depth1 + 1) + '.QosQueueDescription', TrafficQosQueues[depth1].get('QosQueueDescription'))
	def get_TrafficQosPolicyName(self): # String
		return self.get_query_params().get('TrafficQosPolicyName')

	def set_TrafficQosPolicyName(self, TrafficQosPolicyName):  # String
		self.add_query_param('TrafficQosPolicyName', TrafficQosPolicyName)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_TrafficQosPolicyDescription(self): # String
		return self.get_query_params().get('TrafficQosPolicyDescription')

	def set_TrafficQosPolicyDescription(self, TrafficQosPolicyDescription):  # String
		self.add_query_param('TrafficQosPolicyDescription', TrafficQosPolicyDescription)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_TransitRouterId(self): # String
		return self.get_query_params().get('TransitRouterId')

	def set_TransitRouterId(self, TransitRouterId):  # String
		self.add_query_param('TransitRouterId', TransitRouterId)
	def get_TransitRouterAttachmentId(self): # String
		return self.get_query_params().get('TransitRouterAttachmentId')

	def set_TransitRouterAttachmentId(self, TransitRouterAttachmentId):  # String
		self.add_query_param('TransitRouterAttachmentId', TransitRouterAttachmentId)
