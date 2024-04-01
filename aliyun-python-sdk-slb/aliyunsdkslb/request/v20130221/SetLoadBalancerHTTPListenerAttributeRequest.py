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
from aliyunsdkslb.endpoint import endpoint_data

class SetLoadBalancerHTTPListenerAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Slb', '2013-02-21', 'SetLoadBalancerHTTPListenerAttribute','slb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_HealthCheckTimeout(self): # Integer
		return self.get_query_params().get('HealthCheckTimeout')

	def set_HealthCheckTimeout(self, HealthCheckTimeout):  # Integer
		self.add_query_param('HealthCheckTimeout', HealthCheckTimeout)
	def get_XForwardedFor(self): # String
		return self.get_query_params().get('XForwardedFor')

	def set_XForwardedFor(self, XForwardedFor):  # String
		self.add_query_param('XForwardedFor', XForwardedFor)
	def get_HostId(self): # String
		return self.get_query_params().get('HostId')

	def set_HostId(self, HostId):  # String
		self.add_query_param('HostId', HostId)
	def get_UnhealthyThreshold(self): # Integer
		return self.get_query_params().get('UnhealthyThreshold')

	def set_UnhealthyThreshold(self, UnhealthyThreshold):  # Integer
		self.add_query_param('UnhealthyThreshold', UnhealthyThreshold)
	def get_HealthyThreshold(self): # Integer
		return self.get_query_params().get('HealthyThreshold')

	def set_HealthyThreshold(self, HealthyThreshold):  # Integer
		self.add_query_param('HealthyThreshold', HealthyThreshold)
	def get_Scheduler(self): # String
		return self.get_query_params().get('Scheduler')

	def set_Scheduler(self, Scheduler):  # String
		self.add_query_param('Scheduler', Scheduler)
	def get_HealthCheck(self): # String
		return self.get_query_params().get('HealthCheck')

	def set_HealthCheck(self, HealthCheck):  # String
		self.add_query_param('HealthCheck', HealthCheck)
	def get_CookieTimeout(self): # Integer
		return self.get_query_params().get('CookieTimeout')

	def set_CookieTimeout(self, CookieTimeout):  # Integer
		self.add_query_param('CookieTimeout', CookieTimeout)
	def get_StickySessionType(self): # String
		return self.get_query_params().get('StickySessionType')

	def set_StickySessionType(self, StickySessionType):  # String
		self.add_query_param('StickySessionType', StickySessionType)
	def get_ListenerPort(self): # Integer
		return self.get_query_params().get('ListenerPort')

	def set_ListenerPort(self, ListenerPort):  # Integer
		self.add_query_param('ListenerPort', ListenerPort)
	def get_Cookie(self): # String
		return self.get_query_params().get('Cookie')

	def set_Cookie(self, Cookie):  # String
		self.add_query_param('Cookie', Cookie)
	def get_StickySession(self): # String
		return self.get_query_params().get('StickySession')

	def set_StickySession(self, StickySession):  # String
		self.add_query_param('StickySession', StickySession)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # String
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # String
		self.add_query_param('OwnerId', OwnerId)
	def get_URI(self): # String
		return self.get_query_params().get('URI')

	def set_URI(self, URI):  # String
		self.add_query_param('URI', URI)
	def get_LoadBalancerId(self): # String
		return self.get_query_params().get('LoadBalancerId')

	def set_LoadBalancerId(self, LoadBalancerId):  # String
		self.add_query_param('LoadBalancerId', LoadBalancerId)
	def get_Domain(self): # String
		return self.get_query_params().get('Domain')

	def set_Domain(self, Domain):  # String
		self.add_query_param('Domain', Domain)
	def get_Interval(self): # Integer
		return self.get_query_params().get('Interval')

	def set_Interval(self, Interval):  # Integer
		self.add_query_param('Interval', Interval)
