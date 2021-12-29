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

class CreateLoadBalancerHTTPListenerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Slb', '2014-05-15', 'CreateLoadBalancerHTTPListener','Slb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_HealthCheckTimeout(self): # Integer
		return self.get_query_params().get('HealthCheckTimeout')

	def set_HealthCheckTimeout(self, HealthCheckTimeout):  # Integer
		self.add_query_param('HealthCheckTimeout', HealthCheckTimeout)
	def get_ListenerForward(self): # String
		return self.get_query_params().get('ListenerForward')

	def set_ListenerForward(self, ListenerForward):  # String
		self.add_query_param('ListenerForward', ListenerForward)
	def get_XForwardedFor(self): # String
		return self.get_query_params().get('XForwardedFor')

	def set_XForwardedFor(self, XForwardedFor):  # String
		self.add_query_param('XForwardedFor', XForwardedFor)
	def get_HealthCheckURI(self): # String
		return self.get_query_params().get('HealthCheckURI')

	def set_HealthCheckURI(self, HealthCheckURI):  # String
		self.add_query_param('HealthCheckURI', HealthCheckURI)
	def get_AclStatus(self): # String
		return self.get_query_params().get('AclStatus')

	def set_AclStatus(self, AclStatus):  # String
		self.add_query_param('AclStatus', AclStatus)
	def get_AclType(self): # String
		return self.get_query_params().get('AclType')

	def set_AclType(self, AclType):  # String
		self.add_query_param('AclType', AclType)
	def get_HealthCheck(self): # String
		return self.get_query_params().get('HealthCheck')

	def set_HealthCheck(self, HealthCheck):  # String
		self.add_query_param('HealthCheck', HealthCheck)
	def get_VServerGroupId(self): # String
		return self.get_query_params().get('VServerGroupId')

	def set_VServerGroupId(self, VServerGroupId):  # String
		self.add_query_param('VServerGroupId', VServerGroupId)
	def get_AclId(self): # String
		return self.get_query_params().get('AclId')

	def set_AclId(self, AclId):  # String
		self.add_query_param('AclId', AclId)
	def get_Cookie(self): # String
		return self.get_query_params().get('Cookie')

	def set_Cookie(self, Cookie):  # String
		self.add_query_param('Cookie', Cookie)
	def get_HealthCheckMethod(self): # String
		return self.get_query_params().get('HealthCheckMethod')

	def set_HealthCheckMethod(self, HealthCheckMethod):  # String
		self.add_query_param('HealthCheckMethod', HealthCheckMethod)
	def get_HealthCheckDomain(self): # String
		return self.get_query_params().get('HealthCheckDomain')

	def set_HealthCheckDomain(self, HealthCheckDomain):  # String
		self.add_query_param('HealthCheckDomain', HealthCheckDomain)
	def get_RequestTimeout(self): # Integer
		return self.get_query_params().get('RequestTimeout')

	def set_RequestTimeout(self, RequestTimeout):  # Integer
		self.add_query_param('RequestTimeout', RequestTimeout)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_LoadBalancerId(self): # String
		return self.get_query_params().get('LoadBalancerId')

	def set_LoadBalancerId(self, LoadBalancerId):  # String
		self.add_query_param('LoadBalancerId', LoadBalancerId)
	def get_XForwardedFor_SLBIP(self): # String
		return self.get_query_params().get('XForwardedFor_SLBIP')

	def set_XForwardedFor_SLBIP(self, XForwardedFor_SLBIP):  # String
		self.add_query_param('XForwardedFor_SLBIP', XForwardedFor_SLBIP)
	def get_BackendServerPort(self): # Integer
		return self.get_query_params().get('BackendServerPort')

	def set_BackendServerPort(self, BackendServerPort):  # Integer
		self.add_query_param('BackendServerPort', BackendServerPort)
	def get_HealthCheckInterval(self): # Integer
		return self.get_query_params().get('HealthCheckInterval')

	def set_HealthCheckInterval(self, HealthCheckInterval):  # Integer
		self.add_query_param('HealthCheckInterval', HealthCheckInterval)
	def get_XForwardedFor_SLBID(self): # String
		return self.get_query_params().get('XForwardedFor_SLBID')

	def set_XForwardedFor_SLBID(self, XForwardedFor_SLBID):  # String
		self.add_query_param('XForwardedFor_SLBID', XForwardedFor_SLBID)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
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
	def get_ForwardPort(self): # Integer
		return self.get_query_params().get('ForwardPort')

	def set_ForwardPort(self, ForwardPort):  # Integer
		self.add_query_param('ForwardPort', ForwardPort)
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
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_Bandwidth(self): # Integer
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self, Bandwidth):  # Integer
		self.add_query_param('Bandwidth', Bandwidth)
	def get_StickySession(self): # String
		return self.get_query_params().get('StickySession')

	def set_StickySession(self, StickySession):  # String
		self.add_query_param('StickySession', StickySession)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_Gzip(self): # String
		return self.get_query_params().get('Gzip')

	def set_Gzip(self, Gzip):  # String
		self.add_query_param('Gzip', Gzip)
	def get_IdleTimeout(self): # Integer
		return self.get_query_params().get('IdleTimeout')

	def set_IdleTimeout(self, IdleTimeout):  # Integer
		self.add_query_param('IdleTimeout', IdleTimeout)
	def get_XForwardedFor_proto(self): # String
		return self.get_query_params().get('XForwardedFor_proto')

	def set_XForwardedFor_proto(self, XForwardedFor_proto):  # String
		self.add_query_param('XForwardedFor_proto', XForwardedFor_proto)
	def get_HealthCheckConnectPort(self): # Integer
		return self.get_query_params().get('HealthCheckConnectPort')

	def set_HealthCheckConnectPort(self, HealthCheckConnectPort):  # Integer
		self.add_query_param('HealthCheckConnectPort', HealthCheckConnectPort)
	def get_HealthCheckHttpCode(self): # String
		return self.get_query_params().get('HealthCheckHttpCode')

	def set_HealthCheckHttpCode(self, HealthCheckHttpCode):  # String
		self.add_query_param('HealthCheckHttpCode', HealthCheckHttpCode)
