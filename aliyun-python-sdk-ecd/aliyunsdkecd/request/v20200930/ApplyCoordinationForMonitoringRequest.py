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

class ApplyCoordinationForMonitoringRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'ApplyCoordinationForMonitoring')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Uuid(self): # String
		return self.get_query_params().get('Uuid')

	def set_Uuid(self, Uuid):  # String
		self.add_query_param('Uuid', Uuid)
	def get_InitiatorType(self): # String
		return self.get_query_params().get('InitiatorType')

	def set_InitiatorType(self, InitiatorType):  # String
		self.add_query_param('InitiatorType', InitiatorType)
	def get_CoordinatePolicyType(self): # String
		return self.get_query_params().get('CoordinatePolicyType')

	def set_CoordinatePolicyType(self, CoordinatePolicyType):  # String
		self.add_query_param('CoordinatePolicyType', CoordinatePolicyType)
	def get_ResourceCandidatess(self): # RepeatList
		return self.get_query_params().get('ResourceCandidates')

	def set_ResourceCandidatess(self, ResourceCandidates):  # RepeatList
		for depth1 in range(len(ResourceCandidates)):
			if ResourceCandidates[depth1].get('ResourceId') is not None:
				self.add_query_param('ResourceCandidates.' + str(depth1 + 1) + '.ResourceId', ResourceCandidates[depth1].get('ResourceId'))
			if ResourceCandidates[depth1].get('ResourceProperties') is not None:
				self.add_query_param('ResourceCandidates.' + str(depth1 + 1) + '.ResourceProperties', ResourceCandidates[depth1].get('ResourceProperties'))
			if ResourceCandidates[depth1].get('ResourceName') is not None:
				self.add_query_param('ResourceCandidates.' + str(depth1 + 1) + '.ResourceName', ResourceCandidates[depth1].get('ResourceName'))
			if ResourceCandidates[depth1].get('ResourceType') is not None:
				self.add_query_param('ResourceCandidates.' + str(depth1 + 1) + '.ResourceType', ResourceCandidates[depth1].get('ResourceType'))
			if ResourceCandidates[depth1].get('OwnerWyId') is not None:
				self.add_query_param('ResourceCandidates.' + str(depth1 + 1) + '.OwnerWyId', ResourceCandidates[depth1].get('OwnerWyId'))
			if ResourceCandidates[depth1].get('ResourceRegionId') is not None:
				self.add_query_param('ResourceCandidates.' + str(depth1 + 1) + '.ResourceRegionId', ResourceCandidates[depth1].get('ResourceRegionId'))
			if ResourceCandidates[depth1].get('OwnerAliUid') is not None:
				self.add_query_param('ResourceCandidates.' + str(depth1 + 1) + '.OwnerAliUid', ResourceCandidates[depth1].get('OwnerAliUid'))
			if ResourceCandidates[depth1].get('OwnerEndUserId') is not None:
				self.add_query_param('ResourceCandidates.' + str(depth1 + 1) + '.OwnerEndUserId', ResourceCandidates[depth1].get('OwnerEndUserId'))
	def get_EndUserId(self): # String
		return self.get_query_params().get('EndUserId')

	def set_EndUserId(self, EndUserId):  # String
		self.add_query_param('EndUserId', EndUserId)
