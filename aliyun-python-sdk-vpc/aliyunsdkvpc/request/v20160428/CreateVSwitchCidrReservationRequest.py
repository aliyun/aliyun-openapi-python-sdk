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

class CreateVSwitchCidrReservationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateVSwitchCidrReservation','vpc')
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
	def get_VSwitchCidrReservationType(self): # String
		return self.get_query_params().get('VSwitchCidrReservationType')

	def set_VSwitchCidrReservationType(self, VSwitchCidrReservationType):  # String
		self.add_query_param('VSwitchCidrReservationType', VSwitchCidrReservationType)
	def get_VSwitchCidrReservationDescription(self): # String
		return self.get_query_params().get('VSwitchCidrReservationDescription')

	def set_VSwitchCidrReservationDescription(self, VSwitchCidrReservationDescription):  # String
		self.add_query_param('VSwitchCidrReservationDescription', VSwitchCidrReservationDescription)
	def get_VSwitchCidrReservationName(self): # String
		return self.get_query_params().get('VSwitchCidrReservationName')

	def set_VSwitchCidrReservationName(self, VSwitchCidrReservationName):  # String
		self.add_query_param('VSwitchCidrReservationName', VSwitchCidrReservationName)
	def get_IpVersion(self): # String
		return self.get_query_params().get('IpVersion')

	def set_IpVersion(self, IpVersion):  # String
		self.add_query_param('IpVersion', IpVersion)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
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
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_VSwitchCidrReservationMask(self): # String
		return self.get_query_params().get('VSwitchCidrReservationMask')

	def set_VSwitchCidrReservationMask(self, VSwitchCidrReservationMask):  # String
		self.add_query_param('VSwitchCidrReservationMask', VSwitchCidrReservationMask)
	def get_VSwitchCidrReservationCidr(self): # String
		return self.get_query_params().get('VSwitchCidrReservationCidr')

	def set_VSwitchCidrReservationCidr(self, VSwitchCidrReservationCidr):  # String
		self.add_query_param('VSwitchCidrReservationCidr', VSwitchCidrReservationCidr)
