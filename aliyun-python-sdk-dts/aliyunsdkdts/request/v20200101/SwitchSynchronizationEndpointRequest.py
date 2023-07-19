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

class SwitchSynchronizationEndpointRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'SwitchSynchronizationEndpoint','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SynchronizationJobId(self): # String
		return self.get_query_params().get('SynchronizationJobId')

	def set_SynchronizationJobId(self, SynchronizationJobId):  # String
		self.add_query_param('SynchronizationJobId', SynchronizationJobId)
	def get_EndpointType(self): # String
		return self.get_query_params().get('Endpoint.Type')

	def set_EndpointType(self, EndpointType):  # String
		self.add_query_param('Endpoint.Type', EndpointType)
	def get_AccountId(self): # String
		return self.get_query_params().get('AccountId')

	def set_AccountId(self, AccountId):  # String
		self.add_query_param('AccountId', AccountId)
	def get_EndpointPort(self): # String
		return self.get_query_params().get('Endpoint.Port')

	def set_EndpointPort(self, EndpointPort):  # String
		self.add_query_param('Endpoint.Port', EndpointPort)
	def get_EndpointInstanceType(self): # String
		return self.get_query_params().get('Endpoint.InstanceType')

	def set_EndpointInstanceType(self, EndpointInstanceType):  # String
		self.add_query_param('Endpoint.InstanceType', EndpointInstanceType)
	def get_SourceEndpointOwnerID(self): # String
		return self.get_query_params().get('SourceEndpoint.OwnerID')

	def set_SourceEndpointOwnerID(self, SourceEndpointOwnerID):  # String
		self.add_query_param('SourceEndpoint.OwnerID', SourceEndpointOwnerID)
	def get_SourceEndpointRole(self): # String
		return self.get_query_params().get('SourceEndpoint.Role')

	def set_SourceEndpointRole(self, SourceEndpointRole):  # String
		self.add_query_param('SourceEndpoint.Role', SourceEndpointRole)
	def get_EndpointIP(self): # String
		return self.get_query_params().get('Endpoint.IP')

	def set_EndpointIP(self, EndpointIP):  # String
		self.add_query_param('Endpoint.IP', EndpointIP)
	def get_OwnerId(self): # String
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # String
		self.add_query_param('OwnerId', OwnerId)
	def get_EndpointInstanceId(self): # String
		return self.get_query_params().get('Endpoint.InstanceId')

	def set_EndpointInstanceId(self, EndpointInstanceId):  # String
		self.add_query_param('Endpoint.InstanceId', EndpointInstanceId)
	def get_SynchronizationDirection(self): # String
		return self.get_query_params().get('SynchronizationDirection')

	def set_SynchronizationDirection(self, SynchronizationDirection):  # String
		self.add_query_param('SynchronizationDirection', SynchronizationDirection)
