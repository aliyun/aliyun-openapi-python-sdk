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
from aliyunsdkdts.endpoint import endpoint_data

class CreateSynchronizationJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'CreateSynchronizationJob','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_networkType(self): # String
		return self.get_query_params().get('networkType')

	def set_networkType(self, networkType):  # String
		self.add_query_param('networkType', networkType)
	def get_SourceEndpointInstanceType(self): # String
		return self.get_query_params().get('SourceEndpoint.InstanceType')

	def set_SourceEndpointInstanceType(self, SourceEndpointInstanceType):  # String
		self.add_query_param('SourceEndpoint.InstanceType', SourceEndpointInstanceType)
	def get_AccountId(self): # String
		return self.get_query_params().get('AccountId')

	def set_AccountId(self, AccountId):  # String
		self.add_query_param('AccountId', AccountId)
	def get_SynchronizationJobClass(self): # String
		return self.get_query_params().get('SynchronizationJobClass')

	def set_SynchronizationJobClass(self, SynchronizationJobClass):  # String
		self.add_query_param('SynchronizationJobClass', SynchronizationJobClass)
	def get_Period(self): # String
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # String
		self.add_query_param('Period', Period)
	def get_DestRegion(self): # String
		return self.get_query_params().get('DestRegion')

	def set_DestRegion(self, DestRegion):  # String
		self.add_query_param('DestRegion', DestRegion)
	def get_Topology(self): # String
		return self.get_query_params().get('Topology')

	def set_Topology(self, Topology):  # String
		self.add_query_param('Topology', Topology)
	def get_OwnerId(self): # String
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # String
		self.add_query_param('OwnerId', OwnerId)
	def get_UsedTime(self): # Integer
		return self.get_query_params().get('UsedTime')

	def set_UsedTime(self, UsedTime):  # Integer
		self.add_query_param('UsedTime', UsedTime)
	def get_DBInstanceCount(self): # Integer
		return self.get_query_params().get('DBInstanceCount')

	def set_DBInstanceCount(self, DBInstanceCount):  # Integer
		self.add_query_param('DBInstanceCount', DBInstanceCount)
	def get_SourceRegion(self): # String
		return self.get_query_params().get('SourceRegion')

	def set_SourceRegion(self, SourceRegion):  # String
		self.add_query_param('SourceRegion', SourceRegion)
	def get_PayType(self): # String
		return self.get_query_params().get('PayType')

	def set_PayType(self, PayType):  # String
		self.add_query_param('PayType', PayType)
	def get_DestinationEndpointInstanceType(self): # String
		return self.get_query_params().get('DestinationEndpoint.InstanceType')

	def set_DestinationEndpointInstanceType(self, DestinationEndpointInstanceType):  # String
		self.add_query_param('DestinationEndpoint.InstanceType', DestinationEndpointInstanceType)
