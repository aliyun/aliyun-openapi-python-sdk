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
from aliyunsdkvpc.endpoint import endpoint_data

class ListVSwitchCidrReservationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ListVSwitchCidrReservations','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_VSwitchCidrReservationType(self): # String
		return self.get_query_params().get('VSwitchCidrReservationType')

	def set_VSwitchCidrReservationType(self, VSwitchCidrReservationType):  # String
		self.add_query_param('VSwitchCidrReservationType', VSwitchCidrReservationType)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_VSwitchCidrReservationIdss(self): # RepeatList
		return self.get_query_params().get('VSwitchCidrReservationIds')

	def set_VSwitchCidrReservationIdss(self, VSwitchCidrReservationIds):  # RepeatList
		for depth1 in range(len(VSwitchCidrReservationIds)):
			self.add_query_param('VSwitchCidrReservationIds.' + str(depth1 + 1), VSwitchCidrReservationIds[depth1])
	def get_IpVersion(self): # String
		return self.get_query_params().get('IpVersion')

	def set_IpVersion(self, IpVersion):  # String
		self.add_query_param('IpVersion', IpVersion)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Tagss(self): # RepeatList
		return self.get_query_params().get('Tags')

	def set_Tagss(self, Tags):  # RepeatList
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tags.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tags.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_MaxResults(self): # Long
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_query_param('MaxResults', MaxResults)
