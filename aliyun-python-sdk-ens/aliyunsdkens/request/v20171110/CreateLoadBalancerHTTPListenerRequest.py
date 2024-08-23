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

class CreateLoadBalancerHTTPListenerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'CreateLoadBalancerHTTPListener','ens')
		self.set_method('POST')

	def get_ListenerForward(self): # String
		return self.get_query_params().get('ListenerForward')

	def set_ListenerForward(self, ListenerForward):  # String
		self.add_query_param('ListenerForward', ListenerForward)
	def get_HealthCheckTimeout(self): # Integer
		return self.get_query_params().get('HealthCheckTimeout')

	def set_HealthCheckTimeout(self, HealthCheckTimeout):  # Integer
		self.add_query_param('HealthCheckTimeout', HealthCheckTimeout)
	def get_XForwardedFor(self): # String
		return self.get_query_params().get('XForwardedFor')

	def set_XForwardedFor(self, XForwardedFor):  # String
		self.add_query_param('XForwardedFor', XForwardedFor)
	def get_HealthCheckURI(self): # String
		return self.get_query_params().get('HealthCheckURI')

	def set_HealthCheckURI(self, HealthCheckURI):  # String
		self.add_query_param('HealthCheckURI', HealthCheckURI)
	def get_HealthCheck(self): # String
		return self.get_query_params().get('HealthCheck')

	def set_HealthCheck(self, HealthCheck):  # String
		self.add_query_param('HealthCheck', HealthCheck)
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
	def get_LoadBalancerId(self): # String
		return self.get_query_params().get('LoadBalancerId')

	def set_LoadBalancerId(self, LoadBalancerId):  # String
		self.add_query_param('LoadBalancerId', LoadBalancerId)
	def get_HealthCheckInterval(self): # Integer
		return self.get_query_params().get('HealthCheckInterval')

	def set_HealthCheckInterval(self, HealthCheckInterval):  # Integer
		self.add_query_param('HealthCheckInterval', HealthCheckInterval)
	def get_BackendServerPort(self): # Integer
		return self.get_query_params().get('BackendServerPort')

	def set_BackendServerPort(self, BackendServerPort):  # Integer
		self.add_query_param('BackendServerPort', BackendServerPort)
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
	def get_ListenerPort(self): # Integer
		return self.get_query_params().get('ListenerPort')

	def set_ListenerPort(self, ListenerPort):  # Integer
		self.add_query_param('ListenerPort', ListenerPort)
	def get_IdleTimeout(self): # Integer
		return self.get_query_params().get('IdleTimeout')

	def set_IdleTimeout(self, IdleTimeout):  # Integer
		self.add_query_param('IdleTimeout', IdleTimeout)
	def get_HealthCheckConnectPort(self): # Integer
		return self.get_query_params().get('HealthCheckConnectPort')

	def set_HealthCheckConnectPort(self, HealthCheckConnectPort):  # Integer
		self.add_query_param('HealthCheckConnectPort', HealthCheckConnectPort)
	def get_HealthCheckHttpCode(self): # String
		return self.get_query_params().get('HealthCheckHttpCode')

	def set_HealthCheckHttpCode(self, HealthCheckHttpCode):  # String
		self.add_query_param('HealthCheckHttpCode', HealthCheckHttpCode)
