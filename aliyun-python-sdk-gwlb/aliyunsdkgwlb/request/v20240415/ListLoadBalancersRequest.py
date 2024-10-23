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
from aliyunsdkgwlb.endpoint import endpoint_data

class ListLoadBalancersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Gwlb', '2024-04-15', 'ListLoadBalancers','gwlb')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_LoadBalancerNames(self): # Array
		return self.get_body_params().get('LoadBalancerNames')

	def set_LoadBalancerNames(self, LoadBalancerNames):  # Array
		for index1, value1 in enumerate(LoadBalancerNames):
			self.add_body_params('LoadBalancerNames.' + str(index1 + 1), value1)
	def get_LoadBalancerIds(self): # Array
		return self.get_body_params().get('LoadBalancerIds')

	def set_LoadBalancerIds(self, LoadBalancerIds):  # Array
		for index1, value1 in enumerate(LoadBalancerIds):
			self.add_body_params('LoadBalancerIds.' + str(index1 + 1), value1)
	def get_Skip(self): # Integer
		return self.get_body_params().get('Skip')

	def set_Skip(self, Skip):  # Integer
		self.add_body_params('Skip', Skip)
	def get_AddressIpVersion(self): # String
		return self.get_body_params().get('AddressIpVersion')

	def set_AddressIpVersion(self, AddressIpVersion):  # String
		self.add_body_params('AddressIpVersion', AddressIpVersion)
	def get_ResourceGroupId(self): # String
		return self.get_body_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_body_params('ResourceGroupId', ResourceGroupId)
	def get_ZoneIds(self): # Array
		return self.get_body_params().get('ZoneIds')

	def set_ZoneIds(self, ZoneIds):  # Array
		for index1, value1 in enumerate(ZoneIds):
			self.add_body_params('ZoneIds.' + str(index1 + 1), value1)
	def get_NextToken(self): # String
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_body_params('NextToken', NextToken)
	def get_VpcIds(self): # Array
		return self.get_body_params().get('VpcIds')

	def set_VpcIds(self, VpcIds):  # Array
		for index1, value1 in enumerate(VpcIds):
			self.add_body_params('VpcIds.' + str(index1 + 1), value1)
	def get_Tag(self): # Array
		return self.get_body_params().get('Tag')

	def set_Tag(self, Tag):  # Array
		for index1, value1 in enumerate(Tag):
			if value1.get('Key') is not None:
				self.add_body_params('Tag.' + str(index1 + 1) + '.Key', value1.get('Key'))
			if value1.get('Value') is not None:
				self.add_body_params('Tag.' + str(index1 + 1) + '.Value', value1.get('Value'))
	def get_LoadBalancerBusinessStatus(self): # String
		return self.get_body_params().get('LoadBalancerBusinessStatus')

	def set_LoadBalancerBusinessStatus(self, LoadBalancerBusinessStatus):  # String
		self.add_body_params('LoadBalancerBusinessStatus', LoadBalancerBusinessStatus)
	def get_LoadBalancerStatus(self): # String
		return self.get_body_params().get('LoadBalancerStatus')

	def set_LoadBalancerStatus(self, LoadBalancerStatus):  # String
		self.add_body_params('LoadBalancerStatus', LoadBalancerStatus)
	def get_MaxResults(self): # Integer
		return self.get_body_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_body_params('MaxResults', MaxResults)
